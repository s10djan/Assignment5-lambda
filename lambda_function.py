import json
import boto3
import requests
from datetime import datetime

# Initialize clients for SNS, DynamoDB, and Slack
sns_client = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']
sns_topic_arn = os.environ['SNS_TOPIC_ARN']
ddb_table_name = os.environ['DDB_TABLE_NAME']

# DynamoDB table
table = dynamodb.Table(ddb_table_name)

def lambda_handler(event, context):
    # Extract the S3 bucket name and the file name from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_file = event['Records'][0]['s3']['object']['key']
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prepare metadata for DynamoDB
    metadata = {
        'fileName': s3_file,
        'uploadTimestamp': timestamp,
        'bucketName': s3_bucket,
    }
    
    # Store metadata in DynamoDB
    table.put_item(Item=metadata)
    
    # Prepare the SNS message
    sns_message = {
        'default': f'File uploaded to S3 bucket {s3_bucket}: {s3_file}',
    }
    
    # Publish to SNS
    sns_client.publish(
        TargetArn=sns_topic_arn,
        Message=json.dumps(sns_message),
        MessageStructure='json'
    )
    
    # Prepare Slack message
    slack_message = {
        'text': f'File uploaded to S3 bucket {s3_bucket}: {s3_file} at {timestamp}'
    }
    
    # Send Slack notification
    response = requests.post(slack_webhook_url, json=slack_message)
    
    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps('File upload processed successfully')
    }
