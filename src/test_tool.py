#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, sys, os, subprocess
from fabric.api import local

def slack(msg, token, channel, username="Your_bot_name", icon_url='http://i.imgur.com/eLnR8CX.png'):
    api_baseuri = "https://slack.com/api"
    method = "chat.postMessage"
    uri = "%s/%s" % (api_baseuri, method)

    param = {"token":token,
             "channel":channel,
             "text":msg,
             "username":username,
             "link_names": True,
             "icon_emoji":icon_url}

    res = requests.get(uri, params=param)


def main(build_no):
    token = os.environ.get('SLACK_TOKEN')
    channel = '#testroom'
    username = 'Jenkins Build #%s' % build_no
    
    with open('setting.conf') as s: lines = s.read()
    is_setting_ok = 'OK' in lines

    if is_setting_ok:
        pr_url = local('/usr/local/bin/hub pull-request -F /tmp/pr_msg', capture=True)
        local('/usr/local/bin/hub merge %s' % pr_url)
        
        msg = '\n'.join(['Build Passing (Merged!)', str(pr_url)])
        
        icon_url = ':clean:'

        slack (msg, token, channel, username, icon_url)
        
    else:
        print local('git push origin :test_push', capture=True)
        msg = 'Sorry, Build %s was failed...' % build_no
        icon_url = ':x:'
        slack (msg, token, channel, username, icon_url)
    

    exit(0 if is_setting_ok else 1)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        build_no = sys.argv[1]
    else:
        exit(-1)

    main(build_no)
