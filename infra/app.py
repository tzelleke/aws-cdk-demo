import os
from aws_cdk import core as cdk
from stacks.web_api import WebApi

app = cdk.App()

env = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)

WebApi(app, "WebApi", env=env)

app.synth()
