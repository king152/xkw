'''
Created on 2019年5月9日
@author: king
@job number:xy04952
'''
import sys
sys.path.append("..")
from Basecommon.homepage import homePage
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.checkmkdir import creatdirectory
import unittest

global JS

JS = 'let manager = document.querySelector("downloads-manager").shadowRoot; \
    let ironList = manager.querySelector("iron-list");\
    let downloadItem = ironList.querySelector("downloads-item").shadowRoot;\
    var input=downloadItem.querySelector("#title-area #file-link").innerText;\
    return input'

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #creatdirectory.deletefile()
        creatdirectory.checkdirectory()
        cls.imges=[]
    
    def test_01_logon(self):
        '''正常登录成功用例场景'''
        homePage.login()
        pagetitle=xkwBaseUtil.get_page_title()
        try:
            self.assertEqual(u'学科网-海量中小学教育资源共享平台、权威教学资源门户网站！',pagetitle)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_download_free_file_02(self):
        '''下载免费资源第一条资源'''
        filename = homePage.DownloadFile(u'免费')
        xkwBaseUtil.get('chrome://downloads/')
        xkwBaseUtil.sleep(5)
        downloadfilename = xkwBaseUtil.execute_js_text(JS)
        try:
            self.assertIn(filename,downloadfilename)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise

    def test_download_pay_file_03(self):
        '''下载普通资源第一条资源'''
        Flag = homePage.DownloadFile(u'普通')
        try:
            self.assertTrue(Flag)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise    
    
    @classmethod
    def tearDownClass(cls):
        pass
        #xkwBaseUtil.close()

if __name__ == "__main__":
    unittest.main()
