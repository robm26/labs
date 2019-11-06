from __future__ import print_function # Python 2/3 compatibility

import json
import boto3
import string
import random

userPolicy = 'sandboxUserPolicy'
userPolicyFile = 'policy.json'
groupName = 'sandboxUsers'
userFile = 'users.txt'
delimeter = '\t'

iam = boto3.client('iam')
accountId = boto3.client('sts').get_caller_identity().get('Account')

print()

with open(userPolicyFile, 'rb') as pFile:
    policy = json.load(pFile)

    print('Creating IAM Policy: ' + userPolicy)
    response = iam.create_policy(
      PolicyName=userPolicy,
      PolicyDocument=json.dumps(policy)
    )

print('Creating IAM Group: ' + groupName)
response2 = iam.create_group(
    GroupName=groupName
)
print('Attaching Policy to Group ')
response3 = iam.attach_group_policy(
    GroupName=groupName,
    PolicyArn='arn:aws:iam::'+accountId+':policy/sandboxUserPolicy'
)


def randomString(stringLength=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

login_url = 'https://'+accountId+'.signin.aws.amazon.com/console'

print()
print('All users may login via:  ' + login_url)
print()
print('Username        Password        AccessKeyId             SecretAccessKey')
print('--------------- --------------- ----------------------- ----------------------------------------')

with open(userFile, 'rb') as userList:
    for user_raw in userList:
        user = user_raw.rstrip('\n')
        if user:

            # print('Creating user ' + user)
            response4 = iam.create_user(UserName=user)

            response5 = iam.add_user_to_group(
                GroupName=groupName,
                UserName=user
            )

            ak = iam.create_access_key(
                UserName=user
            )
            password = randomString()

            response6 = iam.create_login_profile(
                UserName=user,
                Password=password,
                PasswordResetRequired=False
            )

            print(user + delimeter + password + delimeter + ak['AccessKey']['AccessKeyId'] + delimeter + ak['AccessKey']['SecretAccessKey'])



