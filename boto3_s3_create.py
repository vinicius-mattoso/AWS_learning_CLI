# Import libs
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Name of the bucket you want to create
bucket_name = 'bucketcriadopelopyparavercustos123'

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name)