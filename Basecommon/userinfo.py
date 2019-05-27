'''
Created on 2019年5月27日
@author: king
@job number:xy04952
'''
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.homepage import homePage

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
               
userinfo = UserInfo()
