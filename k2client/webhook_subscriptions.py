""" Handles subscription to webhook services"""
import requests


class WebhookSubscription(object):
    def __init__(self,
                 secret=None,
                 event_type=None,
                 url=None):
        """
        :param secret: (access token) The secret provided by Kopo Kopo to use for accessing services
        :type secret: str

        :param event_type: The event type for which the webhook is being created
        :type event_type: str

        :param url: The end point to which the webhook is to be sent (https://myawesomeapplication.com/destination)
        :type url: str
        """
        self.secret = secret
        self.event_type = event_type
        self.url = url

    def subscribe(self):
        # set request body
        request_body = build_request_body(self.event_type, self.url, self.secret)
        subscription = requests.post(self.url, request_body)
        return subscription

    def location(self):
        subscription_location = self.subscribe().headers.get('location')
        return subscription_location


def build_request_body(provided_event_type, provided_url, provided_secret):
    req_body = "{\" event_type \": \""+provided_event_type + "\"," "\"url""\":" + "\""+provided_url + "\"," "\"secret" "\":" "\"" + provided_secret + "\"}"
    return req_body