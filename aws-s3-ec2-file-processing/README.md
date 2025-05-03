# AWS S3 and EC2 File Processing Workflow

This repository demonstrates a complete workflow using AWS services to upload a file to S3, process it on an EC2 instance, and save the output back to S3.

## Services Covered:
- **AWS S3**: Store the input file and processed output file.
- **AWS EC2**: Process the file using a script running on an EC2 instance.
  
## Workflow:
1. **Create an S3 Bucket**: The script creates an S3 bucket (if it doesn't already exist).
2. **Upload a File from Local Computer to S3**: Upload a local file to the newly created S3 bucket.
3. **Launch an EC2 Instance**: An EC2 instance is launched with an IAM role allowing it to access the S3 bucket.
4. **EC2 Downloads the File from S3**: The EC2 instance downloads the file from S3, processes it, and saves the processed file.
5. **Upload Processed File Back to S3**: After processing, the output is uploaded back to S3.
6. **Terminate EC2 Instance**: After the task is completed, the EC2 instance is terminated to avoid further charges.

## Prerequisites:
- **AWS Account**: You need an AWS account to use S3 and EC2 services.
- **AWS CLI Configured**: Ensure your AWS credentials are set up by running `aws configure` in your terminal.
- **IAM Role**: The EC2 instance needs an IAM role with permission to access the S3 bucket.
- **Python 3.x**: Python must be installed on your local machine.

## Installation:
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd aws-s3-ec2-file-processing
    ```

2. Install dependencies:
    ```bash
    pip install boto3
    ```

## Usage:
### Set up the necessary variables:
- Replace `bucket_name` with a unique name for your S3 bucket.
- Set the path to your local file (`file_path`) and the S3 file name (`file_name`).

### Run the script:
```bash
python aws_s3_ec2_file_processing.py
```

## Expected Output:
- The file will be uploaded to S3.

- EC2 instance will download the file, process it, and save the processed file back to S3.

- The processed file will be stored in S3 as processed_file.txt.

- EC2 instance will be terminated automatically after the process completes.

## Clean Up:
- The EC2 instance will be automatically terminated after processing the file to avoid unnecessary charges.

- Ensure that the S3 bucket and its contents are managed as per your needs.

## IAM Role Setup:
Make sure the EC2 instance has the appropriate IAM role that grants access to S3. You can create a custom IAM role with AmazonS3ReadOnlyAccess and AmazonS3FullAccess permissions.

## Notes:
- The script assumes that the EC2 instance uses an Amazon Linux 2 AMI and is set up with an appropriate security group and key pair for SSH access.

