'''
Created on 2019年5月15日
@author: king
@job number:xy04952
'''
import sys
from win32comext.shell.test.testShellFolder import num
sys.path.append("..")
from Basecommon.homepage import homePage
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.checkmkdir import creatdirectory
import unittest
import HTMLTestReport
import time
import re

global url_download_page
global JS

url_download_page = 'chrome://downloads/'
JS = 'let manager = document.querySelector("downloads-manager").shadowRoot;let ironList = manager.querySelector("iron-list");\
   let downloadItem = ironList.querySelector("downloads-item").shadowRoot;\
   var input=downloadItem.querySelector("#title-area #file-link").innerText;\
   return input'

class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        creatdirectory.deletefile()
        creatdirectory.checkdirectory()
    
    def test_01(self):
        '''正常登录成功用例场景'''
        homePage.login()
        pagetitle=xkwBaseUtil.get_page_title()
        try:
            self.assertEqual(u'学科网-海量中小学教育资源共享平台、权威教学资源门户网站！',pagetitle)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_download_free_file(self):
        '''下载免费资源第一条资源'''
        filename = homePage.DownloadFile(u'免费')
        xkwBaseUtil.get(url_download_page)
        xkwBaseUtil.sleep(5)
        downloadfilename = xkwBaseUtil.execute_js_downloadfile(JS)
        print(downloadfilename) 
        try:
            self.assertIn(filename,downloadfilename)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise
# # 
#     def test_download_pay_file(self):
#         '''下载普通资源第一条资源'''
#         Flag = homePage.DownloadFile(u'普通')
#         try:
#             self.assertTrue(Flag)
#         except Exception as e:
#             xkwBaseUtil.get_screenshot()
#             print(e)
#             xkwBaseUtil.get('http://www.zxxk.com/')
#             raise    
#     
    @classmethod
    def tearDownClass(cls):
        xkwBaseUtil.close()

def testcase():
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_01"))
    suite.addTest(Mytest("test_download_free_file")) 
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

for num in range(10):
    try :
        testcase()
        time.sleep(10)
        print(num)
    except Exception as e:
        print(e)
