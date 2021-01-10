from aws_cdk import (
    core,
    aws_iam as iam
)


class CfnguardPipelineDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cloud_formation_role = iam.Role(self, "CloudFormationCfnGuardDemo",
            assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"),
            description="CodePipeline role with trusted relationship for CFN"
        )

        cloud_formation_role.add_to_policy(iam.PolicyStatement(
            sid="AllowCreateServiceLinkedRoleWithConditions",
            resources=["*"],
            actions=["iam:CreateServiceLinkedRole"],
            conditions={
                "StringEquals":[
                    {"iam:AWSServiceName":[
                        "autoscaling.amazonaws.com",
                        "ec2scheduled.amazonaws.com",
                        "elasticloadbalancing.amazonaws.com"
                        ]
                    }
                ]
            }
        ))

        cloud_formation_role.add_to_policy(iam.PolicyStatement(
            sid="AllowCloudFormationDoItsJob",
            resources=["*"],
            actions=[
                "s3:GetObjectAcl",
                "s3:GetObject",
                "cloudwatch:*",
                "ec2:*",
                "autoscaling:*",
                "s3:List*",
                "s3:HeadBucket"
            ]
        ))

        code_pipeline_role = iam.Role(self, "CodePipelineCfnGuardDemo",
            assumed_by=iam.ServicePrincipal("cloudformation.amazonaws.com"),
            description="CodePipeline role with trusted relationship for CloudFormation"
        )

        code_pipeline_role.add_to_policy(iam.PolicyStatement(
            sid="AllowPassRoleWithConditions",
            resources=["*"],
            actions=["iam:PassRole"],
            conditions={
                "StringEqualsIfExists":[
                    {"iam:PassedToService":["cloudformation.amazonaws.com","ec2.amazonaws.com"]}
                ]
            }
        ))

        code_pipeline_role.add_to_policy(iam.PolicyStatement(
            sid="AllowCodePipelineDoItsJob",
            resources=["*"],
            actions=[
                "codecommit:UploadArchive",
                "codecommit:CancelUploadArchive",
                "codecommit:GetCommit",
                "codecommit:GetUploadArchiveStatus",
                "codecommit:GetBranch",
                "codestar-connections:UseConnection",
                "codebuild:BatchGetBuilds",
                "codedeploy:CreateDeployment",
                "codedeploy:GetApplicationRevision",
                "codedeploy:RegisterApplicationRevision",
                "codedeploy:GetDeploymentConfig",
                "codedeploy:GetDeployment",
                "codebuild:StartBuild",
                "codedeploy:GetApplication",
                "s3:*",
                "cloudformation:*",
                "ec2:*"
            ]
        ))

        core.CfnOutput(self, "CloudFormationRoleArn", value=cloud_formation_role.role_arn)
        core.CfnOutput(self, "CloudFormationRoleId", value=cloud_formation_role.role_id)
        core.CfnOutput(self, "CodePipelineRoleArn", value=code_pipeline_role.role_arn)
        core.CfnOutput(self, "CodePipelineRoleId", value=code_pipeline_role.role_id)
    