#!/usr/bin/env python3
import os
from aws_cdk import core

from cfnguard_pipeline_demo.cfnguard_pipeline_demo_stack import CfnguardPipelineDemoStack


app = core.App()
CfnguardPipelineDemoStack(app, "cfnguard-pipeline-demo", env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]))
)

app.synth()
