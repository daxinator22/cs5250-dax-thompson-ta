import boto3

class Subnet():

    subnet_id = None
    subnet = None
    availability_zone = None
    name = None

    def __init__(self, subnet_id):
        self.subnet_id = subnet_id
        self.subnet = boto3.resource('ec2').Subnet(subnet_id)
        self.availability_zone = self.subnet.availability_zone
        self.name = self.parse_tags()

    def parse_tags(self):
        if self.subnet.tags == None:
            return 'None'

        else:
            return self.subnet.tags[0]['Value']


    def get_subnet(self):
        value = f"""
            Subnet ID:      Availability Zone:          Name:
            {self.subnet_id}    {self.availability_zone}            {self.name}
            -----------------------------------
        """


        return value

