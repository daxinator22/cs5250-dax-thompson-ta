import boto3

ec2 = boto3.resource('ec2')
instances = ec2.instances.all()

for instance in instances:
    print(instance.image_id)
