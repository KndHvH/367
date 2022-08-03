import boto3


client = boto3.client(
    service_name='s3',
    aws_access_key_id='seu_access_key_id',
    aws_secret_access_key='seu_secret_access_key',
    region_name='sa-east-1' # voce pode usar qualquer regiao
)