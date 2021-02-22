import boto3

def check_dynamodb_setup(resource):
    print('Checking DynamoDB Setup...')
    tables = resource.tables.all()
    for table in tables:
        secondary_indexes = table.global_secondary_indexes[0]['KeySchema']
        keys = f'''    Primary Key    :  {table.key_schema[0]['AttributeName']} 
    Secondary Key  :  {secondary_indexes[0]['AttributeName']}, {secondary_indexes[1]['AttributeName']}'''
        print(keys)

def check_sg_setup(sg):
    print(sg)

def check_rds_setup(client):
    instances = client.describe_db_instances()['DBInstances']
    cs5250_instance = None
    for instance in instances:
        if instance['DBInstanceIdentifier'] == 'cs5250':
            cs5250_instance = instance

    sg = boto3.resource('ec2').SecurityGroup(instance['VpcSecurityGroups'][0]['VpcSecurityGroupId'])
    setup = f'''Identifier      :  {instance['DBInstanceIdentifier']}'''
    print(setup)
    check_sg_setup(sg)

dynamodb_resource = boto3.resource('dynamodb')
rds_client = boto3.client('rds')
#check_dynamodb_setup(dynamodb_resource)
check_rds_setup(rds_client)
