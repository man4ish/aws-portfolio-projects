"""
train_model.py
--------------

This script trains a machine learning model using Amazon SageMaker.
It uploads the dataset to S3, initiates a SageMaker training job, and saves the model artifacts to S3.
"""

import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn import SKLearnModel
from sagemaker.inputs import TrainingInput
import os
from sklearn.datasets import load_iris
import pandas as pd

# Initialize session and S3 bucket
sagemaker_session = sagemaker.Session()
role = get_execution_role()
bucket = "your-s3-bucket-name"  # Replace with your S3 bucket name

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['target'])

# Save the dataset to CSV
data = pd.concat([X, y], axis=1)
data.to_csv('/tmp/iris.csv', index=False)

# Upload dataset to S3
s3_data_path = f"s3://{bucket}/data/iris.csv"
s3 = boto3.client('s3')
s3.upload_file('/tmp/iris.csv', bucket, 'data/iris.csv')

# Configure and run SageMaker training job
estimator = sagemaker.estimator.Estimator(
    image_uri=sagemaker.image_uris.retrieve('sklearn', sagemaker_session.boto_region_name),
    role=role,
    instance_type='ml.m5.large',
    instance_count=1,
    output_path=f"s3://{bucket}/output",
    sagemaker_session=sagemaker_session
)

# Define input data for training
train_input = TrainingInput(s3_data=s3_data_path, content_type='csv')

# Start training
estimator.fit(train_input)

# Save the trained model
model = estimator.create_model()
model_name = f"sklearn-model-{int(time.time())}"
model.deploy(instance_type='ml.m5.large', initial_instance_count=1)

print(f"Model deployed: {model_name}")
