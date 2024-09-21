import boto3

s3 = boto3.client('s3')

def get_s3_image_links(bucket_name: str, folder_name: str):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    bucket_location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    base_url = f"https://{bucket_name}.s3.{bucket_location}.amazonaws.com"
    image_links = []

    for obj in response.get('Contents', []):
        object_url = f"{base_url}/{obj['Key']}"
        
        if obj['Key'].endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_links.append(object_url)

    return image_links
