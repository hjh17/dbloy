import click
from databricks_cli.configure.config import provide_api_client
from databricks_cli.sdk import JobsService

from dbloy.click_types import DeployYmlClickType
from dbloy.util import CONTEXT_SETTINGS, read_yml


@click.command(context_settings=CONTEXT_SETTINGS, short_help='Updates a Databricks Job based on config definition.')
@provide_api_client
@click.option('--deploy-yml', required=True, type=DeployYmlClickType(), help=DeployYmlClickType.help)
@click.option('--configmap-yml', required=True, type=DeployYmlClickType(), help=DeployYmlClickType.help)
@click.option('--version', required=True, help="Deployment version")
def apply(api_client, deploy_yml, configmap_yml, version):
    deploy_config = read_yml(deploy_yml)
    config_map = read_yml(configmap_yml)
    job_service = JobsService(api_client)
    json_obj = _construct_job_payload(config_map, deploy_config, version)
    job_service.reset_job(json_obj["job_id"], json_obj)


def _construct_job_payload(config_map, deploy_config, version):
    for i, lib in enumerate(deploy_config["template"]["libraries"]):
        if "egg_main" in lib:
            main_egg = deploy_config["template"]["libraries"].pop(i)
            main_egg = main_egg["egg_main"].replace("VERSION", version)
            deploy_config["template"]["libraries"].append({"egg": main_egg})

    if "notebooks" in deploy_config["template"]:
        for notebook_info in deploy_config["template"]["notebooks"]:
            for key, value in notebook_info.items():
                path = "/{}/{}/{}/{}/{}".format(deploy_config["metadata"]["workspace"],
                                                deploy_config["metadata"]["name"], config_map["metadata"]["namespace"],
                                                version,
                                                value)
                config_map["params"][key] = path

    data = {
        "name": "{} - {} v{}".format(deploy_config["template"]["job"]["name"], config_map["metadata"]["namespace"],
                                     version),
        "job_id": config_map["job"]["id"],
        "email_notifications": deploy_config["template"]["notifications"]["email"],
        "libraries": deploy_config["template"]["libraries"],
        "max_concurrent_runs": deploy_config["template"]["run"]["max_concurrent_runs"],
        "max_retries": config_map["job"]["max_retries"],
        "min_retry_interval_millis": deploy_config["template"]["run"]["min_retry_interval_millis"],
        "notebook_task": {
            "base_parameters": config_map["params"],
            "notebook_path": "/{}/{}/{}/{}/{}".format(deploy_config["metadata"]["workspace"],
                                                      deploy_config["metadata"]["name"],
                                                      config_map["metadata"]["namespace"],
                                                      version, deploy_config["template"]["base_notebook"])
        },
        "retry_on_timeout": deploy_config["template"]["run"]["retry_on_timeout"],

        "timeout_seconds": deploy_config["template"]["run"]["timeout_seconds"]
    }

    if "cluster_id" in config_map["cluster"]:
        data["existing_cluster_id"] = config_map["cluster"]["cluster_id"]
    else:
        data["new_cluster"] = config_map["cluster"]

    if "schedule" in config_map["job"]:
        data["schedule"] = config_map["job"]["schedule"]
    return data
