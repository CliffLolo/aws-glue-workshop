from pyspark.sql.functions import udf, col
from pyspark.sql.types import IntegerType, StringType
from pyspark import SparkContext
from pyspark.sql import SQLContext

from datetime import datetime

# Copyright (c) 2017 TUNE, Inc. All rights reserved.
from pycountry_convert import (
    convert_country_alpha2_to_country_name,
    convert_country_alpha2_to_continent,
    convert_country_name_to_country_alpha2,
    convert_country_alpha3_to_country_alpha2,
)


def get_country_code2(country_name):
    country_code2 = 'US'
    try:
        country_code2 = convert_country_name_to_country_alpha2(country_name)
    except KeyError:
        country_code2 = ''
    return country_code2


udf_get_country_code2 = udf(lambda z: get_country_code2(z), StringType())

sparkDF = spark.read.load("s3://${BUCKET_NAME}/input/lab2/sample.csv",
                          format="csv",
                          sep=",",
                          inferSchema="true",
                          header="true")
sparkDF.printSchema()
new_df = sparkDF.withColumn('country_code_2', udf_get_country_code2(col("Country")))
new_df.printSchema()
new_df.show(10)

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

glueContext = GlueContext(SparkContext.getOrCreate())

dynaFrame = glueContext.create_dynamic_frame.from_catalog(database="glueworkshop", table_name="csv")
dynaFrame.printSchema()
dynaFrame.toDF().show(10)


