'''
Created on 2019年5月31日
@author: king
@job number:xy04952
'''
import requests
from threading import Thread

global relist

relist = []

def writefile(id):
    with open('time.txt', 'a+', encoding = 'utf-8') as fp:
        fp.write(id+'\n')
    fp.close()
        
class MyThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.url = "http://uslo.zxxk.com/think/schedule/school/version"
        self.querystring = {"subjectid":"12","gradeid":"11","schoolid":"26824"}
        self.headers = {
                'User-Agent': "PostmanRuntime/7.13.0",
                'Accept': "*/*",
                'Cache-Control': "no-cache",
                'Host': "uslo.zxxk.com",
                'accept-encoding': "gzip, deflate",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
                }
        
    def run(self):
        while True:
            try:
                response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
                writefile(str(response.elapsed.total_seconds()))
                #print(response.elapsed.total_seconds())
            except Exception as e :
                print(e)
    
def creat_thread():
    for i in range(100):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    creat_thread()