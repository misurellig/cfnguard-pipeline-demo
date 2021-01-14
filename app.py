#!/usr/bin/env python3
import os
from aws_cdk import core

from cfnguard_pipeline_demo.cfnguard_pipeline_demo_stack import CfnguardPipelineDemoStack
from cfnguard_pipeline_demo.roles_permissions_stack import RolesPermissionsStack


app = core.App()
ns = CfnguardPipelineDemoStack(app, "cfnguard-pipeline-demo", env=core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]))
)

roles_permissions = RolesPermissionsStack(app, "RolesPermissionsStack")
roles_permissions.add_dependency(ns)

app.synth()
