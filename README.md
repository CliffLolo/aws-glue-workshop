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

