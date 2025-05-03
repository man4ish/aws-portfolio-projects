import boto3
import time
import os

# Initialize the AWS clients
s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

# Parameters
bucket_name = 'my-unique-bucket-name'  # Make sure this is unique
file_path = 'path/to/your/local/file.txt'  # Local file to upload
file_name = 'file.txt'  # S3 file name
processed_file_name = 'processed_file.txt'
download_path = '/home/ec2-user/file.txt'  # Path to download file on EC2
processed_file_path = '/home/ec2-user/processed_file.txt'  # Path to save processed file on EC2

# Step 1: Create an S3 Bucket (if it doesn't exist)
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-1'
        }
    )
    print(f"Bucket {bucket_name} created successfully.")
except s3.exceptions.Boto3Error:
    print(f"Bucket {bucket_name} already exists.")

# Step 2: Upload a Local File to S3
s3.upload_file(file_path, bucket_name, file_name)
print(f"File {file_path} uploaded to S3 bucket {bucket_name} as {file_name}.")

# Step 3: Launch EC2 Instance with IAM role (make sure IAM role is configured for S3 access)
response = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2 AMI
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='my-key-pair',  # Replace with your key pair name
    SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group ID
    SubnetId='subnet-xxxxxxxx',  # Replace with your subnet ID
    IamInstanceProfile={'Name': 'EC2S3AccessRole'},  # Ensure IAM role allows EC2 to access S3
)

instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance {instance_id} launched successfully.")

# Wait for EC2 instance to be running
print("Waiting for EC2 instance to be running...")
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])
print(f"EC2 instance {instance_id} is running.")

# Step 4: EC2 Instance will Download the File from S3 and Process It
# EC2 instance script to download from S3 and process the file
ec2_script = f"""
#!/bin/bash
aws s3 cp s3://{bucket_name}/{file_name} {download_path}
echo "File downloaded to {download_path}"

# Process the file (convert text to uppercase)
cat {download_path} | tr '[:lower:]' '[:upper:]' > {processed_file_path}
echo "File processed and saved to {processed_file_path}"

# Upload the processed file back to S3
aws s3 cp {processed_file_path} s3://{bucket_name}/{processed_file_name}
echo "Processed file uploaded back to S3 as {processed_file_name}"
"""

# Step 5: Use EC2 Instance to Run the Script (via SSH or SSM)
# In a real scenario, you'd SSH into the instance or use SSM to run the script, but for simplicity, we're assuming the EC2 instance will automatically process when it starts.
# For simplicity, we will use EC2's UserData to run the script (this is an assumption in this case)

# Step 6: Wait for EC2 instance to process and save output to S3
time.sleep(120)  # Sleep for 2 minutes to ensure EC2 has time to process the file

# Step 7: Check if processed file is in S3
print(f"Checking if processed file is available in S3 bucket {bucket_name}...")
processed_file = s3.get_object(Bucket=bucket_name, Key=processed_file_name)
print(f"Processed file {processed_file_name} is available in S3.")

# Step 8: Cleanup - Terminate EC2 Instance
ec2.terminate_instances(InstanceIds=[instance_id])
print(f"EC2 instance {instance_id} terminated.")

