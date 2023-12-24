import boto3
import logging
from botocore.exceptions import ClientError
import os
from celery import shared_task





# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# MEDIA_DIR = Path.joinpath(BASE_DIR, 'videos', 'media')
# file_name = 'Ecowiser.mp4'
# file_name = Path.joinpath(MEDIA_DIR, file_name)




# Upload video to AWS S3 bucket
@shared_task
def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name.
    :return: True if file was uploaded, else False
    """


    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    try:
        response = s3_client.upload_file(file_name, BUCKET, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    print(response)
    return True



def upload_videos(filepath):
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    subtitle_file_name = filepath.name.strip().split('.')[0] + '.txt'
    s3 = session.resource('s3')
    s3.meta.client.upload_file(Filename=filepath, Bucket=BUCKET, key='subtitle_1')
    


@shared_task
# Upload search keywords in AWS dynamoDB
def upload_search_keywords(search_keyword):

        
    
    # Implement from the stackoverflow answer.
    pass
