import boto3

def check_bucket_setup(buckets, unique_word):
    bucket_ends = ['requests', 'web', 'dist']
    print('Checking bucket setup...')

    #Checks bucket names
    print('    Checking bucket names')
    for bucket in buckets:
        if check_bucket_name(bucket.name, unique_word, bucket_ends):
            print(f'        {bucket.name} name formatted correctly')
        else:
            print(f'        Error: {bucket.name} name formatted incorrectly')

    for name in bucket_ends:
        print(f'        Missing bucket name: usu-cs5250-{unique_word}-{name}')

    #Does not need to check bucket region, if the bucket isn't in the correct region will not show up here
    #Checks bucket public access
    print('    Checking bucket public access policy')
    for bucket in buckets:
        if check_bucket_public_access(bucket.Website()):
            print(f'        {bucket.name} has correct public access policy')
        else:
            print(f'        Error: {bucket.name} has incorrect public access policy')


    #Checks bucket versioning
    print('    Checking bucket versioning policy')
    for bucket in buckets:
        if check_bucket_versioning(bucket):
            print(f'        {bucket.name} has correct versioning policy')
        else:
            print(f'        Error: {bucket.name} has incorrect versioning policy of {bucket.Versioning().status}')



def check_bucket_versioning(bucket):
    versioning = {'requests': None, 'web': 'Enabled', 'dist': None}
    parts = bucket.name.split('-')
    if versioning[parts[3]] == bucket.Versioning().status:
        return True
    else:
        return False

def check_bucket_public_access(website):
    public_access = {'requests': False, 'web': True, 'dist': False}
    access = True

    #Tests public access
    try:
        website.index_document
    except:
        access = False

    parts = website.bucket_name.split('-')
    if public_access[parts[3]] == access:
        return True
    else:
        return False

def check_bucket_name(bucket, unique_word, bucket_ends):
    try:
        parts = bucket.split('-')
        if parts[0] == 'usu' and parts[1] == 'cs5250' and parts[2] == unique_word and parts[3] in bucket_ends:
            bucket_ends.remove(parts[3])
            return True
        else:
            return False
    except:
        return False

#Checks the bucket logs
def check_bucket_logs:
    


#Sets up AWS connection
s3_client = boto3.client('s3') 
s3_resource = boto3.resource('s3') 

#Retrieves bucket names from AWS
buckets = list()
for bucket in s3_client.list_buckets()['Buckets']:
    buckets.append(s3_resource.Bucket(bucket['Name']))

unique_word = buckets[0].name.split('-')[2]
check_bucket_setup(buckets, unique_word)
check_bucket_logs(buckets)
