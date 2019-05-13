'''
Created on 2019年5月8日

@author: king
@number:xy04952
'''
#-*-encoding:utf-8-*-


from selenium import webdriver
import unittest
import HTMLTestReport
import time
import configparser


class Mytest(unittest.TestCase):

    def setUp(self):
        config=configparser.ConfigParser()
        config.read('..//conf//data.conf', 'utf-8')
        self.MobilePhone=config.get("LoginAccount","MobilePhone")
        self.pwd=config.get("LoginAccount","Password")
        self.driver = webdriver.Chrome()  
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://www.baidu.com/"
        self.driver.get(self.base_url)
        
    def test_case1(self):
        self.driver.find_element_by_class_name('icon-guanbi').click()
        self.driver.find_element_by_class_name('login-btn').click()
        self.driver.find_element_by_class_name('lcon-weixin').click()
        self.driver.find_element_by_id('username').clear()
        self.driver.find_element_by_id('username').send_keys(self.MobilePhone)
        self.driver.find_element_by_class_name('psd').clear()
        self.driver.find_element_by_class_name('psd').send_keys(self.pwd)
        self.driver.find_element_by_id('CommonLogin').submit()
        Username=self.driver.find_element_by_class_name('user-btn').text
        self.assertEqual('xy049521', Username)
        pic_directory=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '../Report/image/'+pic_directory+'/' + current_time +'.png'
        print(pic_path)
        self.driver.save_screenshot(pic_path)    
    

    def test_case2(self):
        '''设计测试失败case'''
        print ("========【case_0002】打开百度搜索 =============")
        try:
            self.assertEqual('百度一下，你就知道',self.driver.title)
        except Exception as e:
            pic_directory=time.strftime("%Y-%m-%d", time.localtime(time.time()))
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = '../Report/image/'+pic_directory+'/' + current_time +'.png'
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(e)
            raise
        


   

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    '''生成测试报告'''
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Mytest("test_case2"))
    #testunit.addTest(Baidu("test_case2"))
    #testunit.addTest(Baidu("test_case3"))
    report_path = "..\\Report\\xkwTestReport_" + current_time  + '.html'  #生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化测试报告",description='自动化测试报告',tester='king')
    runner.run(testunit)
    fp.close()

