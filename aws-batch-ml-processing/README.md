# AWS Batch ML Processing with Python

This repository demonstrates how to use **AWS Batch** for running large-scale batch jobs, such as data processing tasks or machine learning model training, in parallel.

## Services Covered:
- **AWS Batch**: A fully managed batch processing service that allows you to run batch computing workloads on the AWS Cloud.
- **Amazon S3**: Used for storing input data and output results.
- **AWS SDK for Python (Boto3)**: Python library to interact with AWS services, including AWS Batch.

## Prerequisites:
- **AWS account** with necessary permissions to access AWS Batch, S3, and other services.
- **AWS CLI** configured (`aws configure`).
- **Python 3.x** installed.
- **Boto3** and **AWS SDK** for Python installed.
  You can install them using the following:

```bash
  pip install boto3
```

An S3 bucket to store input data and output results.

## Installation:
Clone the repository:

```bash
git clone <repository_url>
cd aws-batch-ml-processing
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage:
- 1. Configure AWS Batch:
Before using the script, ensure that your AWS Batch environment is set up. This includes creating a compute environment, job queues, and job definitions. For a step-by-step guide on setting up AWS Batch, refer to the AWS Batch User Guide.

- 2. Prepare the Input Data:
Upload your input data to an S3 bucket. This data will be used for processing in the batch job.

- 3. Run the Python Script:
The provided Python script will submit a batch job that runs parallel ML processing on multiple compute resources using AWS Batch.

```bash
python aws_batch_ml_processing.py
```
- 4. Monitor Job Status:
You can monitor the status of the jobs through the AWS Batch Console or by using the AWS CLI:

```bash
aws batch describe-jobs --jobs <job_id>
```

## Expected Output:
- The input data is retrieved from an S3 bucket.

- The batch jobs are submitted and executed in parallel.

- After processing, the results will be uploaded back to the specified S3 bucket.

## Clean Up:
- Delete any AWS Batch jobs that are no longer needed to avoid unnecessary costs.

- You can delete the S3 bucket (if not required) to avoid ongoing storage costs.