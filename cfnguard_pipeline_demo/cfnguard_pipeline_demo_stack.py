from aws_cdk import (
    core,
    aws_iam as iam,
    aws_codecommit as codecommit
)


class CfnguardPipelineDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        repo = codecommit.Repository(self, "Repository",
            repository_name="cfnguard-demo",
            description="CFN code to demo at the checkride."
        )

        core.CfnOutput(self, "RepositoryCloneUrlGrc", value=repo.repository_clone_url_grc)
    