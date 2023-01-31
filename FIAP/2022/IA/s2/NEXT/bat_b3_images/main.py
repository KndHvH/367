import boto3
from dotenv import dotenv_values

ENV_DATA = dotenv_values(".env")


client = boto3.client(
    service_name='s3',
    aws_access_key_id=ENV_DATA["AWS_KEY_ID" ],
    aws_secret_access_key=ENV_DATA["AWS_ACCESS_KEY"],
    region_name='sa-east-1' # voce pode usar qualquer regiao

)
time = funcaosxa
client.upload_file("foto.jpg", "albumknd", icaro+time)