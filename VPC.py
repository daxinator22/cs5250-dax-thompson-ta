import boto3, Subnet

class VPC():

    vpc_id = None
    vpc = None
    subnets = list()

    def __init__(self, vpc_id):
        self.vpc_id = vpc_id
        self.vpc = boto3.resource('ec2').Vpc(vpc_id)

        for subnet in self.vpc.subnets.all():
            self.subnets.append(Subnet.Subnet(subnet.id))


    def get_subnet_name(self, subnet_id):
        for subnet in self.subnets:
            if subnet.subnet_id == subnet_id:
                return subnet.name

    def get_vpc(self):
        value = f"""
        VPC ID       : {self.vpc_id}
        -----------------------------------
        """
        for subnet in self.subnets:
            value += subnet.get_subnet()


        return value

