from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_kms as kms,
    RemovalPolicy,
    aws_s3_deployment as s3deploy
)
from constructs import Construct
import aws_cdk as cdk

class bucketboot(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")

        # s3 bucket ####
        bucketscript=s3.Bucket(self,"bucketBootstrap",
                                encryption=s3.BucketEncryption.KMS,
                                    removal_policy=cdk.RemovalPolicy.DESTROY,
                                        auto_delete_objects=True)
        

        ### S3 bucket deployment ######

        s3deploy.BucketDeployment(
            self,"deploy",
            sources=[s3deploy.Source.asset("./Bucket")],
            destination_bucket=bucketscript
        )