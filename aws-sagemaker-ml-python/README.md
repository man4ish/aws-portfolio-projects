# Train ML Model on AWS SageMaker using Python

This repository contains an example of how to train a machine learning model using AWS SageMaker and Python. Specifically, it demonstrates how to train a Random Forest model on the Iris dataset using AWS SageMaker's built-in support for scikit-learn. The model is then deployed as a SageMaker endpoint for inference.

## Overview

The script `train_ml_model_sagemaker.py` performs the following steps:

1. Loads the Iris dataset from `sklearn.datasets`.
2. Uploads the dataset to an S3 bucket for SageMaker to access.
3. Creates a SageMaker training job using a scikit-learn container.
4. Deploys the trained model to a SageMaker endpoint.
5. Makes predictions using the deployed model.
6. Deletes the deployed endpoint to clean up resources.

### Requirements

- **AWS Account**: You must have an AWS account with SageMaker and S3 permissions.
- **Python Libraries**:
  - `boto3` – AWS SDK for Python
  - `sagemaker` – AWS SageMaker SDK for Python
  - `pandas` – Data manipulation library
  - `numpy` – Library for numerical operations
  - `scikit-learn` – Machine learning library for Python
  - `joblib` – Python library for saving machine learning models

You can install the required Python libraries using the following command:

```bash
pip install sagemaker boto3 pandas scikit-learn joblib
```

## Prerequisites
AWS Configuration: Ensure your AWS credentials are set up. You can do this by configuring the AWS CLI:

```bash
aws configure
```

## S3 Bucket: Make sure you have an S3 bucket in your AWS account where you can upload the dataset and store model artifacts.

Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

- Configure the S3 Bucket and Script:

- Open the train_ml_model_sagemaker.py file.

- Replace your_s3_bucket_name with your actual S3 bucket name.

## Run the script:

```bash
python train_ml_model_sagemaker.py
```

## Expected Output:

- The script will upload the Iris dataset to S3.

- It will initiate a SageMaker training job and train the model using a scikit-learn container.

- After training, the model will be deployed as a SageMaker endpoint for inference.

- Predictions will be made using the trained model, and the trained model will be saved in the specified S3 location.

- The deployed SageMaker endpoint will be deleted after inference.

## Evaluation
Once the script has finished running, it will print the accuracy of the model on the test data.

## Clean Up
The script will automatically delete the SageMaker endpoint after inference to ensure resources are not left running and incurring costs.
