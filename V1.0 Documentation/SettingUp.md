
###   


## Install AWS CDK



1. All AWS CDK developers, even those working in Python, Java, or C#, need[Node.js](https://nodejs.org/en/download/) 10.13.0 or later.
2. Install the AWS CDK Toolkit globally using the following Node Package Manager command.

        npm install -g aws-cdk

3. Run the following command to verify correct installation and print the version number of the AWS CDK.
        
        cdk --version
4. Many AWS CDK stacks that you write will include[assets](https://docs.aws.amazon.com/cdk/v2/guide/assets.html): external files that are deployed with the stack, such as AWS Lambda functions or Docker images. The AWS CDK uploads these to an Amazon S3 bucket or other container so they are available to AWS CloudFormation during deployment. Deployment requires that these containers already exist in the account and region you are deploying into.

        cdk bootstrap aws://ACCOUNT-NUMBER/REGION


## Creating App


The standard AWS CDK development workflow is similar to the workflow you're already familiar with as a developer, just with a few extra steps.
1. Create the app from a template provided by the AWS CDK
2. Add code to the app to create resources within stacks
3. Build the app (optional; the AWS CDK Toolkit will do it for you if you forget)
4. Synthesize one or more stacks in the app to create an AWS CloudFormation template
5. Deploy one or more stacks to your AWS account

Steps:
1. Each AWS CDK app should be in its own directory, with its own local module dependencies.
 Create a new directory for your app.

         mkdir CDK-Project
         cd CDK-Project
 
 2. Now initialize the app using the    **cdk init** command, specifying the desired template ("app") and programming language.
 
        cdk init app --language python
3. After the app has been created, also enter the following two commands to activate the app's Python virtual environment and install the AWS CDK core dependencies.

        To manually create a virtualenv on MacOS and Linux:


         $ python -m venv .venv

         After the init process completes and the virtualenv is created, you can use the following step to activate your virtualenv.

         $ source .venv/bin/activate

        If you are a Windows platform, you would activate the virtualenv like this:

         %.venv\Scripts\activate.bat

         Once the virtualenv is activated, you can install the required dependencies.


        python -m pip install -r requirements.txt


4. You can now Synthesize your app. The cdk synthesize command synthesizes a stack defined in your app into a CloudFormation template.

         cdk synth
5. The cdk deploy subcommand deploys the specified stack(s) to your AWS account.

        cdk deploy 


 
 ![](https://lh5.googleusercontent.com/F0ESoNOE9cc6AqluQjR_sZ0ikyzBdyVmVpgyeu3F1Lbt6N-8DEtSd2mZ6JFM-beYajTUCXIAUtHm20KdaA8YgMcU4YYm74YNVpyecDPMxJQWH-Tufs80fgWtU_IP1oTgUHFHkTMc)  

  
