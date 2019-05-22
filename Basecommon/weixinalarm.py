'''
Created on 2019年5月22日
@author: king
@job number:xy04952
'''

import urllib.request
import json
import configparser

class weixinAlarm:
    def __init__(self):
        self.url = 'https://qyapi.weixin.qq.com'
        config=configparser.ConfigParser()
        config.read('E:\\pythonscript\\xkw.zxxk\\conf\\data.conf', 'utf-8')
        self.corpid=config.get("weixinconf","corpid")
        self.corpsecret=config.get("weixinconf","corpsecret")
    
    def get_token(self):
        try:
            self.token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.url,self.corpid,self.corpsecret)
            self.token = json.loads(urllib.request.urlopen(self.token_url).read().decode())['access_token']
            return self.token
        except Exception as e :
            print(e)


    def send_message_text(self,token, msg):
        try:
            values = {
            "touser": '@all',
            "msgtype": 'text',
            "agentid": 1000002, 
            "text": {'content': msg},
            "safe": 0
            }
            msges=(bytes(json.dumps(values), 'utf-8'))
            send_url = '%s/cgi-bin/message/send?access_token=%s' % (self.url,token)
            respone=urllib.request.urlopen(urllib.request.Request(url=send_url, data=msges)).read()
            x = json.loads(respone.decode())['errcode']
            if x == 0:
                print ('Succesfully')
            else:
                print ('Failed')
        except Exception as e:
            print(e)

weixinalarm=weixinAlarm()
            