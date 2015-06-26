import requests, os

def slack(msg, token, channel, username="Your_bot_name", icon_url='http://i.imgur.com/eLnR8CX.png'):
    api_baseuri = "https://slack.com/api" 
    method = "chat.postMessage" 
    uri = "%s/%s" % (api_baseuri, method)

    param = {"token": token,
             "channel":channel,
             "text":msg,
             "username":username,
             "link_names": True,
             "icon_emoji": icon_url}

    res = requests.get(uri, params=param, verify=False)

if __name__ == '__main__':
    token = os.environ.get('SLACK_TOKEN')
    slack('merged', token, '#testroom', username='Circle CI', icon_url=':checkered_flag:')
    
