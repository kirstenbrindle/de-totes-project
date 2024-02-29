import boto3


def bucket_maker():
    """
    When run, this function prompts the user for a bucket name
    and creates an s3 bucket with that name.
    """
    s3 = boto3.client("s3")
    bucket_name = input("Enter bucket name: ")
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
                     'LocationConstraint': 'eu-west-2'})
    print(f"Bucket '{bucket_name}' created.")
