import boto3

# Hard-coded AWS credentials
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'your_region'

# Create a Boto3 client using the hard-coded credentials and region
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Now you can use the s3_client to interact with S3
# For example, list buckets
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])