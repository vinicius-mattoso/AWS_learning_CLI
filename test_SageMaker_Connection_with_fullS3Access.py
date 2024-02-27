# Import Libs
import time


import sagemaker
import boto3

import pandas as pd
from sklearn.model_selection import train_test_split

sagemaker_client = boto3.client('sagemaker')
session = sagemaker.Session()
region = session.boto_session.region_name
bucket = 'bucketcriadopelopyparavercustos123'

print(f'''Vamos utilizar o bucket :{bucket}\n
A regiao que estamos utilizando é: {region}''')

df = pd.read_csv("mob_price_classification_train.csv")
print(df.head())

features = list(df.columns)
label = features.pop(-1)

x = df[features]
y = df[label]

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.15, random_state=0)


trainX = pd.DataFrame(X_train)
trainX[label] = y_train

testX = pd.DataFrame(X_test)
testX[label] = y_test

trainX.to_csv("train-V-1.csv",index = False)
testX.to_csv("test-V-1.csv", index = False)

# Record the start time
start_time = time.time()
# send data to S3. SageMaker will take training data from s3
sk_prefix = "sagemaker/house_data/sklearncontainer"
trainpath = session.upload_data(
    path="train-V-1.csv", bucket=bucket, key_prefix=sk_prefix
)

testpath = session.upload_data(
    path="test-V-1.csv", bucket=bucket, key_prefix=sk_prefix
)

from sagemaker.sklearn.estimator import SKLearn

FRAMEWORK_VERSION = "0.23-1"

sklearn_estimator = SKLearn(
    entry_point="script.py",
    role='arn:aws:iam::730335578970:role/SagemakerRole',#get_execution_role(),
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version=FRAMEWORK_VERSION,
    base_job_name="RF-custom-sklearn",
    hyperparameters={
        "n_estimators": 100,
        "random_state": 0,
    },
    use_spot_instances = True,
    max_wait = 7200,
    max_run = 3600
)


# launch training job, with asynchronous call
sklearn_estimator.fit({"train": trainpath, "test": testpath}, wait=True)
# sklearn_estimator.fit({"train": datapath}, wait=True)
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

import joblib

# Save the trained model to a file
joblib.dump(sklearn_estimator, 'sklearn_estimator_v1.joblib')
