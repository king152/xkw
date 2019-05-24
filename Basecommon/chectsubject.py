'''
Created on 2019年5月24日
@author: king
@job number:xy04952
'''
#coding=utf-8

from Basecommon.xkw_basecommon import xkwBaseUtil
import requests

global softid 
softid = []

def writefile(id):
    with open('1.txt', 'a+', encoding = 'utf-8') as fp:
        fp.write(id+'\n')

def getsoftid():
    url = "http://uslo.zxxk.com/api/commend/schedule"
    querystring = {"class":"563","chapter":"1080","node":"3706","sort":"download%2C-1","pagenum":"1","pagesize":"10"}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "uslo.zxxk.com",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    for i in range(len(res['data'])):
        softid.append(res['data'][i]['softid'])
        writefile(str(res['data'][i]['softid']))



getsoftid()
xkwBaseUtil.set_driver('谷歌')
xkwBaseUtil.maximize_window()
for id in softid:
    base_url = 'http://www.zxxk.com/soft/'+str(id)+'.html'
    xkwBaseUtil.get(base_url)
    try:
        text1 = xkwBaseUtil.find_element_by_link_text(u'学科网').text
        text2 = xkwBaseUtil.find_element_by_link_text(u'高中数学').text
        text3 = xkwBaseUtil.find_element_by_link_text(u'必修一').text
        text4 = xkwBaseUtil.find_element_by_link_text(u'人教A版').text
        text5 = xkwBaseUtil.find_element_by_link_text(u'第一章 集合与函数的概念').text
        text6 = xkwBaseUtil.find_element_by_link_text(u'1.1 集合').text
        print('请求URL为：%s  本次softid版本信息：%s > %s > %s > %s > %s > %s'%(base_url,text1,text2,text3,text4,text5,text6))
    except Exception as e :
        print(e)
    xkwBaseUtil.sleep(3)
print('******softID请求校验完成，关闭浏览器*****')
xkwBaseUtil.close()