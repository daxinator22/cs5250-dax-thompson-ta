import boto3

class Iam_Role():

    role = None
    policies = list()

    def __init__(self, role):
        self.role = role
        for policy in self.role.attached_policies.all():
            self.policies.append(policy.policy_name)


    def get_role(self):
        value = f"""
        {self.role.name}
        -----------------------------------"""
        for policy in self.policies:
            value = value + f"""
        {policy}"""

        return value

