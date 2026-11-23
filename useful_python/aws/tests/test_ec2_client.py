"""Tests for ec2_client.ec2instances against moto's fake AWS. No real account is touched."""

import boto3
import pytest
from moto import mock_aws

import ec2_client

REGION = "us-west-2"


@pytest.fixture
def session(monkeypatch):
    # fake credentials, and no profile, so nothing can reach a real account
    for var in ("AWS_PROFILE", "AWS_DEFAULT_PROFILE"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", REGION)
    with mock_aws():
        yield boto3.Session(region_name=REGION)


def _ami(ec2):
    return ec2.describe_images(Owners=["amazon"])["Images"][0]["ImageId"]


def _only_instance(ec2):
    return ec2.describe_instances()["Reservations"][0]["Instances"][0]


def test_instance_with_public_ip(session):
    ec2 = session.client("ec2")
    ec2.run_instances(ImageId=_ami(ec2), MinCount=1, MaxCount=1)
    assert "PublicIpAddress" in _only_instance(ec2)  # sanity check on moto

    [[instance_id, public_ip, private_ip]] = ec2_client.ec2instances(session)
    assert instance_id is not None
    assert instance_id.startswith("i-")
    assert public_ip
    assert private_ip


def test_instance_without_public_ip(session):
    ec2 = session.client("ec2")
    vpc = ec2.create_vpc(CidrBlock="10.0.0.0/16")["Vpc"]["VpcId"]
    # a new subnet doesn't auto-assign public IPs
    subnet = ec2.create_subnet(VpcId=vpc, CidrBlock="10.0.1.0/24")["Subnet"]["SubnetId"]
    ec2.run_instances(ImageId=_ami(ec2), MinCount=1, MaxCount=1, SubnetId=subnet)
    assert "PublicIpAddress" not in _only_instance(ec2)  # sanity check on moto

    [[_instance_id, public_ip, private_ip]] = ec2_client.ec2instances(session)
    assert public_ip is None
    assert private_ip
