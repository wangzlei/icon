import os
import boto3

s3 = boto3.resource("s3")
for bucket in s3.buckets.all():
    if bucket.name.startswith('lambda-artifacts'):
        print(bucket.name + "deleting")
        os.system("aws s3 rb --force s3://" + bucket.name)
