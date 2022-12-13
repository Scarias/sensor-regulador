import boto3
import json
from botocore.exceptions import ClientError


def get_credentials(region):

    secret_name = "lumensense/dynamodb"
    region_name = region

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    creds = json.loads(secret)

    return creds

def get_sqs():

    region_name = 'sa-east-1'
    creds = get_credentials(region_name)

    sqs = boto3.client(
        'sqs',
        aws_access_key_id=creds['access_id'],
        aws_secret_access_key=creds['access_secret_key'],
        region_name=region_name
    )

    return sqs


def get_message(sqs, queue_url):

    response = sqs.recieve_message(
        QueueUrl=queue_url,
        AttributeNames=[],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )

    print(f'Message: {message}')
    return message