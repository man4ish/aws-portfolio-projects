# AWS Lambda – S3 Trigger with SNS Notification

This project demonstrates an **event-driven serverless application** using **AWS Lambda**, **S3**, and **SNS**. The Lambda function is automatically triggered when a new file is uploaded to a specified S3 bucket. Upon triggering, it sends a notification email via Amazon SNS.

## 🧰 Technologies Used

- AWS Lambda
- Amazon S3
- Amazon SNS
- Python 3.x
- Boto3 (AWS SDK for Python)

## 📂 File Structure

- `lambda_s3_sns_notify.py` – Main Lambda handler that reacts to S3 events and sends SNS messages.

## ⚙️ How it Works

1. A file is uploaded to the specified S3 bucket.
2. The event triggers the Lambda function.
3. Lambda reads the event metadata and publishes a message to the SNS topic.
4. SNS sends an email (or SMS, etc.) to the subscribed user.

## 🛠️ Setup Instructions

1. **Create an SNS topic** and subscribe your email.
2. **Create an S3 bucket** for uploads.
3. **Deploy the Lambda function:**
   - Go to AWS Lambda console.
   - Create a new function (Author from scratch).
   - Add the Python code from `lambda_s3_sns_notify.py`.
   - Set the environment variable `SNS_TOPIC_ARN` to your topic ARN.
   - Create an S3 trigger in the Lambda config.

4. **Test It:**
   - Upload a file to your S3 bucket.
   - You should receive an email notification.

## 💡 Example Output (Email Content)


