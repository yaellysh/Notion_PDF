import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def check_file_exists(bucket_name, object_name):
    s3_client = boto3.client('s3')

    try:
        s3_client.head_object(Bucket=bucket_name, Key=object_name)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise

def get_s3_image_links(bucket_name: str, folder_name: str):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    bucket_location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    base_url = f"https://{bucket_name}.s3.{bucket_location}.amazonaws.com"
    image_links = []

    for obj in response.get('Contents', []):
        object_url = f"{base_url}/{obj['Key']}"
        
        if obj['Key'].endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_links.append(object_url)

    return image_links

def upload_image_to_s3(file_name, bucket_name, object_name=None):

    if check_file_exists(bucket_name, object_name):
        return None

    session = boto3.Session()
    s3 = session.client('s3')

    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        return True
    
    except FileNotFoundError:
        print("The specified file was not found.")
        return False
    
    except NoCredentialsError:
        print("Credentials not available.")
        return False
        
    except ClientError as e:
        print(f"Client error occurred: {e}")
        return False
