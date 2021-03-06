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
        xkwBaseUtil.sleep(2)
    
    #search soucrce
    def search(self,keys):
        pass

    def downfile(self):
        xkwBaseUtil.get('http://sx.zxxk.com/h/jc-book554/?level=1')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_link_text(u"下载").click()
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.switch_windows_handle()
        pagetile = xkwBaseUtil.get_page_title()
        xkwBaseUtil.find_element_by_xpath('//*[@id="btnSoftDownload"]/div/span[1]').click()
        xkwBaseUtil.sleep(20)
        return pagetile.strip(u'-学科网')
        

    
    # Random Download of the First Free Document in Mathematics
    def DownloadFile(self,level):
        xkwBaseUtil.get('http://sx.zxxk.com/jc-book554/')
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_link_text(level).click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_link_text(u"下载").click()
        xkwBaseUtil.switch_windows_handle()
        pagetile = xkwBaseUtil.get_page_title()
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_xpath('//*[@id="btnSoftDownload"]/div/span[1]').click()
        xkwBaseUtil.sleep(20)
        try:
            if level==u'免费':
                return pagetile.strip(u'-学科网')
            else:
                xkwBaseUtil.sleep(5)
                elementisExists = xkwBaseUtil.is_exist_element('#layui-layer-iframe2')
                return elementisExists
        except Exception as e:
            print(e)
    
    def getfilename(self):
        xkwBaseUtil.get('chrome://downloads/')
        xkwBaseUtil.sleep(5)
        filename = xkwBaseUtil.find_element_by_id('file-link')
        print(filename)
        return filename
        
homePage=HomePage()