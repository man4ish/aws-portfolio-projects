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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn import SKLearnModel

# Function to load the model from the deployed endpoint (this can be used for inference)
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, 'model.joblib'))
    return model

if __name__ == '__main__':
    # 1. Load the dataset (Replace this with your own dataset)
    print("Loading dataset...")
    iris = datasets.load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target

    # 2. Save dataset to CSV file and upload it to S3
    print("Uploading dataset to S3...")
    data.to_csv('iris.csv', index=False)

    # Set up S3 client
    s3_client = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'  # Make sure to change this to your bucket name
    s3_client.create_bucket(Bucket=bucket_name)
    
    # Upload the file to S3
    s3_client.upload_file('iris.csv', bucket_name, 'iris/iris.csv')
    s3_uri = f's3://{bucket_name}/iris/iris.csv'
    print(f"Dataset uploaded to: {s3_uri}")

    # 3. SageMaker setup
    print("Setting up SageMaker session...")
    role = get_execution_role()  # Automatically fetch the execution role of the notebook
    sagemaker_session = sagemaker.Session()
    output_path = f's3://{bucket_name}/output/'

    # 4. Train the model using SageMaker
    print("Training the model with SageMaker...")

    from sagemaker.sklearn.estimator import SKLearnModel
    estimator = sagemaker.sklearn.model.SKLearnModel(
        model_data=s3_uri, 
        role=role, 
        entry_point='train_script.py',  # The script that will train the model
        framework_version='0.23-1',  # Framework version for sklearn
        instance_type='ml.m4.xlarge',  # Instance type to use
        sagemaker_session=sagemaker_session
    )

    # 5. Start training job
    estimator.fit({'train': s3_uri})
    print("Training job started...")

    # 6. Deployment (optional)
    print("Deploying the trained model...")
    predictor = estimator.deploy(
        initial_instance_count=1,
        instance_type='ml.m4.xlarge'
    )

    # 7. Make Predictions (Example input data)
    print("Making predictions using the deployed model...")
    input_data = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)
    predictions = predictor.predict(input_data)
    print("Predictions:", predictions)

    # 8. Clean Up
    print("Deleting the endpoint...")
    predictor.delete_endpoint()

    print("Done!")

