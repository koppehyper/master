#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, sys, os, subprocess

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
        subprocess.check_call(['/usr/local/bin/hub', 'pull-request', '-F', '/tmp/pr_msg'])
    else:
        subprocess.check_call(['git', 'push', 'origin', ':test_push'])

    exit(0 if is_setting_ok else 1)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        build_no = sys.argv[1]
    else:
        exit(-1)
        
    main(build_no)
