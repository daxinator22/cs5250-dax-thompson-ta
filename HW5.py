import boto3

class HW5():

    dynamodb_primary_key = None
    dyanmodb_secondary_key = None
    rds_identifier = None
    sg_name = None
    sg_inbound_rule = list()
    sg_outbound_rule = list()
    logs = 0

    def aws_sg_setup(self, sg):
        try:
            self.sg_inbound_rule.append(sg.ip_permissions[0]['FromPort'])
            self.sg_inbound_rule.append(sg.ip_permissions[0]['IpProtocol'])
            self.sg_inbound_rule.append(sg.ip_permissions[0]['IpRanges'][0]['CidrIp'])
            self.sg_outbound_rule.append(sg.ip_permissions_egress[0]['IpProtocol'])
            self.sg_outbound_rule.append(sg.ip_permissions_egress[0]['IpRanges'][0]['CidrIp'])
            self.sg_name = sg.group_name
        except:
            return


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

        config_list = list()
        for line in config:
            try:
                parts = line.split(':  ')
                config_list.append(parts[1][:-1])
            except:
                continue

        config.close()
        self.dynamodb_primary_key = config_list[0]
        self.dynamodb_secondary_key = config_list[1]
        self.rds_identifier = config_list[2]
        self.sg_name = config_list[3]
        #self.sg_inbound_rule = config_list[4:6]
        #self.sg_outbound_rule = config_list[6:8]
        #self.logs = int(config_list[9])
            

        self.dynamodb_primary_key = config_list[0][:-1]
        self.dynamodb_secondary_key = config_list[1]
        self.rds_identifier = config_list[2]
        self.sg_name = config_list[3]
        self.sg_inbound_rule.append(int(config_list[4]))
        self.sg_inbound_rule.append(config_list[5:7])
        self.sg_outbound_rule = config_list[8:10]
        self.logs = int(config_list[10])

    def to_string(self):
        string = f'''
DynamoDB Setup
    Primary Key              :  {self.dynamodb_primary_key} 
    Secondary Key            :  {self.dynamodb_secondary_key}
RDS Setup
    Identifier               :  {self.rds_identifier}
    Security Group Name      :  {self.sg_name}
                                Inbound Rules    :
                                                    Port       :  {self.sg_inbound_rule[0]}
                                                    Protocol   :  {self.sg_inbound_rule[1]}
                                                    IP Range   :  {self.sg_inbound_rule[2]}
                                Outbound Rules   :  
                                                    Protocol   :  {self.sg_outbound_rule[0]}
                                                    IP Range   :  {self.sg_outbound_rule[1]}
S3 Log Files
    Log Files                :  {self.logs}'''

        return string

    def compare_to(self, compare):

        same = True
        if not compare.dynamodb_primary_key == self.dynamodb_primary_key:
            same = False
            print(f'Incorrect DynamoDB Primary Key: {self.dynamodb_primary_key}')
        if not compare.dynamodb_secondary_key == self.dynamodb_secondary_key:
            same = False
            print(f'Incorrect DynamoDB Secondary Key: {self.dynamodb_secondary_key}')
        if not compare.rds_identifier == self.rds_identifier:
            same = False
            print(f'Incorrect RDS Identifier: {self.rds_identifier}')
        if not compare.sg_name == self.sg_name:
            same = False
            print(f'Incorrect Security Group Name: {self.sg_name}')
        if not compare.sg_inbound_rule == self.sg_inbound_rule:
            same = False
            print(f'Incorrect Security Group Inbound Rule: {self.sg_inbound_rule}')
        if not compare.sg_outbound_rule == self.sg_outbound_rule:
            same = False
            print(f'Incorrect Security Group Outbound Rule: {self.sg_outbound_rule}')
        if not self.logs >= 2:
            same = False
            print(f'Incorrect Log Numbers: {self.logs}')

        if same:
            return 0
        else:
            return -1
    

