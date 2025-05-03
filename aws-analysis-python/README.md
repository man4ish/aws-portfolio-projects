# AWS Rekognition, Comprehend, and Translate Python Integration

This repository demonstrates how to use AWS Rekognition, Comprehend, and Translate APIs in Python.

## Services Covered:
- **AWS Rekognition**: Image analysis, object detection, and facial recognition.
- **AWS Comprehend**: Sentiment analysis, entity recognition, and language detection.
- **AWS Translate**: Language translation between different languages.

## Prerequisites:
- AWS account with the necessary permissions to access Rekognition, Comprehend, and Translate services.
- AWS CLI configured (`aws configure`).
- Python 3.x.

## Installation:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd aws-analysis-python
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage:

Run the following command to execute all the services (Rekognition, Comprehend, and Translate) together:

```bash
python aws_analysis_example.py

```

This script will:

- Analyze an image with AWS Rekognition.

- Perform sentiment analysis and entity recognition with AWS Comprehend.

- Translate a given text into another language using AWS Translate.

## Clean Up:
Remember to delete any AWS resources created to avoid incurring costs.