'''
Created on 2019年5月16日
@author: king
@job number:xy04952
'''
# coding:utf-8
import unittest
import HTMLTestRunner_cn
import time
from Basecommon.autosendmail import sendmail


global report_path
global case_path

now=time.strftime("%Y-%m-%d_%H_%M_%S")
reportfile = '学科网自动化回归_'+now+'_result.html'
report_path = './Report/'+ reportfile #报告路径
case_path='./case/'  #用例路径

#discover组装用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    return discover

if __name__ == "__main__":
    fp = open(report_path, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(title="学科网首页自动化回归测试报告", 
                                              description="学科网首页自动化回归测试报告，详情见附件", 
                                              stream=fp, 
                                              verbosity=2, 
                                              retry=1, 
                                              save_last_try=True)
    runner.run(all_case())
    fp.close()
    sendmail.sendEmail(report_path,reportfile)