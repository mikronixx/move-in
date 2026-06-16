import argparse

import boto3
import boto3.session

DEFAULT_REGION = "us-west-2"


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.
    --profile and --region are mandatory
    """
    parser = argparse.ArgumentParser(description="List running EC2 instances")
    parser.add_argument("--profile", required=True, help="AWS profile name")
    parser.add_argument(
        "--region", required=True, help="AWS region (required if --profile is set)"
    )
    args = parser.parse_args()
    return args


def get_session(
    region: str = DEFAULT_REGION, profile: str | None = None
) -> boto3.session.Session:
    """
    Create a boto3 session.

    Args:
        region: AWS region name. Defaults to us-west-2.
        profile: AWS profile name. Defaults to None (uses default profile).
    """
    return boto3.Session(region_name=region or "us-west-2", profile_name=profile)
