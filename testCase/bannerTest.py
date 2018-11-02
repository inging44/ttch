import sys
import unittest2,requests
from readConfig import RunConfig
sys.path.append('./common')
from common.bannerAPI import BannerAPI


class BannerTest(unittest2.TestCase):

    '''
    def __init__(self, arg):
        super(bannerTest, self).__init__()
        self.arg = arg
    '''

    def setUp(self):
        cfg = RunConfig()
        self.baseurl = cfg.get_base_url()
        self.banner = BannerAPI(self.baseurl)
        self.result = ''


    def tearDown(self):
        # print(self.result)
        pass


    def test_banner_success(self):
        params = "url_name=nvzhuang&version=2.0.6"
        response = self.banner.getBannerData(params)
        try:
            self.assertEqual(200,response.status_code)
            self.result = 'banner_success'
        except Exception as e:
            raise e


    def test_banner_version(self):
        params = "url_name=nvzhuang&version=1.8.5"
        response = self.banner.getBannerData(params)
        try:
            self.assertEqual(200,response.status_code)
            self.result = "banner_version"
        except Exception as e:
            raise e

