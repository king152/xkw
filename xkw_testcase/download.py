'''
Created on 2019年5月15日
@author: king
@job number:xy04952
'''
import re
import time


global url_download_page

url_download_page = 'chrome://downloads/'

def verify_download(self,file_title):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("打开浏览器下载窗口")
        self.browser.get(url_download_page)
        time.sleep(10)

        download_page_file_title = self.browser.execute_script('let manager = document.querySelector("downloads-manager").shadowRoot;let ironList = manager.querySelector("iron-list");let downloadItem = ironList.querySelector("downloads-item").shadowRoot;var input=downloadItem.querySelector("#title-area #file-link").innerText;return input')


        print("下载窗口里的文件标题是")
        print(download_page_file_title)
        print("检验二者是否是一个文件") 
        if re.findall(file_title,download_page_file_title):
            print ("确认文件已下载，over，撤退")    
            print("")
        else:
            print("没有下载成功，请确认下载服务器是否出现问题！")
            print("")
        time.sleep(3)
        pass

