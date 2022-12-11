import boto3
from botocore.exceptions import ClientError
import json

#"CREATE"
def CreateTable(client, excepts):
    try:
        table = client.create_table(
            TableName='DistanciaFocos',
            KeySchema=[
                {
                    'AttributeName': 'ID_Focos',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'ID_Focos',
                    'AttributeType': 'S'
                }

            ]
        )
        waiter = client.get_waiter('table_exists')
        waiter.wait(TableName='DistanciaFocos')
        print("Table created.")

    except excepts.ResourceInUseException:
        print("Table exists.")


#"READ"
def ScanTable(dynamodb):
    response = dynamodb.Table('DistanciaFocos').scan()
    #for i in response['Items']:
    #    print(i)
    return response

#"UPDATE"
def PutItem(dynamodb, IDs, distancia):
    dynamodb.Table('DistanciaFocos').put_item(
        Item={
            'ID_Focos': IDs,
            'distancia': distancia
        }
    )

#"DELETE" (table)
def DeleteTable(client, name):
    print("Deleting Table")
    client.delete_table(TableName=name)
    waiter = client.get_waiter('table_not_exists')
    waiter.wait(TableName=name)
    print("Table deleted")


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



if __name__ == '__main__':

    region_name = 'sa-east-1'

    db_creds = get_credentials(region_name)

    dynamoclient = boto3.client(
        'dynamodb',
        aws_access_key_id=db_creds['access_id'],
        aws_secret_access_key=db_creds['access_secret_key'],
        region_name=region_name,
    )
    ddb_excepts = dynamoclient.clientexceptions

    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=db_creds['access_id'],
        aws_secret_access_key=db_creds['access_secret_key'],
        region_name=region_name,
    )
