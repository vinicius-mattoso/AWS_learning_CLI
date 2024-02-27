# import libs
import boto3
import os


def download_files(bucket_name, all_files=True):
    if all_files:
        # Initialize the S3 client
        s3_client = boto3.client('s3')
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket(bucket_name)
        files_list = list(bucket.objects.all())

        # Path for the storage folder
        storage_path = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(storage_path, exist_ok=True)

        for file in files_list:
            filename = os.path.join(storage_path, file.key)
            s3_client.download_file(bucket_name, file.key, filename)
    else:
        raise ValueError('Something wrong with the bucket: {}'.format(bucket_name))

bucket = 'bucketcriadopelopyparavercustos123'
download_files(bucket)
