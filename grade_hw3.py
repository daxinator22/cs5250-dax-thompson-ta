import boto3
import Instance, Iam_Role

iam = boto3.resource('iam')
role = Iam_Role.Iam_Role(iam.Role('cs5250-EC2-backend-role'))

print('____________IAM_Role__________________')
print(role.get_role())


ec2 = boto3.resource('ec2')
instances_from_aws = ec2.instances.all()
instances = list()

for instance in instances_from_aws:
    instances.append(Instance.Instance(instance))

print('\n____________EC2_Instances_____________')

for instance in instances:
    print(instance.get_instance())


print('\n___________Security_Groups_____________')
