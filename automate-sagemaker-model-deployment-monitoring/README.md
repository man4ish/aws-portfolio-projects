# Automate SageMaker Model Deployment and Monitoring

This repository contains Python scripts to automate the deployment and monitoring of machine learning models on AWS SageMaker.

## Overview

1. **train_model.py**: Trains a machine learning model using Amazon SageMaker, uploads the dataset to S3, and saves the trained model.
2. **inference.py**: Uses a deployed SageMaker endpoint to make predictions.
3. **monitor_model.py**: Monitors model performance over time, tracking accuracy and identifying any potential model drift.

## Prerequisites

### AWS Configuration:
Ensure your AWS credentials are set up. You can do this by configuring the AWS CLI:

```bash
aws configure
```

## S3 Bucket:
Make sure you have an S3 bucket in your AWS account to upload datasets and store model artifacts.

### Usage
Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

## Configure the S3 Bucket and Scripts:

- Open the train_model.py file.

- Replace your-s3-bucket-name with your actual S3 bucket name.

## Run the Scripts:
- Train the Model:

```bash
python train_model.py
```

This will upload the Iris dataset to S3, initiate a SageMaker training job, and deploy the trained model.

## Make Predictions:

```bash
python inference.py
```

This script will make predictions using the deployed model.

## Monitor Model Performance:

```bash
python monitor_model.py
```
This will monitor the performance of the deployed model over time.

## Expected Output
- The model is trained, deployed, and can make predictions.

- The model performance over time is tracked and plotted.

- Any drift or changes in accuracy are visualized in a plot saved as model_accuracy_plot.png.

## Clean Up
The scripts will automatically delete SageMaker endpoints and other resources after use to prevent unnecessary costs.