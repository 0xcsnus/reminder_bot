import json
import urllib.request as req
import os

# from dotenv import load_dotenv
# load_dotenv()


def remind(event, context):
    
    # For daily and weekly meetings
    if 'name' in event:
        if event['name'] == 'daily_reminder':
            #Formats text message according to slack docs
            content = formatting("This is a daily reminder. You have a meeting at 12")
            send_msg(content)
        elif event['name'] == 'weekly_reminder':
            content = formatting("This is a weekly reminder. You have a meeting at 11")
            send_msg(content)
            
    # To trigger for instant meetings        
    elif event['path'] == '/instant':
            content = formatting("This is an instant reminder. You have a meeting now")  
            send_msg(content) 
            
    
def send_msg(content):
        url = os.environ.get('SLACK')
        request_object = req.Request(url, content, {'Content-Type':'application/json'})
        req.urlopen(request_object)
    
    
def formatting(data):
    text = {
        "text": data
    }
    return json.dumps(text).encode("utf-8")



