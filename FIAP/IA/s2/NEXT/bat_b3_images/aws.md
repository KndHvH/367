

cafe:Macarone1!%



b3: albumknd

ident group: kndhvh

policies: albumcafe

aws cred:
```javascript
// Inicializar o provedor de credenciais do Amazon Cognito
AWS.config.region = 'sa-east-1'; // Região
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'sa-east-1:45f72d07-c362-49c2-976b-7204d3f4acd6',
});
```
```json
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Effect": "Allow",
         "Action": [
            "s3:ListBucket"
         ],
         "Resource": [
            "arn:aws:s3:::albumknd"
         ]
      }
   ]
}
```


Cognito_kndhvhAuth_Role
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "mobileanalytics:PutEvents",
        "cognito-sync:*",
        "cognito-identity:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

Cognito_kndhvhUnauth_Role
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "mobileanalytics:PutEvents",
        "cognito-sync:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
```
CORS
```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "HEAD",
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ]
    }
]
```
ss
```x
var albumBucketName = 'albumknd';

AWS.config.region = 'sa-east-1';
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'sa-east-1:45f72d07-c362-49c2-976b-7204d3f4acd6',
});

var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {Bucket: albumknd}
});
function getHtml(template) {
  return template.join('\n');
}

```
User name,Password,Access key ID,Secret access key,Console login link
cafe,,AKIA3K6TTNCMGZUVBPRR,XHCJO31J80X7GCYihsO5zoedUm8TvH78C+ZkzHmx,https://kndhvh.signin.aws.amazon.com/console

FONTE: https://butecotecnologico.com.br/python-aws-s3/

FONTE: https://docs.aws.amazon.com/pt_br/sdk-for-javascript/v2/developer-guide/s3-example-photos-view.html