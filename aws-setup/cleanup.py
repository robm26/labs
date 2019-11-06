from __future__ import print_function # Python 2/3 compatibility

import json
import boto3
import sys

userFile = 'users.txt'
userPolicy = 'sandboxUserPolicy'
groupName = 'sandboxUsers'


iam = boto3.client('iam')
accountId = boto3.client('sts').get_caller_identity().get('Account')

print()

response = iam.detach_group_policy(
    GroupName=groupName,
    PolicyArn='arn:aws:iam::'+accountId+':policy/sandboxUserPolicy'
)

print('Deleting IAM Policy: ' + userPolicy)

response2 = iam.delete_policy(
    PolicyArn='arn:aws:iam::'+accountId+':policy/sandboxUserPolicy'
)

with open(userFile, 'rb') as userList:
    for user_raw in userList:
        user = user_raw.rstrip('\n')
        if user:

            print('Deleting IAM User: ' + user)
            response3 = iam.remove_user_from_group(
                GroupName=groupName,
                UserName=user
            )
            aks = iam.list_access_keys(
                UserName=user
            )

            for ak in aks['AccessKeyMetadata']:

                response4 = iam.delete_access_key(
                    UserName=user,
                    AccessKeyId=ak['AccessKeyId']
                )

            response5 = iam.delete_login_profile(
                UserName=user
            )

            response6 = iam.delete_user(UserName=user)


print('Deleting IAM Group: ' + groupName)

response5 = iam.delete_group(GroupName=groupName)



