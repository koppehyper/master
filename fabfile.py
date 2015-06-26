#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, put, local, env, get, execute, settings, hide, task, abort, put
from fabric.colors import *
import os

@task
def test_task():
    local('hostname')

@task
def open_sg():
    sg_id = os.environ.get('MY_SECURITY_GROUP')
    my_ip = local('dig +short myip.opendns.com @resolver1.opendns.com', capture=True)
    local('aws ec2 authorize-security-group-ingress --group-id %s --protocol tcp --port 22 --cidr %s/32' 
          % (sg_id, my_ip))

@task
def close_sg():
    sg_id = os.environ.get('MY_SECURITY_GROUP')
    my_ip = local('dig +short myip.opendns.com @resolver1.opendns.com', capture=True)
    local('aws ec2 revoke-security-group-ingress --group-id %s --protocol tcp --port 22 --cidr %s/32'
          % (sg_id, my_ip))

@task
def deploy():
    run('echo CIRCLECI >> /root/deploy.log')
