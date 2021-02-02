from aws_cdk import (
    core,
    aws_iam as iam,
    aws_codecommit as codecommit,
    aws_codebuild as codebuild
)


class CfnguardPipelineDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        ccommit_repo = self.node.try_get_context("ccommit_repo")
        ccommit_repo_desc = self.node.try_get_context("ccommit_repo_desc")
        cbuild_specfile = self.node.try_get_context("cbuild_specfile")
        cbuild_docker_repo = self.node.try_get_context("cbuild_docker_repo")

        repo = codecommit.Repository(self, "Repository",
            repository_name=ccommit_repo,
            description=ccommit_repo_desc
        )

        build_project = codebuild.Project(self, "CfnGuardDemo",
            description="AWS CloudFormation Guard demo project - created with CDK",
            source=codebuild.Source.code_commit(repository=repo),
            build_spec=codebuild.BuildSpec.from_source_filename(cbuild_specfile),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.from_docker_registry(cbuild_docker_repo),
                # compute_type="Linux",
                # privileged=False
            )
        )

        core.CfnOutput(self, "RepositoryCloneUrlGrc", value=repo.repository_clone_url_grc)
        core.CfnOutput(self, "CodeBuildProject", value=build_project.project_arn)
    