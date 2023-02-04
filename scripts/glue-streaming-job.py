import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, StringType
from pyspark import SparkContext
from pyspark.sql import SQLContext
from datetime import datetime

glueContext = GlueContext(SparkContext.getOrCreate())
s3_bucket = "s3://${BUCKET_NAME}"
output_path = s3_bucket + "/output/lab4/notebook/"
job_time_string = datetime.now().strftime("%Y%m%d%H%M%S")
s3_target = output_path + job_time_string

country_lookup_frame = glueContext.create_dynamic_frame.from_options(
                            format_options = {"withHeader":True, "separator":',', "quoteChar":"\""},
                            connection_type = "s3",
                            format = "csv",
                            connection_options = {"paths": [s3_bucket + "/input/lab4/country_lookup/"], "recurse":True},
                            transformation_ctx = "country_lookup_frame")
