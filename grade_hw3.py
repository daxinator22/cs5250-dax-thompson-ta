import boto3
import Instance, Iam_Role, VPC
from sys import argv


def check_iam_role(role):
    print('Checking IAM Role...')
    if role.name == 'cs5250-EC2-backend-role':
        print('    IAM Role has correct name')
    else:
        print(f'    Error - IAM Role has name: {role.name}')

    count = 0
    policies = ['AmazonS3FullAccess', 'AmazonDynamoDBFullAccess', 'AmazonRDSFullAccess']
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
            if instance.ami == 'ami-0be2609ba883822ec' or instance.ami == 'ami-047a51fa27710816e':
                print('        Found Amazon Linux AMI')

            else:
                print(f'        Error: Incorrect AMI - {instance.ami}')

            if instance.instance_type == 't2.micro':
                print('        Found Correct Instance Type')

            else:
                print(f'        Error: Incorrect Instance Type - {instance.instance_type}')

            if instance.subnet == 'cs5250-public':
                print('        Found Correct Subnet')

            else:
                print(f'        Error: Incorrect Subnet - {instance.subnet}')

            if instance.iam == 'None':
                print('        Found Correct IAM Role')

            else:
                print(f'        Error: Incorrect IAM Role - {instance.iam}')

            if not instance.ip == None:
                print(f'        Found Public IP Address: {instance.ip}')

            else:
                print(f'        Error: Incorrect Public IP Settings - {instance.ip}')

            if instance.storage == '8 GiB':
                print('        Found Correct Storage')

            else:
                print(f'        Error: Incorrect Storage Size - {instance.storage}')

            if instance.sg.name == 'ssh-only-sg':
                print('        Found Security Group')
                if instance.sg.permissions_in['IpProtocol'] == 'tcp':
                    print('            Found Security Group In IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group In IP Protocol - {instance.sg.permissions_in["IpProtocol"]}')
                if instance.sg.permissions_in['IpRanges'][0]['CidrIp'] == '0.0.0.0/0':
                    print('            Found Security Group In IP Range')

                else:
                    print(f'            Error: Incorrect Security Group In IP Ranges - {instance.sg.permissions_in["IpRanges"][0]["CidrIp"]}')

                if instance.sg.permissions_out['IpProtocol'] == '-1':
                    print('            Found Security Group Out IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Protocol - {instance.sg.permissions_out["IpProtocol"]}')
                if instance.sg.permissions_out['IpRanges'][0]['CidrIp'] == '0.0.0.0/0':
                    print('            Found Security Group Out IP Range')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Ranges - {instance.sg.permissions_out["IpRanges"][0]["CidrIp"]}')



            else:
                print(f'        Error: Incorrect Security Group - {instance.sg.name}')

            count = count + 1

        if instance.name == 'HostB':
            print('    Found HostB')
            if instance.ami == 'ami-0053f34b22df259f2':
                print('        Found Amazon Linux AMI')

            else:
                print(f'        Error: Incorrect AMI - {instance.ami}')

            if instance.instance_type == 't2.micro':
                print('        Found Correct Instance Type')

            else:
                print(f'        Error: Incorrect Instance Type - {instance.instance_type}')

            if instance.subnet == 'cs5250-private1':
                print('        Found Correct Subnet')

            else:
                print(f'        Error: Incorrect Subnet - {instance.subnet}')

            if instance.iam == 'cs5250-EC2-backend-role':
                print('        Found Correct IAM Role')

            else:
                print(f'        Error: Incorrect IAM Role - {instance.iam}')

            if not instance.ip == None:
                print('        Found Public IP Address')

            else:
                print(f'        Error: Incorrect Public IP Settings - {instance.ip}')

            if instance.storage == '8 GiB':
                print('        Found Correct Storage')

            else:
                print(f'        Error: Incorrect Storage Size - {instance.storage}')

            if instance.sg.name == 'vpc-only-sg':
                print('        Found Security Group')
                if instance.sg.permissions_in['IpProtocol'] == '-1':
                    print('            Found Security Group In IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group In IP Protocol - {instance.sg.permissions_in["IpProtocol"]}')
                if instance.sg.permissions_in['IpRanges'][0]['CidrIp'] == '172.31.0.0/16':
                    print('            Found Security Group In IP Range')

                else:
                    print(f'            Error: Incorrect Security Group In IP Ranges - {instance.sg.permissions_in["IpRanges"][0]["CidrIp"]}')

                if instance.sg.permissions_out['IpProtocol'] == '-1':
                    print('            Found Security Group Out IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Protocol - {instance.sg.permissions_out["IpProtocol"]}')
                if instance.sg.permissions_out['IpRanges'][0]['CidrIp'] == '0.0.0.0/0':
                    print('            Found Security Group Out IP Range')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Ranges - {instance.sg.permissions_out["IpRanges"][0]["CidrIp"]}')

            else:
                print(f'        Error: Incorrect Security Group - {instance.sg.name}')

            count = count + 1

        if instance.name == 'HostC':
            print('    Found HostC')
            if instance.ami == 'ami-0053f34b22df259f2':
                print('        Found Amazon Linux AMI')

            else:
                print(f'        Error: Incorrect AMI - {instance.ami}')

            if instance.instance_type == 't2.micro':
                print('        Found Correct Instance Type')

            else:
                print(f'        Error: Incorrect Instance Type - {instance.instance_type}')

            if instance.subnet == 'cs5250-private2':
                print('        Found Correct Subnet')

            else:
                print(f'        Error: Incorrect Subnet - {instance.subnet}')

            if instance.iam == 'cs5250-EC2-backend-role':
                print('        Found Correct IAM Role')

            else:
                print(f'        Error: Incorrect IAM Role - {instance.iam}')

            if not instance.ip == None:
                print('        Found Public IP Address')

            else:
                print(f'        Error: Incorrect Public IP Settings - {instance.ip}')

            if instance.storage == '16 GiB':
                print('        Found Correct Storage')

            else:
                print(f'        Error: Incorrect Storage Size - {instance.storage}')

            if instance.sg.name == 'vpc-only-sg':
                print('        Found Security Group')
                if instance.sg.permissions_in['IpProtocol'] == '-1':
                    print('            Found Security Group In IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group In IP Protocol - {instance.sg.permissions_in["IpProtocol"]}')
                if instance.sg.permissions_in['IpRanges'][0]['CidrIp'] == '172.31.0.0/16':
                    print('            Found Security Group In IP Range')

                else:
                    print(f'            Error: Incorrect Security Group In IP Ranges - {instance.sg.permissions_in["IpRanges"][0]["CidrIp"]}')

                if instance.sg.permissions_out['IpProtocol'] == '-1':
                    print('            Found Security Group Out IP Protocol')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Protocol - {instance.sg.permissions_out["IpProtocol"]}')
                if instance.sg.permissions_out['IpRanges'][0]['CidrIp'] == '0.0.0.0/0':
                    print('            Found Security Group Out IP Range')

                else:
                    print(f'            Error: Incorrect Security Group Out IP Ranges - {instance.sg.permissions_out["IpRanges"][0]["CidrIp"]}')

            else:
                print(f'        Error: Incorrect Security Group - {instance.sg.name}')

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
role = None
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

print()
check_instances(instances)

if len(argv) > 1 and argv[1] == '-p':
    if not role == None: 
        print(role.get_role())

    print(vpc.get_vpc())
    for instance in instances:
        print(instance.get_instance())

