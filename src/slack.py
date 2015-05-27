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
             "icon_url":icon_url}

    res = requests.get(uri, params=param)

if __name__ == '__main__':
    msg = sys.argv[1]
    token = os.environ.get('SLACK_TOKEN')    
    slack(msg, token, '#testroom', 'Jenkins', None)
