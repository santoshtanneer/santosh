import boto
from boto.s3.key import Key
import os


access_key_id = 'AKIAIVEYLJPVCMMPU3ZQ'
secret_access_key = '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'


def create_bucket(bucket_name):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    if not conn.lookup(bucket_name):
        print 'creating bucket'
        conn.create_bucket(bucket_name)
    else:
        print 'bucket already exists'
        
def delete_bucket(bucket_name):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    for key in bucket.list():
        key.delete()
    bucket.delete()
    
def delete_file_from_bucket(bucket_name,file_name):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    for key in bucket.list():
        if key.name == file_name:
            key.delete()

def upload_file_to_bucket(bucket_name,file_loc):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    k = Key(bucket)
    k.key = os.path.basename(file_loc)
    k.set_contents_from_file(open(file_loc,'rb'))

def download_file_from_bucket(bucket_name,file_name):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    for key in bucket.list():
        if key.name == file_name:
            key.get_contents_to_file(open('rakesh.jpg','wb'))

def set_file_permissions(bucket_name,file_name,permission):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    for key in bucket.list():
        if key.name == file_name:
            key.set_acl(permission)

def get_all_file_names(bucket_name):
    conn = boto.connect_s3(access_key_id,secret_access_key)
    bucket = conn.get_bucket(bucket_name)
    for key in bucket.list():
        print key.name
        
create_bucket('santosh11')
# upload_file_to_bucket('rakeshbalusabucket', 'C:\\Users\\rakesh\\Downloads\\beast.jpg')
# set_file_permissions('rakeshbalusabucket', 'beast.jpg', 'public-read')
# download_file_from_bucket('rakeshbalusabucket', 'beast.jpg')
# get_all_file_names('rakeshbalusabucket')
# delete_file_from_bucket('rakeshbalusabucket', 'beast.jpg')
#delete_bucket('rakeshbalusabucket')