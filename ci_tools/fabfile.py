#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, put, local, env, get, execute, settings, hide, task, abort, put
from fabric.colors import *
import os, requests

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

@task
def git_merge():
    circle_branch = os.environ.get('CIRCLE_BRANCH')
    local("git config --global user.name 'Koppe Pan'")
    local("git config --global user.email 'koppehyper@gmail.com'")
    local("./hub pull-request -m 'Test PullRequest'")
    local("git checkout master")
    local("git pull")
    local("git merge --no-ff %s -m 'Merge master'" % circle_branch) 
    local("git push origin master")
    local("git push origin :%s" % circle_branch)


@task 
def slack():
    api_baseuri = "https://slack.com/api"
    method = "chat.postMessage"
    uri = "%s/%s" % (api_baseuri, method)
    token = os.environ.get('SLACK_TOKEN')
    msg = 'MERGED'
    channel = '#testroom'
    username = 'Hogehoge'
    icon_url = ':dora:'

    param = {"token": token,
             "channel":channel,
             "text":msg,
             "username":username,
             "link_names": True,
             "icon_emoji": icon_url}

    res = requests.get(uri, params=param, verify=False)


@task
def artifact_test():
    ev = '''CIRCLE_PROJECT_USERNAME
CIRCLE_PROJECT_REPONAME
CIRCLE_BRANCH
CIRCLE_SHA1
CIRCLE_COMPARE_URL
CIRCLE_BUILD_NUM
CIRCLE_PREVIOUS_BUILD_NUM
CI_PULL_REQUESTS
CI_PULL_REQUEST
CIRCLE_ARTIFACTS
CIRCLE_USERNAME
CIRCLE_TEST_REPORTS'''

    c = ev.splitlines()
    
    for x in c:
        print "%-25s ... %s" % (x, os.environ.get(x))
