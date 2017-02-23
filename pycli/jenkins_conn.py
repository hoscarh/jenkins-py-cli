import requests
from config import *


class JenkinsConn(object):

    def __init__(self):
        self.session = requests.session()
        self.session.auth = (jenkins['username'], jenkins['api_key'])

    def send_post(self, url, params=None, config_file=None, headers=None):
        response = self.session.post(url,  params=params, data=config_file, headers=headers, verify=False)
        return response


