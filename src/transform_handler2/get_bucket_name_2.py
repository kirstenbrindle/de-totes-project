import re


def get_bucket_name_2(s3):
    """
    This function takes an s3 connection
    and returns processed bucket name.

    Args:
        `s3`: s3 client connection
    ---------------------------

    Returns:
        String of processed bucket name.

    Errors:
        Raises ValueError if no bucket name.
    """
    response = s3.list_buckets()
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
    matching_string = ''

    for bucket in bucket_list:
        match = re.search('processed', bucket)

        if match:
            matching_string = match.string
        else:
            continue
    if matching_string == '':
        raise ValueError
    else:
        return matching_string
