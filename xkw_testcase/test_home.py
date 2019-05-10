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
import HTMLTestReport
import time

class Mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        creatdirectory.deletefile()
        creatdirectory.checkdirectory()
    
    def test_login(self):
        '''正常登录成功用例场景'''
        homePage.login()
        pagetitle=xkwBaseUtil.get_page_title()
        try:
            self.assertEqual(u'学科网-海量中小学教育资源共享平台、权威教学资源门户网站！',pagetitle)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_download(self):
        '''随机下载资源用例'''
        filename = homePage.DownloadFile()
        xkwBaseUtil.sleep(10)
#         downloadfilename = creatdirectory.get_dir_filename()
        downloadfilename = homePage.getfilename()
        try:
            self.assertEqual(filename,downloadfilename)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise
    
    
    @classmethod
    def tearDownClass(cls):
        xkwBaseUtil.close()

if __name__ == "__main__":
    '''生成测试报告'''
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Mytest("test_login"))
    testunit.addTest(Mytest("test_download"))
    report_path = "..\\Report\\xkwTestReport_" + current_time  + '.html'  #生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化测试报告",description='自动化测试报告',tester='king')
    runner.run(testunit)
    fp.close()