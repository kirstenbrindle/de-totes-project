import boto3


def bucket_maker():
    s3 = boto3.client("s3")
    bucket_name = input("Enter bucket name: ")
    # bucket_name = 'bit_me_tf_state'
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
    print(f"Bucket '{bucket_name}' created.")

bucket_maker()