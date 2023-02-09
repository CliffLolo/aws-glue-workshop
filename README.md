# AWS GLUE WORKSHOP

### Creating s3 bucket and cloning required files
```
BUCKET_NAME=<give your bucket a name>
aws s3 mb s3://${BUCKET_NAME}
aws s3api put-public-access-block --bucket ${BUCKET_NAME} \
  --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
echo ${BUCKET_NAME}
```

This above script is performing the following actions:
1. Creating an S3 bucket with the name specified in the BUCKET_NAME variable.
2. Using the S3 API to set the public access block configuration for the S3 bucket, which includes blocking public access to the bucket's ACLs and policies, and restricting public access to the bucket.
3. Printing the name of the created bucket.

Basically, the script is creating an S3 bucket and then making sure it's private by applying public access block configuration. 

### Downloading the lab files
```
cd ~/environment
curl 'https://static.us-east-1.prod.workshops.aws/public/a1abfb93-c66c-46be-a661-da71865ece0b/static/download/glue-workshop.zip' --output glue-workshop.zip
unzip glue-workshop.zip
mkdir ~/environment/glue-workshop/library
mkdir ~/environment/glue-workshop/output

git clone https://github.com/jefftune/pycountry-convert.git
cd ~/environment/pycountry-convert
zip -r pycountry_convert.zip pycountry_convert/
mv ~/environment/pycountry-convert/pycountry_convert.zip ~/environment/glue-workshop/library/

cd ~/environment/glue-workshop
aws s3 cp --recursive ~/environment/glue-workshop/code/ s3://${BUCKET_NAME}/script/
aws s3 cp --recursive ~/environment/glue-workshop/data/ s3://${BUCKET_NAME}/input/
aws s3 cp --recursive ~/environment/glue-workshop/library/ s3://${BUCKET_NAME}/library/
aws s3 cp --recursive s3://covid19-lake/rearc-covid-19-testing-data/json/states_daily/ s3://${BUCKET_NAME}/input/lab5/json/

```

This above script is performing the following actions:
1. Changing the current directory to "~/environment"
2. Downloading a file named "glue-workshop.zip" from a specified URL and saving it as "glue-workshop.zip" in the current directory
3. Unzipping the "glue-workshop.zip" file in the current directory
4. Creating a directory named "library" in "~/environment/glue-workshop"
5. Creating a directory named "output" in "~/environment/glue-workshop"
6. Cloning a git repository named "pycountry-convert" from a specified URL
7. Changing the current directory to "~/environment/pycountry-convert"
8. Zipping the contents of the "pycountry_convert" directory and saving the zip as "pycountry_convert.zip" in the current directory
9. Moving the "pycountry_convert.zip" file to "~/environment/glue-workshop/library"
10. Changing the current directory to "~/environment/glue-workshop"
11. Copying the contents of the "code" directory to an S3 bucket under the "script" directory
12. Copying the contents of the "data" directory to an S3 bucket under the "input" directory
13. Copying the contents of the "library" directory to an S3 bucket under the "library" directory
14. Copying the contents of the "states_daily" directory from a specified S3 bucket to an S3 bucket under the "input/lab5/json" directory.

Basically, the script downloads a zip file, unzips it, creates some directories, clones a git repository, zips a directory within it, moves it, and finally copies various directories to an S3 bucket.

### Creating Cloudformation stack

```
aws cloudformation create-stack --stack-name glueworkshop \
            --template-body file://~/environment/glue-workshop/cloudformation/NoVPC.yaml \
            --capabilities CAPABILITY_NAMED_IAM \
            --region us-east-2 \
            --parameters \
            ParameterKey=UniquePostfix,ParameterValue=glueworkshop \
            ParameterKey=S3Bucket,ParameterValue=s3://${BUCKET_NAME}/
```

The script above is using the AWS CloudFormation service to create a new CloudFormation stack named "glueworkshop". The following actions are being performed:
1. Using the aws cloudformation create-stack command to create a new CloudFormation stack.
2. The --stack-name parameter is set to "glueworkshop", which is the name of the stack being created.
3. The --template-body parameter is set to "file://~/environment/glue-workshop/cloudformation/NoVPC.yaml", which specifies the location of the CloudFormation template file that will be used to create the stack.
4. The --capabilities parameter is set to "CAPABILITY_NAMED_IAM", which is a required capability when the template includes IAM resources.
5. The --region parameter is set to "us-east-2", which specifies the region in which the stack will be created.
    * The --parameters parameter is used to pass two key-value pairs as parameters to the CloudFormation template:
    * ParameterKey=UniquePostfix,ParameterValue=glueworkshop
    * ParameterKey=S3Bucket,ParameterValue=s3://${BUCKET_NAME}/

Basically, the script is creating a CloudFormation stack. It uses a CloudFormation template file stored locally and it creates the stack in the us-east-2 region. The script also sets two parameters that are passed to the CloudFormation template when creating the stack.

Run the following command in the terminal to view the first 10 lines of the sample data:
```
head ~/environment/glue-workshop/data/lab1/csv/sample.csv
```

```angular2html
aws s3 cp s3://${BUCKET_NAME}/output/ ~/environment/glue-workshop/output --recursive

```

```angular2html
 aws glue create-job \
    --name glueworkshop_lab4_glue_streaming \
    --role AWSGlueServiceRole-glueworkshop  \
    --command "Name=gluestreaming,ScriptLocation=s3://${BUCKET_NAME}/script/lab4/streaming.py,PythonVersion=3" \
    --glue-version "2.0" \
    --default-arguments "{\"--s3_bucket\": \"s3://${BUCKET_NAME}/\" }" \
    --region us-east-2

```