# Assignment 5 – AWS Lambda Integration with S3 and DynamoDB

## 📌 Project Description

This project demonstrates an AWS Lambda function that is triggered whenever a new object is uploaded to a specified Amazon S3 bucket. Once triggered, the Lambda function performs a simple operation and logs relevant metadata to a DynamoDB table.

---

## 🧱 Architecture Overview

- **S3 Bucket (Trigger Source):** Triggers the Lambda function on `ObjectCreated` events.
- **Lambda Function (Processor):** Processes S3 event data and interacts with DynamoDB.
- **DynamoDB Table (Storage):** Stores file metadata or related logs from S3 uploads.

### 💡 Flow Summary:

1. File is uploaded to S3.
2. S3 sends an event to Lambda.
3. Lambda processes the event and logs the data to DynamoDB.

---

## 📂 Files Included

- `lambda_function.py`: Contains the Lambda function code.
- `README.md`: Describes the project setup and architecture.
- `screenshots/`: (Optional) Add screenshots here showing:
  - S3 trigger setup
  - Lambda configuration
  - DynamoDB table
  - Successful test/invocation result

---

## 🛠️ How to Use

1. Clone the repo:
   ```bash
   git clone git@github.com:s10djan/Assignment5-lambda.git
   cd Assignment5-lambda
