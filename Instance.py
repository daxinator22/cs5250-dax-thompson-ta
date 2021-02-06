import boto3, Security_Group

class Instance():

    instance = None
    name = None
    instance_id = None
    ami = None
    instance_type = None
    subnet = None
    ip = None
    iam = None
    storage = None
    sg = None

    def __init__(self, instance):
        self.instance = instance
        self.name = self.instance.tags[0]['Value']
        self.instance_id = instance.id
        self.ami = instance.image_id
        self.instance_type = instance.instance_type
        self.subnet = instance.subnet_id
        self.ip = instance.public_ip_address
        self.iam = self.parse_iam()
        self.storage = self.parse_storage()
        self.sg = Security_Group.Security_Group(self.parse_sg())

    def parse_iam(self):
        if self.instance.iam_instance_profile == None:
            return 'None'
        
        else:
            parts = self.instance.iam_instance_profile['Arn'].split('/')
            return parts[1]

    def parse_storage(self):
        volumes = self.instance.volumes.all()
        result = ''
        for volume in volumes:
            result = result + str(volume.size) + ' GiB'

        return result

    def parse_sg(self):
        return self.instance.security_groups[0]['GroupId']

    def get_instance(self):
        return f"""
        {self.name}
        -----------------------------------
        Instance ID       : {self.instance_id}
        AMI               : {self.ami}
        Instance Type     : {self.instance_type}
        Subnet            : {self.subnet}
        Public IP Address : {self.ip}
        IAM Role          : {self.iam}
        Storage           : {self.storage}
        Security Group    : {self.sg.get_sg()}
        """
