import aws_cdk as core
import aws_cdk.assertions as assertions

from test1.test1_stack import Test1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in test1/test1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Test1Stack(app, "test1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
