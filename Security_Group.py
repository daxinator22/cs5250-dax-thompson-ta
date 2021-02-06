import boto3

class Security_Group():

    sg_id = None
    sg = None
    name = None
    permissions_in = None
    permissions_out = None

    def __init__(self, sg_id):
        self.sg_id = sg_id
        self.sg = boto3.resource('ec2').SecurityGroup(sg_id)
        self.name = self.sg.group_name
        self.permissions_in = self.sg.ip_permissions[0]
        self.permissions_out = self.sg.ip_permissions_egress[0]



    def get_sg(self):
        value = f"""{self.name}
                ---------------
                ID             - {self.sg_id}
                Inbound Rules  - Protocol: {self.permissions_in['IpProtocol']} ||| IP Ranges: {self.permissions_in['IpRanges'][0]['CidrIp']}
                Outbound Rules - Protocol: {self.permissions_out['IpProtocol']} ||| IP Ranges: {self.permissions_out['IpRanges'][0]['CidrIp']}
        """


        return value

