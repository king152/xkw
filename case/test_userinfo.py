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
        print('用户中心case开始执行')
     
    def test_100(self):
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
    
    def test_1001(self):
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
        
    def test_1002(self):
        ''' 打卡成功，验证打卡进度'''
        clonkreslut = userinfo.clockresult()
        try:
            self.assertEqual(clonkreslut, u'高考真题')
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_1003(self):
        '''提交带评论内容的评价'''
        content = userinfo.evaluate(u'资源非常不错，结构清晰，排版漂亮')
        try:
            self.assertEqual(content, u'评价成功，您的评论内容将在审核通过后显示！')
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    def test_1004(self):
        '''提交无评论内容的评价'''
        content = userinfo.evaluate('')
        try:
            self.assertEqual(content, u'评价成功！')
        except Exception as e:
            xkwBaseUtil.get_screenshot()
            print(e)
            raise
    
    @classmethod
    def tearDownClass(cls):
        print('用户中心case执行完毕')
 
if __name__ == "__main__":
    unittest.main()       