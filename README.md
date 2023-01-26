# AWS GLUE WORKSHOP

### Creating s3 bucket and cloning required files
```bash
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