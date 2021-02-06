import boto3

class Security_Group():

    group = None
    policies = list()

    def __init__(self, group):
        self.group = group


    def get_role(self):
        value = f"""
        {self.role.name}
        -----------------------------------"""
        for policy in self.policies:
            value = value + f"""
        {policy}"""

        return value

