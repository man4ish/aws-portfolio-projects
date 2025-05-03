import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

# Initialize GlueContext and SparkContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Input arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Read data from an S3 source
input_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="my_database", 
    table_name="my_s3_table", 
    transformation_ctx="input_dynamic_frame"
)

# Perform transformation (example: filter data where age > 30)
transformed_dynamic_frame = input_dynamic_frame.filter(lambda x: x["age"] > 30)

# Write the transformed data to Amazon Redshift
glueContext.write_dynamic_frame.from_options(
    transformed_dynamic_frame, 
    connection_type="redshift", 
    connection_options={"url": "jdbc:redshift://your-cluster-url:5439/database", 
                        "dbtable": "target_table", 
                        "user": "username", 
                        "password": "password"},
    transformation_ctx="output_dynamic_frame"
)
