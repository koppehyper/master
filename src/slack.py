import requests, sys, os

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

if __name__ == '__main__':
    url = sys.argv[1]
    build_number = sys.argv[2]
    msg = '\n'.join(['Congratulations!! Jenkins check passed!',
                     'Please merge this story please.',
                     '*%s*' % url])

    username = 'Jenkins Build %s' % build_number

    token = os.environ.get('SLACK_TOKEN')
    slack(msg, token, '#testroom', username, ':clean:')
