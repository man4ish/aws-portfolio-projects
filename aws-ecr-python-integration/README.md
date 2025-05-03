# AWS ECR Python Integration

This repository demonstrates how to use **AWS Elastic Container Registry (ECR)** with **Docker** and **Python** to:

1. Build and push Docker images to ECR.
2. Pull Docker images from ECR.
3. Run Docker containers locally or on EC2.

## Prerequisites

- AWS Account with ECR permissions.
- AWS CLI configured (`aws configure`).
- Docker installed.
- Python 3.x.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd aws-ecr-python-integration
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Build and Push Docker Image to ECR

Run the following command to authenticate Docker to ECR, build the image, tag it, and push it to your ECR repository:

```bash
python ecr_push_pull.py
```

## Pull Docker Image from ECR
Once the image is pushed to ECR, you can pull it with:

```bash
docker pull <aws_account_id>.dkr.ecr.us-west-2.amazonaws.com/my-python-app:latest
```

### Run Docker Image Locally
Run the image locally using the following command:

```bash
docker run -p 5000:5000 <aws_account_id>.dkr.ecr.us-west-2.amazonaws.com/my-python-app:latest
```

### Clean Up
Ensure that you delete any Docker containers or resources created to avoid incurring costs.

## AWS ECR Repository
- Repository Name: my-python-app

- Region: us-west-2