import boto3, HW5

dynamodb_resource = boto3.resource('dynamodb')
rds_client = boto3.client('rds')
s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
student = HW5.HW5()
#student.aws_setup(dynamodb_resource, rds_client, s3_client, s3_resource)
#print(student.to_string())
example = HW5.HW5()
#example.file_setup('hw5_example.txt')

print(student.to_string())
