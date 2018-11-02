import requests

class BannerAPI:
    def __init__(self, url):
        self.baseurl=url


    u'''
    Method：get
    @param string url_name
    @param String version

    '''
    def getBannerData(self,params='version=2.0.6'):
        url = self.baseurl+'/jxh5/banners/v4?'+params
        r = requests.get(url)
        return r