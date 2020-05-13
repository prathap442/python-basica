import boto3
from botocore.exceptions import NoCredentialsError
import os
from PIL import Image
img = Image.open(os.getcwd()+"/shot4-1.png")
import pdb

ACCESS_KEY="***************************"
SECRET_KEY="***************************"


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        return_value = s3.upload_file(local_file, bucket, s3_file)
        print(dir(return_value))
        pdb.set_trace()
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name



upload_to_aws(os.getcwd()+"/shot4-1.png", "tracksafety-dev",'puppet2.png')

