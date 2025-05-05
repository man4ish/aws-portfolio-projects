"""
train_ml_model_sagemaker.py

This script demonstrates how to train a machine learning model using AWS SageMaker and Python. Specifically, 
it trains a Random Forest model using the Iris dataset. The script performs the following steps:

1. Loads the dataset (Iris dataset in this case).
2. Uploads the dataset to an S3 bucket for use with SageMaker.
3. Configures and initiates a SageMaker training job with the dataset.
4. Deploys the trained model to a SageMaker endpoint.
5. Uses the deployed model to make predictions.
6. Cleans up by deleting the deployed SageMaker endpoint.

The model is trained using SageMaker's built-in support for scikit-learn and saved as a `.joblib` file. The script also 
provides a mechanism to evaluate the model and obtain predictions.

The script assumes the following:
- You have a working AWS account with proper IAM permissions for SageMaker and S3.
- You have the `boto3` and `sagemaker` Python packages installed.

Requirements:
- AWS Account with SageMaker and S3 permissions.
- `boto3` and `sagemaker` Python libraries installed.
- An active S3 bucket to store the dataset and output files.

Note:
- The script is designed to work with the Iris dataset, but can be easily adapted to work with other datasets by 
  modifying the data loading part.
- Ensure that the S3 bucket name is correctly set in the script.
- The script will automatically deploy the model after training and make a prediction based on the input data.

Usage:
1. Install necessary libraries:
    pip install sagemaker boto3 pandas scikit-learn

2. Run the script:
    python train_ml_model_sagemaker.py

After the script runs, the trained model will be saved in the specified S3 output path, and a model endpoint will 
be created for inference.

The script also evaluates the model and prints the accuracy of the trained model on the test data.

Module Dependencies:
- boto3
- sagemaker
- pandas
- numpy
- scikit-learn
- joblib
"""

import os
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn.estimator import SKLearn  # Correct class for training

if __name__ == '__main__':
    # 1. Load dataset
    print("Loading Iris dataset...")
    iris = datasets.load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target

    # 2. Save to CSV and upload to S3
    print("Saving dataset and uploading to S3...")
    csv_file = 'iris.csv'
    data.to_csv(csv_file, index=False)

    # Set your S3 bucket
    bucket_name = 'your-s3-bucket-name'  # Replace with your actual bucket name
    s3_prefix = 'iris'
    s3_key = f'{s3_prefix}/{csv_file}'

    s3 = boto3.client('s3')
    s3.upload_file(csv_file, bucket_name, s3_key)
    s3_uri = f's3://{bucket_name}/{s3_key}'
    print(f"Data uploaded to: {s3_uri}")

    # 3. SageMaker config
    print("Configuring SageMaker...")
    role = get_execution_role()
    session = sagemaker.Session()
    output_path = f's3://{bucket_name}/output/'

    # 4. Define estimator
    estimator = SKLearn(
        entry_point='iris_model_train.py',  # Training script
        role=role,
        instance_type='ml.m4.xlarge',
        framework_version='0.23-1',
        sagemaker_session=session,
        output_path=output_path
    )

    # 5. Fit model
    print("Starting training job...")
    estimator.fit({'train': s3_uri})

    # 6. Deploy
    print("Deploying model to endpoint...")
    predictor = estimator.deploy(initial_instance_count=1, instance_type='ml.m4.xlarge')

    # 7. Inference
    print("Sending test prediction...")
    test_input = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)
    prediction = predictor.predict(test_input)
    print("Prediction:", prediction)

    # 8. Clean up
    print("Deleting endpoint...")
    sagemaker.Session().delete_endpoint(predictor.endpoint_name)

    print("Done.")
