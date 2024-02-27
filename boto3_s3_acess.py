# Load the lib
import boto3

# Making the connection
s3 = boto3.resource('s3')

# Get the list of buckets
buckets = list(s3.buckets.all())

# Check if the list is empty
if not buckets:
    print("No buckets found.")
else:
    # Loop through the buckets and print their names
    for bucket in buckets:
        print(bucket.name)

