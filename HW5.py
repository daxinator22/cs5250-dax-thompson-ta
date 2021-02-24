import boto3

class HW5():

    dynamodb_primary_key = None
    dyanmodb_secondary_key = None
    rds_identifier = None
    sg_name = None
    sg_inbound_rule = None
    sg_outbound_rule = None
    logs = 0

    def aws_sg_setup(self, sg):
        self.sg_inbound_rule = sg.ip_permissions[0]
        self.sg_outbound_rule = sg.ip_permissions_egress[0]
        self.sg_name = sg.group_name

    def aws_rds_setup(self, client):
        instances = client.describe_db_instances()['DBInstances']
        cs5250_instance = None
        for instance in instances:
            if instance['DBInstanceIdentifier'] == 'cs5250':
                cs5250_instance = instance

        sg = boto3.resource('ec2').SecurityGroup(instance['VpcSecurityGroups'][0]['VpcSecurityGroupId'])
        self.rds_identifier = f"{instance['DBInstanceIdentifier']}"
        #print(f'{instance}')
        self.aws_sg_setup(sg)

        
    def aws_dynamodb_setup(self, resource):
        tables = resource.tables.all()
        for table in tables:
            secondary_indexes = table.global_secondary_indexes[0]['KeySchema']
            

        self.dynamodb_primary_key = table.key_schema[0]['AttributeName']
        self.dynamodb_secondary_key = f"{secondary_indexes[0]['AttributeName']}, {secondary_indexes[1]['AttributeName']}"



    def aws_log_files(self, client, resource):
        dist_name = None
        buckets = client.list_buckets()['Buckets']
        for bucket in buckets:
            if bucket['Name'].endswith('dist'):
                dist_name = bucket['Name']

        dist_bucket = resource.Bucket(dist_name)
        objects = dist_bucket.objects.all()
        logs = list()
        for object_file in objects:
            if object_file.key.endswith('log.gz'):
                self.logs += 1


    def aws_setup(self, dynamodb_resource, rds_client, s3_client, s3_resource):
        self.aws_dynamodb_setup(dynamodb_resource)
        self.aws_rds_setup(rds_client)
        self.aws_log_files(s3_client, s3_resource)

    def file_setup(self, path):
        config = open(path)
        print(config.read())
        config.close()


    def to_string(self):
        string = f'''
DynamoDB Setup
    Primary Key              :  {self.dynamodb_primary_key} 
    Secondary Key            :  {self.dynamodb_secondary_key}
RDS Setup
    Identifier               :  {self.rds_identifier}
    Security Group Name      :  {self.sg_name}
                                Inbound Rules    :  Port       :  {self.sg_inbound_rule['FromPort']}
                                                    Protocol   :  {self.sg_inbound_rule['IpProtocol']}
                                                    IP Range   :  {self.sg_inbound_rule['IpRanges'][0]['CidrIp']}
                                Outbound Rules   :  Protocol   :  {self.sg_outbound_rule['IpProtocol']}
                                                    IP Range   :  {self.sg_outbound_rule['IpRanges'][0]['CidrIp']}
S3 Log Files
    {self.logs} logs were found'''


        return string
    

