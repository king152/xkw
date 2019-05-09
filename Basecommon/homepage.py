'''
Created on 2019年5月9日
@author: king
@job number:xy04952
'''
import configparser
from Basecommon.xkw_basecommon import xkwBaseUtil

class HomePage:
    
    #init data
    def __init__(self):
        config=configparser.ConfigParser()
        config.read('..//conf//data.conf', 'utf-8')
        self.MobilePhone=config.get("LoginAccount","MobilePhone")
        self.pwd=config.get("LoginAccount","Password")
    
    #login system
    def login(self):
        xkwBaseUtil.set_driver('谷歌')
        xkwBaseUtil.maximize_window()
        xkwBaseUtil.get('http://www.zxxk.com/')
        xkwBaseUtil.find_element_by_class_name('icon-guanbi').click()
        xkwBaseUtil.find_element_by_class_name('login-btn').click()
        xkwBaseUtil.find_element_by_class_name('lcon-weixin').click()
        xkwBaseUtil.find_element_by_id('username').clear()
        xkwBaseUtil.find_element_by_id('username').send_keys(self.MobilePhone)
        xkwBaseUtil.find_element_by_class_name('psd').clear()
        xkwBaseUtil.find_element_by_class_name('psd').send_keys(self.pwd)
        xkwBaseUtil.find_element_by_id('CommonLogin').submit()
        xkwBaseUtil.sleep(5)
    
    #search soucrce
    def search(self,keys):
        pass
    
    # Random Download of the First Free Document in Mathematics
    def DownloadFile(self):
        pass

homePage=HomePage()        
         
        