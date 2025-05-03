import boto3
import time

# Initialize a boto3 client for AWS Batch and S3
batch_client = boto3.client('batch')
s3_client = boto3.client('s3')

# Define S3 Bucket and Paths
s3_bucket_name = 'your-s3-bucket-name'
input_data_key = 'input/data.csv'
output_data_key = 'output/results.csv'

# Define Batch Job Definition and Job Queue
job_definition = 'your-job-definition'
job_queue = 'your-job-queue'

# Function to submit a job to AWS Batch
def submit_batch_job():
    response = batch_client.submit_job(
        jobName='ml-processing-job',  # Job name
        jobQueue=job_queue,           # Job queue to use
        jobDefinition=job_definition,  # Job definition (Docker container or EC2)
        containerOverrides={
            'environment': [
                {
                    'name': 'INPUT_DATA_S3',
                    'value': f's3://{s3_bucket_name}/{input_data_key}'  # Pass input data path
                },
                {
                    'name': 'OUTPUT_DATA_S3',
                    'value': f's3://{s3_bucket_name}/{output_data_key}'  # Pass output data path
                }
            ]
        }
    )
    return response['jobId']

# Function to check job status
def check_job_status(job_id):
    response = batch_client.describe_jobs(
        jobs=[job_id]
    )
    job_status = response['jobs'][0]['status']
    return job_status

# Upload the input data to S3
def upload_input_data():
    with open('data.csv', 'rb') as file:
        s3_client.upload_fileobj(file, s3_bucket_name, input_data_key)
    print(f"Input data uploaded to s3://{s3_bucket_name}/{input_data_key}")

# Download the output data from S3
def download_output_data():
    s3_client.download_file(s3_bucket_name, output_data_key, 'results.csv')
    print(f"Output data downloaded from s3://{s3_bucket_name}/{output_data_key}")

# Main function
def main():
    # Step 1: Upload input data to S3
    upload_input_data()

    # Step 2: Submit Batch Job
    job_id = submit_batch_job()
    print(f"Batch job submitted with Job ID: {job_id}")

    # Step 3: Monitor the job status
    while True:
        job_status = check_job_status(job_id)
        print(f"Job Status: {job_status}")
        if job_status in ['SUCCEEDED', 'FAILED']:
            break
        time.sleep(30)  # Polling every 30 seconds

    # Step 4: Download output data from S3 after job completes
    if job_status == 'SUCCEEDED':
        download_output_data()
    else:
        print("Job failed, please check the logs.")

if __name__ == "__main__":
    main()

