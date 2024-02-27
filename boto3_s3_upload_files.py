# import libs
import boto3
from botocore.exceptions import ClientError
import logging
import os
import sys
import threading

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


# Initialize the S3 client
s3 = boto3.client('s3')

# Creating a function
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, Callback=ProgressPercentage(file_name))
        print('Upload complete')
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucket = 'bucketcriadopelopyparavercustos123'
# Carregando um arquivo .zip
# upload_file(file_name='data\zip_test.rar', bucket= bucket)

# Carregando um arquivo .txt
# upload_file(file_name=r'D:\Users\vmattoso\Documents\repositorios\AWSCLI\data\teste.txt', bucket= bucket)

# Carregando um arquivo .csv
upload_file(file_name=r'D:\Users\vmattoso\Documents\repositorios\AWSCLI\data\book.csv', bucket= bucket)

# Carregando um arquivo .zip
# upload_file(file_name='data\zip_test.zip', bucket= bucket)

# Carregando um arquivo .jpg
# upload_file(file_name='data\ICA_logo.jpg', bucket= bucket)