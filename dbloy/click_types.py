from click import ParamType


class DeployYmlClickType(ParamType):
    name = 'DEPLOY_YML'
    help = ('Deployment manifest')
