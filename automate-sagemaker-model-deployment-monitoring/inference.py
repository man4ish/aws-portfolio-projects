"""
inference.py
------------

This script makes predictions using a deployed model on Amazon SageMaker.
It sends requests to the deployed endpoint and prints the predicted results.
"""

import boto3
import json

# Initialize the SageMaker runtime
runtime_client = boto3.client('runtime.sagemaker')

# Define endpoint name (Replace with your actual endpoint name)
endpoint_name = "sklearn-model-123456"

# Sample input data for prediction
sample_input = [[5.1, 3.5, 1.4, 0.2]]

# Get predictions from SageMaker endpoint
response = runtime_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',
    Body=json.dumps(sample_input)
)

# Parse and print prediction
result = json.loads(response['Body'].read().decode())
print("Predicted class:", result)
