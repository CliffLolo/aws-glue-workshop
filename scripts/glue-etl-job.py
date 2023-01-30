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


