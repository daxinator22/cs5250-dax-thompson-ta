import boto3
from sys import argv

host_name = argv[1]
host = None

instances = boto3.resource('ec2').instances.all()
for instance in instances:
    if instance.tags[0]['Value'] == host_name:
        host = instance

print(f'Public DNS Host Name: {host.public_dns_name}')
