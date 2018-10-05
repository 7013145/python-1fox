from HttpMD5Util import httpGet
import os
import datetime


class OneFox:
    def __init__(self, api_token):
        self.api_token = api_token
        self.url_base = "https://1fox.com"
        self.resource_header = "/api/v1/"

    def error_check(self, result):
        if result['warning']:
            string = source + " warning: " + str(result['warning_message'])
            print(string)
        if result['error']:
            string = source + " error[" + str(result['error_code']) + "]: " + str(result['error_message'])
            print(string)

    def user_get(self, currency='BTC'):
        resource = self.resource_header + "user/get.php"
        params = {
            "token": self.api_token,
            "currency": currency
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_overview(self, currency='BTC'):
        resource = self.resource_header + "user/overview.php"
        params = {
            "token": self.api_token,
            "currency": currency
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_dead_man_switch(self, symbols, stop=False):
        resource = self.resource_header + "user/dead_man_switch.php"
        params = {
            "token": self.api_token,
            "symbols": ','.join([symbols]),
            "stop": stop
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

