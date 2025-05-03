import boto3

# Initialize the Glue client
client = boto3.client('glue', region_name='us-east-1')

# Set the parameters for your job
job_name = 'ETL-Job-Example'
script_location = 's3://my-glue-scripts/etl_script.py'  # Replace with the actual S3 path
role = 'AWSGlueServiceRole'  # Your IAM role for AWS Glue

# Define the ETL Job (e.g., transforming CSV data in S3 and loading it into Redshift)
def create_glue_job():
    response = client.create_job(
        Name=job_name,
        Role=role,
        Command={
            'Name': 'glueetl',
            'ScriptLocation': script_location,  # Location of the script in S3
            'PythonVersion': '3'
        },
        MaxCapacity=10,  # You can adjust this depending on the scale
        Timeout=2880  # Timeout after 48 hours
    )
    print(f"Created Glue Job: {response['Name']}")

# Start the Glue job
def start_glue_job():
    response = client.start_job_run(JobName=job_name)
    print(f"Started Glue Job Run: {response['JobRunId']}")

if __name__ == "__main__":
    create_glue_job()  # Create the Glue Job
    start_glue_job()   # Start the Glue Job
