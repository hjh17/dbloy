import yaml

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def read_yml(yml_path):
    with open(yml_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
