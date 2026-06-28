# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
# sessions are your friend for creating clients https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html
# session docs slightly out of date.  see get_session() below for clean example
# boto3 pagination, and why it is cool:  https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html
# boto3 undocumented feature, that is also cool https://github.com/boto/boto3/issues/3001 it may be documented by the time you see this.
# aws ec2 describe-instances <args, incl --instance-id> are your friends here

from session import get_session, parse_args
import boto3

DEFAULT_REGION = "us-west-2"


# create a client that returns a paginated object, which is giant dictonary
def ec2instances(session: boto3.session.Session) -> list[list[str | None]]:
    """
    Return a list of running EC2 instances.

    Each entry is [InstanceId, PublicIpAddress, PrivateIpAddress].
    Uses pagination to handle large result sets.

    Args:
        session: boto3 Session object.
    """
    instances: list[list[str | None]] = []
    pagination_filters = [{"Name": "instance-state-name", "Values": ["running"]}]
    page = (
        session.client("ec2")
        .get_paginator("describe_instances")
        .paginate(Filters=pagination_filters)
        .build_full_result()
    )
    for reservation in page["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(
                [
                    instance["InstanceId"],
                    instance["PublicIpAddress"],
                    instance["PrivateIpAddress"],
                ]
            )
    return instances


if __name__ == "__main__":
    args = parse_args()
    session = get_session(region=args.region, profile=args.profile)
    print(ec2instances(session))
