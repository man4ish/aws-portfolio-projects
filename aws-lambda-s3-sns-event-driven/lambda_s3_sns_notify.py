import json
import boto3
from datetime import datetime

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:S3UploadNotification'  # Replace with your SNS ARN

def lambda_handler(event, context):
    # Extract bucket and object info
    bucket = event['Records'][0]['s3']['bucket']['name']
    file = event['Records'][0]['s3']['object']['key']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message = f"A new file '{file}' was uploaded to bucket '{bucket}' at {time}."

    # Publish to SNS
    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject='New S3 Upload Notification'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent!')
    }

