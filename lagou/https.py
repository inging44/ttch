#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,random
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')


class Http:
    '''
    http请求相关的操作
    '''
    def __init__(self):
        self.UA =  ['Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0;\
       Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1))',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; 360SE)',

      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
      'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
      'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
      'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; \
      SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 \
      (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
      'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) \
      Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',

      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) \
      Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; \
      .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',

      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; \
      .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',

      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
      'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',

      'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) \
      Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0',

      'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) \
      Version/5.0.2 Mobile/8C148 Safari/6533.18.5',

      'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)']

    def get(self, url, headers=None, cookies=None, proxy=None, timeOut=5, timeOutRetry=5):
        '''
        获取网页源码
        url: 网页链接
        headers: headers
        cookies: cookies
        proxy: 代理
        timeOut: 请求超时时间
        timeOutRetry: 超时重试次数
        return: 源码
        '''
        if not url:
            logging.error('GetError url not exit')
            return 'None'
        logging.error('Get %s' % url)
        try:
            if not headers: headers = {'User-Agent': self.UA[random.randint(0, len(self.UA)-1)]}
            #if not proxy: proxy = {'http':"http://"+IP[random.randint(0, len(IP)-1)]}
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy, timeout=timeOut)
            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text
            else:
                htmlCode = 'None'
            logging.error('Get %s %s' % (str(response.status_code), url))
        except Exception as e:
            logging.error('GetExcept %s' % str(e))
            if timeOutRetry > 0:
                htmlCode = self.get(url=url, timeOutRetry=(timeOutRetry-1))
            else:
                logging.error('GetTimeOut %s' % url)
                htmlCode = 'None'
        return htmlCode

    def post(self,url, para, headers=None, cookies=None, proxy=None, timeOut=5, timeOutRetry=5):
        '''
        post获取响应
        url: 目标链接
        para: 参数
        headers: headers
        cookies: cookies
        proxy: 代理
        timeOut: 请求超时时间
        timeOutRetry: 超时重试次数
        return: 响应
        '''
        if not url or not para:
            logging.error('PostError url or para not exit')
            return None
        logging.error('Post %s' % url)
        try:
            if not headers:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3'}
            response = requests.post(url, data=para, headers=headers, cookies=cookies, proxies=proxy, timeout=timeOut)
            if response.status_code == 200 or response.status_code == 302:
                htmlCode = response.text
            else:
                htmlCode = None
            logging.error('Post %s %s' % (str(response.status_code), url))
        except Exception as e:
            logging.error('PostExcept %s' % str(e))
            if timeOutRetry > 0:
                htmlCode = self.post(url=url, para=para, timeOutRetry=(timeOutRetry-1))
            else:
                logging.error('PostTimeOut %s' % url)
                htmlCode = None
        return htmlCode

    def confirm(self, htmlCode, url, headers, cookies,proxy,catch_retry=5):
        '''
        反爬，验证页面
        htmlCode:网页源码
        return:网页源码
        '''
        #获取网页title判断是否被ban
        return htmlCode

    def urlprocess(self,items):
        # +    URL 中+号表示空格               %2B
        # 空格 URL中的空格可以用+号或者编码    %20
        # /    分隔目录和子目录                %2F
        # ?    分隔实际的URL和参数             %3F
        # %    指定特殊字符                    %25
        # #    表示书签                        %23
        # &    URL 中指定的参数间的分隔符      %26
        # =    URL 中指定参数的值              %3D
        content = items.replace('&#047;','%2F').replace('&#061;','%3D').replace('+','%2B').replace(\
                                ' ','%20').replace('/','%2F').replace('?','%3F').replace('=','%3D')
        return content