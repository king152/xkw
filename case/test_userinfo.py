'''
Created on 2019年5月27日
@author: king
@job number:xy04952
'''
import sys
sys.path.append("..")
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.userinfo import userinfo
import unittest

class testuserCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def test_01_signin(self):
        '''签到成功，验证学豆'''
        beforebean = userinfo.getbean()
        userinfo.signin()
        xkwBaseUtil.sleep(3)
        afterbean = userinfo.getbean()
        try:
            self.assertEqual(beforebean+3, afterbean)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_clonk_05(self):
        '''打卡成功，验证打卡学豆'''
        beforebean = userinfo.getbean()
        userinfo.clock()
        xkwBaseUtil.sleep(3)
        afterbean = userinfo.getbean()
        try:
            self.assertEqual(beforebean+5, afterbean)
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
        
    def test_clonk_06(self):
        ''' 打卡成功，验证打卡进度'''
        clonkreslut = userinfo.clockresult()
        try:
            self.assertEqual(clonkreslut, u'高考真题')
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    @classmethod
    def tearDownClass(cls):
        pass
 
if __name__ == "__main__":
    unittest.main()       