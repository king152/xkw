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

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        creatdirectory.deletefile()
        creatdirectory.checkdirectory()
        cls.imges=[]
    
    def test_01(self):
        '''正常登录成功用例场景'''
        homePage.login()
        pagetitle=xkwBaseUtil.get_page_title()
        try:
            self.assertEqual(u'学科网-海量中小学教育资源共享平台、权威教学资源门户网站！',pagetitle)
        except Exception as e:
            self.imges.append(xkwBaseUtil.add_img())
            print(e)
            raise
    
    def test_download_free_file(self):
        '''下载免费资源第一条资源'''
        filename = homePage.DownloadFile(u'免费')
        downloadfilename = creatdirectory.get_dir_filename()
        try:
            self.assertIn(downloadfilename,filename)
        except Exception as e:
            self.imges.append(xkwBaseUtil.add_img())
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise

    def test_download_pay_file(self):
        '''下载普通资源第一条资源'''
        Flag = homePage.DownloadFile(u'普通')
        try:
            self.assertTrue(Flag)
        except Exception as e:
            self.imges.append(xkwBaseUtil.add_img())
            print(e)
            xkwBaseUtil.get('http://www.zxxk.com/')
            raise    
    
    @classmethod
    def tearDownClass(cls):
        xkwBaseUtil.close()

if __name__ == "__main__":
    unittest.main()
