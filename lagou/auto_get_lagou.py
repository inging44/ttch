#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from https import Http
import time
# import logging
import smtplib
from email.mime.text import MIMEText
import demjson
import requests
import bs4

#定义header
headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept-Encoding': 'gzip, deflate',
           'Host': 'www.lagou.com',
           'Origin': 'http://www.lagou.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'https://www.lagou.com/jobs/list_python?px=new&city=%E6%88%90%E9%83%BD',
           'Proxy-Connection': 'keep-alive',
           'X-Anit-Forge-Code': '0',
           'X-Anit-Forge-Token': None,
           'Cookie': 'user_trace_token=20171128173126-0bb2cc5bf83d49ddaa479fc07e33e10a; LGUID=20171128173133-ebed45b1-d41e-11e7-9ab7-5254005c3644; JSESSIONID=ABAAABAACEBACDG3381DC7F5DD8A2C0B28348ADC3BA57FF; _gat=1; X_HTTP_TOKEN=12ca0280aca5e1c0b5eb1bfe924e98ec; _putrc=DDAB52D6F6BF07B5; login=true; unick=%E9%BB%84%E5%85%B0%E5%A9%B7; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=137; gate_login_token=2b52d1ddae541fa67a650b326f0feb34cf5683c9ca35c43d; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516609575,1517369749; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517382018; LGSID=20180131142800-e25c30d9-064f-11e8-abe0-5254005c3644; LGRID=20180131150031-6d50958f-0654-11e8-a2fe-525400f775ce; TG-TRACK-CODE=index_navigation; _ga=GA1.2.327129751.1511861500; _gid=GA1.2.1003860854.1517369750; SEARCH_ID=f525a987fb004241b691cc1c56f26090; index_location_city=%E6%88%90%E9%83%BD'
           }

url = 'https://www.lagou.com/jobs/positionAjax.json?px=new'

needAddtionalResult = False
city = u'成都'
kd = u'测试'



'''
http请求获取api信息
'''
def getInfo(url, para):
    print(url)
    print(para)
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=headers)
    if htmlCode != None:
        json = demjson.decode(htmlCode)
    # print(htmlCode)
    else:
        return ""

    # logging.error('htmlCode:')
    # logging.error(htmlCode)
    pageCount = getPageCount(json)
    html = '<html><style>.a{display:none}:target{display: table-row;border: 2px solid #D4D4D4;background-color: #e5eecc;}</style><body><table><tr><th>公司名</th><th>职位</th><th>公司规模</th><th>年限</th><th>地区</th><th>薪资</th><th>发布时间</th></tr>'
    jobList = []
    for i in range(1,pageCount+1):#
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=headers)
        jobList += getAll(htmlCode)
        time.sleep(2)
    jobListAfterFilter  = filt(jobList)
    html += parseInfo(jobListAfterFilter)
    html += '</table></body></html>'
    return html


'''
        解析并计算页面数量
        :return: 页面数量
'''
def getPageCount(json):
    # print(json)
    totalCount = json['content']['positionResult']['totalCount']      #职位总数量
    resultSize = json['content']['positionResult']['resultSize']      #每一页显示的数量
    pageCount = int(totalCount) // int(resultSize) + 1          #页面数量
    return pageCount

#解析json为嵌套dict的list
def getAll(htmlCode):
    json = demjson.decode(htmlCode)
    #解析json为嵌套dict的list
    jobList=[]
    for i in json['content']['positionResult']['result']:
        dict = {}
        dict['companyFullName'] = i['companyFullName']
        dict['positionId'] = i['positionId']
        dict['district'] = i['district']
        dict['salary'] = i['salary']
        dict['createTime'] = i['createTime']
        dict['workYear'] = i['workYear']
        dict['companySize'] = i['companySize']
        dict['positionName'] = i['positionName']
        jobList.append(dict)
    return jobList
#去重

def filt(list1):
    jobList = []
    jobList.append(list1[0])
    for i in list1:
        k = 0
        for j in jobList:
            if i['positionId'] != j['positionId'] : k +=1
            else:break
            if k==len(jobList):jobList.append(i)
    return jobList
'''
解析api返回值,拼接成邮箱需要的表格html字符串
'''
def parseInfo(jobList):
    # print(jobList)
    #拼接成html
    h = ''
    for p in jobList:
        desc = str(getPositionDesc(p['positionId']).decode('utf-8')).replace('\n\n','\n').replace('\n','<br />')
        detail = str(p['companyFullName'])+'——'+str(p['positionName'])+'——'+str(p['district'])+'——'+str(p['companySize'])+'——'+str(p['workYear'])+'——'+str(p['createTime'])+'<br />'+desc
        h += '<tr><td><a href="#'+str(p['positionId'])+'">'+str(p['companyFullName'])+\
        '</a></td><td>'+str(p['positionName'])+'</td><td>'+str(p['companySize'])+'</td><td>'+\
                str(p['workYear'])+'</td><td>'+str(p['district'])+'</td><td>'+str(p['salary'])+\
        '</td><td>'+str(p['createTime'])+'</td></tr><tr class="a" id="'+str(p['positionId'])+\
        '"><td colspan=7>'+detail+'</td></tr>'
        
    return h
#获取职位详情
def getPositionDesc(posId):
    response = requests.get('https://m.lagou.com/jobs/'+str(posId)+'.html',headers=headers)
    content = bs4.BeautifulSoup(response.content, "lxml")
    # print(content)
    c = content.find(class_="job_bt").find('div').get_text().encode('utf-8')

    # return content.find('dd', class_="job_bt").find('div').get_text().encode('utf-8')
    return c



# 发送通知邮件
def sendMail(text):
    # print("html:")
    # print(text)
    print(text)

    sender = '13990122270@163.com'
    # receiver = ['462037754@qq.com']
    receiver = ['738631563@qq.com']
    mailToCc = ['ltinghuang@163.com'] #抄送
    subject = '职位通知'
    smtpserver = 'smtp.163.com'
    username = '13990122270@163.com'
    password = 'qwertyuioplmn123'
    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    try:
        smtp = smtplib.SMTP(smtpserver)
        #smtp = smtplib.SMTP(smtpserver)
        # smtp.docmd("EHLO server")
        # smtp.starttls()
        # smtp.EnableSsl = True
        # smtp.set_debuglevel(1)
        #smtp.connect(smtpserver,'465')
        # smtp.docmd("AUTH LOGIN")
        smtp.login(username, password)
        smtp.sendmail(sender, receiver + mailToCc, msg.as_string())
        #logging.error('email success!!!!!!!!!!')
        smtp.quit()
        return True
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        #logging.error('email wrong')
        return None



if __name__ == '__main__':
    #logging.error('Main start')
    print('---begin---')
    para = {'first': 'true', 'pn': '1', 'kd': kd, 'city': city,'gj':'1-3年'}
    html = getInfo(url, para)   # 获取原始接口返回值,拼接成邮箱需要的表格html字符串
    flag = sendMail(html)   #发送至邮箱
    if flag : print('%s爬取成功' % city)
    else : print('%s爬取失败' % city)