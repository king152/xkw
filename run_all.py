'''
Created on 2019年5月16日
@author: king
@job number:xy04952
'''
# coding:utf-8
import unittest
import HTMLTestRunner_cn
import time


global report_path

now=time.strftime("%Y-%m-%d_%H_%M_%S")
report_path = './Report/'+now+'_result.html'
case_path='./case/'

# 用例路径
#case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
#     print(discover)
    return discover



if __name__ == "__main__":
 
    fp = open(report_path, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(title="测试报告", 
                                              description="学科网首页", 
                                              stream=fp, 
                                              verbosity=2, 
                                              retry=1, 
                                              save_last_try=True)
    runner.run(all_case())
    fp.close()