import http.client, urllib


class PushService():

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def pushMessage(self, title, message, url, url_title, priority=0):
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
            "priority":priority,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()