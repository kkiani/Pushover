import http.client, urllib
from enum import Enum

class MessagePriority(Enum):
    Lowest_Priority = -2
    Low_Priority = -1
    Normal_Priority = 0
    High_Priority = 1

class PushService():

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def pushMessage(self, title, message, url, url_title, priority=MessagePriority.Normal_Priority):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": self.token,
            "user": self.user_id,
            "title":title,
            "sound":"classical",
            "message": message,
            "url":url,
            "url_title":url_title,
            "priority":priority.value,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
