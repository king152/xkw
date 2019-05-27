'''
Created on 2019年5月27日
@author: king
@job number:xy04952
'''
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.homepage import homePage
from Basecommon.autocode import autocode
from test.test_typing import XK

class UserInfo:
    def __init__(self):
        pass
    
    #获取当前学豆
    def getbean(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        beanNum = xkwBaseUtil.find_element_by_id('beanNum').text
        return int(beanNum)
    
    #获取打卡结果
    def clockresult(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.scrollelment('xpath', '//*[@id="lesson-sign"]/div[2]/a[1]')
        xkwBaseUtil.sleep(2)
        result = xkwBaseUtil.find_element_by_xpath('//*[@id="lesson-sign"]/div[3]/span[2]/a[4]').text
        return result
    
    #签到
    def signin(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_class_name('btn-checkin').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_xpath('//*[@id="modalSignin"]/i').click()
    
    #打卡    
    def clock(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.scrollelment('xpath', '//*[@id="lesson-sign"]/div[2]/a[1]')
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_xpath('//*[@id="lesson-sign"]/div[2]/a[1]').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_xpath('//*[@id="selectGroup"]/div[1]/ul/li[1]/a').click() #初始化到学段
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="selectGrade"]/a[2]').click() #选择高中同步
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="selectSubject"]/a[3]').click() #选择数学
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="step3"]/div/a[11]').click() #选择高考
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="step3"]/div[3]/a[1]').click() #选择高考真题
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="modalClockin"]/i').click() #关闭打卡成功页面
    
    #提交评价    
    def evaluate(self,contents):
        xkwBaseUtil.get('http://user.zxxk.com/ConsumeLog/list?listtype=1')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_class_name('speed-seconds').click()
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_class_name('five-stars').click()
        xkwBaseUtil.find_element_by_xpath('//*[@class="topspeed"]/div[2]/div/div[2]/ul/li[1]/a').click()
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@class="topspeed"]/div[2]/div/div[2]/ul/li[2]/a').click()
        xkwBaseUtil.sleep(1)
        if len(contents):
            xkwBaseUtil.find_element_by_id('discussContent').send_keys(contents)
            xkwBaseUtil.sleep(2)
        else:
            pass
        xkwBaseUtil.find_element_by_class_name('speed-btn').click()
        xkwBaseUtil.sleep(2)
        content = xkwBaseUtil.get_alert_content()
        xkwBaseUtil.sleep(3)
        xkwBaseUtil.alert_accept()
        return content
    
    #获取评价后提交评价按钮标签    
    def get_evaluate(self):
        return xkwBaseUtil.find_element_by_class_name('ypj').text
    
    #绑定微信
    def bindwx(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_id('bind-wx').click()
        xkwBaseUtil.sleep(3)
        xkwBaseUtil.switch_to_frame('id','iframe')
        title = xkwBaseUtil.find_element_by_class_name('title').text
        xkwBaseUtil.logout_iframe()   
        return title
    
    #绑定邮箱
    def bindemail(self):
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_id('bind-email').click()
        xkwBaseUtil.sleep(3)
        xkwBaseUtil.find_element_by_class_name('email-address').send_keys('1694380821@qq.com')
        xkwBaseUtil.sleep(3)
        code = xkwBaseUtil.get_VerificatCodepic('captcha')
        xkwBaseUtil.find_element_by_class_name('vcode').send_keys(code)
        xkwBaseUtil.find_element_by_class_name('send').click()
        xkwBaseUtil.sleep(3)
        content = xkwBaseUtil.find_element_by_class_name('cover-email').text
        return content
        
               

userinfo = UserInfo()
homePage.login()
print(userinfo.bindemail())


