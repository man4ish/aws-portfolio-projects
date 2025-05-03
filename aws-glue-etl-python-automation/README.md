# AWS Glue ETL Python Automation

This repository demonstrates how to use AWS Glue to automate ETL (Extract, Transform, Load) tasks using Python scripts. The workflow involves extracting data from Amazon S3, transforming it, and loading it into Amazon Redshift.

## Project Structure:

- **`glue_etl_script.py`**: Python script that defines the ETL logic for extracting, transforming, and loading data using AWS Glue.
- **`create_glue_job.py`**: Python script that creates and manages AWS Glue jobs. It includes the logic to start and monitor the ETL job.
- **`requirements.txt`**: File that contains all the necessary Python dependencies.
- **`.gitignore`**: Git ignore file to ensure that unnecessary files are not committed.

## Prerequisites:
- AWS account with necessary permissions for AWS Glue, S3, and Redshift.
- AWS CLI configured (`aws configure`).
- Python 3.x installed along with the `boto3` package (`pip install boto3`).

## Setup:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aws-glue-etl-python-automation.git
    cd aws-glue-etl-python-automation
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your AWS Glue environment by creating a Glue crawler and database. Follow AWS Glue documentation for detailed steps on setting up crawlers.

4. **Create Glue ETL Job**: 
   Use the `create_glue_job.py` script to create an AWS Glue job that will execute the ETL script. The script requires the following arguments:
   - **JOB_NAME**: Name of the Glue job.
   - **ROLE**: IAM role with permissions for AWS Glue.

    Example:
    ```bash
    python create_glue_job.py
    ```

5. **Run the Glue Job**:
   Once the job is created, start the ETL process by running the job and monitor its progress.

    Example:
    ```bash
    python create_glue_job.py
    ```

## Notes:
- **glue_etl_script.py** contains the logic for extracting data from Amazon S3, performing transformations, and loading the result into Amazon Redshift.
- This solution uses **AWS Glue** with **Python** for serverless ETL automation.

## Dependencies:
- `boto3`
- `aws-glue` (for Glue job management)
- `pyspark` (for handling transformation tasks)

