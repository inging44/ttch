#coding = utf-8
from configparser import ConfigParser
import os

class RunConfig:
    def __init__(self):
        path = os.getcwd()
        filename = os.path.join(path, 'config.ini')
        httpcfg = ConfigParser()
        httpcfg.read(filename)
        self.url = httpcfg.get('baseurl', 'url')

    def get_base_url(self):
        return self.url

    def get_db(self):
        return self.db