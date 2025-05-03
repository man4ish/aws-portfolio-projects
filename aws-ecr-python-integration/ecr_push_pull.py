import subprocess
import boto3

# Define AWS ECR repository and region
ecr_repository = "my-python-app"
region = "us-west-2"
aws_account_id = "<aws_account_id>"

# Authenticate Docker to AWS ECR
def authenticate_ecr():
    login_command = f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {aws_account_id}.dkr.ecr.{region}.amazonaws.com"
    subprocess.run(login_command, shell=True, check=True)
    print(f"Successfully authenticated Docker to ECR")

# Build Docker image
def build_docker_image():
    build_command = "docker build -t my-python-app ."
    subprocess.run(build_command, shell=True, check=True)
    print("Docker image built successfully")

# Tag Docker image
def tag_docker_image():
    tag_command = f"docker tag my-python-app:latest {aws_account_id}.dkr.ecr.{region}.amazonaws.com/{ecr_repository}:latest"
    subprocess.run(tag_command, shell=True, check=True)
    print(f"Docker image tagged successfully for ECR repository {ecr_repository}")

# Push Docker image to ECR
def push_docker_image():
    push_command = f"docker push {aws_account_id}.dkr.ecr.{region}.amazonaws.com/{ecr_repository}:latest"
    subprocess.run(push_command, shell=True, check=True)
    print(f"Docker image pushed to ECR repository {ecr_repository}")

# Pull Docker image from ECR
def pull_docker_image():
    pull_command = f"docker pull {aws_account_id}.dkr.ecr.{region}.amazonaws.com/{ecr_repository}:latest"
    subprocess.run(pull_command, shell=True, check=True)
    print(f"Docker image pulled from ECR repository {ecr_repository}")

if __name__ == "__main__":
    authenticate_ecr()
    build_docker_image()
    tag_docker_image()
    push_docker_image()
    pull_docker_image()
