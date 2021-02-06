import boto3
import Instance, Iam_Role, VPC


def check_iam_role(role):
    print('Checking IAM Role...')
    if role.name == 'cs5250-EC2-backend-role':
        print('    IAM Role has correct name')
    else:
        print(f'    Error - IAM Role has name: {role.name}')

    count = 0
    policies = ['AmazonS3FullAccess', 'AmazonDynamoDBFullAccess', 'AmazonRDSDataFullAccess']
    for policy in role.policies:
        if policy in policies:
            print(f'    Found {policy} in IAM Role')
            count = count + 1
        else:
            print(f'    Error - Wrong policy: {policy}')

    if count < 3:
        print(f'    Mising policies: {3 - count}')

def view_iam_role(role):

    print('____________IAM_Role__________________')
    print(role.get_role())

def check_instances(instances):
    print('Checking EC2 Instances...')
    count = 0
    for instance in instances:
        if instance.name == 'HostA':
            print('    Found HostA')
            count = count + 1

        if instance.name == 'HostB':
            print('    Found HostB')
            count = count + 1

        if instance.name == 'HostC':
            print('    Found HostC')
            count = count + 1

    if count < 3:
        print(f"Misisng instances: {3 - count}")

def view_instances(instance_list):
    print('\n____________EC2_Instances_____________')
    for instance in instance_list:
        print(instance.get_instance())


def check_vpc(vpc):
    print('Checking VPC...')
    count = 0
    for subnet in vpc.subnets:
        if subnet.name == 'cs5250-public' and subnet.availability_zone == 'us-east-1a':
            print(f'    Found subnet: {subnet.name}')
            count = count + 1

        elif subnet.name == 'cs5250-private1' and subnet.availability_zone == 'us-east-1b':
            print(f'    Found subnet: {subnet.name}')
            count = count + 1

        elif subnet.name == 'cs5250-private2' and subnet.availability_zone == 'us-east-1c':
            print(f'    Found subnet: {subnet.name}')
            count = count + 1

    if count < 3:
        print(f'Missing subnets: {3 - count}')


def view_vpc(vpc):
    print('\n_________________VPC__________________')
    print(vpc.get_vpc())
    

vpc_id = None

iam = boto3.resource('iam')
try:
    role = Iam_Role.Iam_Role(iam.Role('cs5250-EC2-backend-role'))
    check_iam_role(role)
except:
    print('Error retrieving IAM Role')


ec2 = boto3.resource('ec2')
instances_from_aws = ec2.instances.all()
instances = list()

for instance in instances_from_aws:
    vpc_id = instance.vpc_id
    instances.append(Instance.Instance(instance))
try:
    vpc = VPC.VPC(vpc_id)
    print()
    check_vpc(vpc)
except:
    print(f'Error retrieving VPC {vpc_id}')

for instance in instances:
    instance.subnet = vpc.get_subnet_name(instance.subnet)

check_instances(instances)
