# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
# sessions are your friend for creating clients https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html
# session docs slightly out of date.  see boto3session() below for clean example
# boto3 pagination, and why it is cool:  https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html
# boto3 undocumented feature, that is also cool https://github.com/boto/boto3/issues/3001 it may be documented by the time you see this.
# aws ec2 describe-instances <args, incl --instance-id> are your friends here

import boto3

# basic boto3 auth using local aws credentials


def boto3session():
    boto3session = boto3.Session(region_name="us-west-2")
    return boto3session


boto3session = boto3session()

# create a client that returns a paginated object, which is giant dictonary


def ec2instances(boto3session):
    ec2instances = []
    pagination_filters = [{"Name": "instance-state-name", "Values": ["running"]}]
    page = (
        boto3session.client("ec2")
        .get_paginator("describe_instances")
        .paginate(Filters=pagination_filters)
        .build_full_result()
    )
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            ec2instances.append(
                [
                    instance["InstanceId"],
                    instance["PublicIpAddress"],
                    instance["PrivateIpAddress"],
                ]
            )
    return ec2instances


print(ec2instances(boto3session))
