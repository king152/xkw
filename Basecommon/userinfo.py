'''
Created on 2019年5月27日
@author: king
@job number:xy04952
'''
from Basecommon.xkw_basecommon import xkwBaseUtil
from Basecommon.homepage import homePage
import os
from Basecommon.Executablefile.getdir import getDir
from random import randint


class UserInfo:
    def __init__(self):
        pass
    
    #获取当前学豆
    def getbean(self):
        '''
        #返回学豆
        return int(beanNum)
        '''
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        beanNum = xkwBaseUtil.find_element_by_id('beanNum').text
        return int(beanNum)
    
    #获取打卡结果
    def clockresult(self):
        '''
        return result
        #返回打卡进度信息
        '''
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.scrollelment('xpath', '//*[@id="lesson-sign"]/div[2]/a[1]')
        xkwBaseUtil.sleep(2)
        result = xkwBaseUtil.find_element_by_xpath('//*[@id="lesson-sign"]/div[3]/span[2]/a[4]').text
        return result
    
    #签到
    def signin(self):
        '''
        #进行签到，无返回值
        '''
        xkwBaseUtil.get('http://user.zxxk.com/userbean/usertask')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_class_name('btn-checkin').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_xpath('//*[@id="modalSignin"]/i').click()
    
    #打卡    
    def clock(self):
        '''
        #进行打卡，无返回值
        
        '''
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
        '''
        content:提交评价成功后获取的alert的文本内容
        return content
        
        '''
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
        '''
        #返回资源评价后标签按钮名称：已评价
        '''
        return xkwBaseUtil.find_element_by_class_name('ypj').text
    
    #绑定微信
    def bindwx(self):
        '''
        title 微信二维码区域上方标题
        return title
        '''
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
        '''
        return content
        content:发送激活邮件页面发送信息  例如：已发送验证邮件至：1694****@qq.com
        '''
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
    
    #获取我的资产信息
    def userasset(self):
        '''
        #获取我的资产信息
        Point :普通点
        advPoint: 高级点
        storedPoint：储值
        moneyPoint：现金
        
        return [Point,advPoint,storedPoint,moneyPoint]
        
        '''
        xkwBaseUtil.get('http://user.zxxk.com/Userinfo/userasset')
        xkwBaseUtil.sleep(5)
        Point = xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/div/div[1]/div/div[1]/div[2]/div/div[1]/a').text
        advPoint =xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/div/div[1]/div/div[1]/div[2]/div/div[2]/a').text
        storedPoint = xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/div/div[1]/div/div[1]/div[2]/div/div[3]/a').text
        moneyPoint = xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/div/div[1]/div/div[1]/div[2]/div/div[4]/a').text
        return [Point,advPoint,storedPoint,moneyPoint]            
    
    #将储值转换成普通点，返回普通点总数
    def userassettoPoint(self):
        '''
        Pointnumber :普通点与储值转换为普通点的总数
        return Pointnumber
        '''
        pointlist = self.userasset()
        Pointnumber = float(pointlist[0])+float(pointlist[2])*5
        return Pointnumber
    
    def uploadfile(self):
        '''
        #上传资源
        return text_reslut 
        text_reslut 上传成功页面提示信息
        '''
        text_string = u'学科网用户中心自动化回归测试文件上传，请忽略'
        xkwBaseUtil.get('http://user.zxxk.com/upload-doc/')
        xkwBaseUtil.sleep(5)
        xkwBaseUtil.find_element_by_id('chooseFile').click()
        xkwBaseUtil.sleep(3)
        excefile = getDir()+'\\'+'uploadfile.exe'
        #print(excefile)
        os.system(excefile)
        #选择类别
        xkwBaseUtil.find_select('//*[@id="datas-list"]/filelist/div/div[1]/div/div[1]', \
                                 '//*[@id="datas-list"]/filelist/div/div[1]/div/div[2]/ul[1]/li[2]/span')
        xkwBaseUtil.sleep(1)
        #选择年级 高三
        xkwBaseUtil.find_select('//*[@id="datas-list"]/resource/div[3]/div[1]/div/div[1]', \
                                 '//*[@id="datas-list"]/resource/div[3]/div[1]/div/div[2]/ul/li[2]/span')
        xkwBaseUtil.sleep(1)
        #选择学科 数学
        xkwBaseUtil.find_select('//*[@id="datas-list"]/resource/div[3]/div[2]/div/div[1]', \
                                 '//*[@id="datas-list"]/resource/div[3]/div[2]/div/div[2]/ul/li[3]/span')
        xkwBaseUtil.sleep(1)
        #选择栏目
        xkwBaseUtil.find_element_by_class_name('select-category').click()
        xkwBaseUtil.sleep(2)
        #栏目选择框 选择高中竞赛
        xkwBaseUtil.find_element_by_class_name('tree1-name').click()
        xkwBaseUtil.sleep(1)
        #选择教学指导
        xkwBaseUtil.find_element_by_css_selector('#treeRoot > li.tree1.show > ul > li:nth-child(1) > div > a').click()
        xkwBaseUtil.sleep(2)
        #栏目选择页面点击确定
        xkwBaseUtil.find_element_by_id('confirmClass').click()
        xkwBaseUtil.sleep(2)
        #选择学校
        js = 'document.getElementById("selectArea").removeAttribute("readonly");'
        xkwBaseUtil.execute_js(js)
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_id('selectArea').send_keys(u'东直门中学')
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.scroll_to_top_or_bottom(u'底部')
        xkwBaseUtil.sleep(3)
        #选择地区 北京
        xkwBaseUtil.find_select('//*[@id="datas-list"]/resource/div[5]/div[2]/div[1]', \
                                 '//*[@id="datas-list"]/resource/div[5]/div[2]/div[2]/ul/li[2]/span')
        xkwBaseUtil.sleep(1)
        xkwBaseUtil.find_element_by_xpath('//*[@id="datas-list"]/resource/div[6]/textarea').send_keys(text_string)
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_id('sub').click()
        text_reslut = xkwBaseUtil.find_element_by_xpath('xpath') #获取上传结果
        return text_reslut
    
    def Userinfosetup(self):
        '''
        #获取用户基本信息
        return [name,birthday,address]
        name 真实姓名
        birthday 生日
        address 详细地址
        '''
        jsbirthday = 'document.getElementById("birthday").value="1991-08-10";'
        jsArea = 'document.getElementById("selectArea").value="北京市-北京市-西城区";'
        xkwBaseUtil.get('https://sso.zxxk.com/user/uc#/user/uc/getUserInfo')
        xkwBaseUtil.sleep(3)
        xkwBaseUtil.find_element_by_name('realName').clear()
        xkwBaseUtil.sleep(3)
        xkwBaseUtil.find_element_by_id('realName').send_keys(u'学科网王勇')
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_xpath('//*[@id="sexDiv"]/label[2]/input').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.execute_js(jsbirthday)
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.execute_js(jsArea)
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_id('address').clear()
        xkwBaseUtil.find_element_by_id('address').send_keys(u'学科网首发物流')
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_id('save').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.find_element_by_class_name('layui-layer-btn0').click()
        
        #获取提交的信息
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.get('https://sso.zxxk.com/user/uc#/user/uc/getUserInfo')
        name = xkwBaseUtil.find_element_by_id('realName').get_attribute('value')
        birthday = xkwBaseUtil.find_element_by_id('birthday').get_attribute('value')
        address = xkwBaseUtil.find_element_by_id('address').get_attribute('value')
        return [name,birthday,address]
    
    def professInfo(self,infotype):
        '''
        #身份信息
        infotype 输入值为：教师 、学生、家长
        return [userinfo,subject,stage,version]
        userinfo 用户身份 
        subject  学科
        stage   年级
        version  教材版本
        '''
        xkwBaseUtil.get('https://sso.zxxk.com/user/uc#/user/uc/professionSetup')
        xkwBaseUtil.sleep(5)
        if infotype == u'教师':
            #选择教师
            elements = xkwBaseUtil.find_element_by_class_names('radio-inline')
            elements[0].click() 
            xkwBaseUtil.sleep(2)
            #选择高中
            xkwBaseUtil.find_element_by_xpath('//*[@id="stageId"]/a[3]').click()
            xkwBaseUtil.sleep(2)
            #选择高三
            xkwBaseUtil.find_element_by_xpath('//*[@id="gradeId"]/a[3]').click()
            xkwBaseUtil.sleep(2)
            #选择高中数学
            xkwBaseUtil.find_element_by_xpath('//*[@id="subjects"]/a[2]').click()
            xkwBaseUtil.sleep(2)
            
            #教材版本
            xkwBaseUtil.find_element_by_class_name('single').click()
            El = xkwBaseUtil.find_element_by_class_names('option')
            El[0].click()
            xkwBaseUtil.sleep(2)
            xkwBaseUtil.find_element_by_id('saveBtn').click()
            xkwBaseUtil.sleep(2)
            xkwBaseUtil.find_element_by_class_name('layui-layer-btn0').click()
            xkwBaseUtil.sleep(2)
        
            #获取选择结果            
            xkwBaseUtil.get('http://user.zxxk.com/userinfo/userinfo')
            xkwBaseUtil.sleep(2)
            
            userinfo = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[1]/span').text
            subject = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[2]/span').text
            stage = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[3]/span').text
            version = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[4]/span').text
            return [userinfo,subject,stage,version]
        elif infotype == u'学生':
            #选择学生
            elements = xkwBaseUtil.find_element_by_class_names('radio-inline')
            elements[1].click() 
            xkwBaseUtil.sleep(2)
            #选择高中
            xkwBaseUtil.find_element_by_xpath('//*[@id="stageId"]/a[2]').click()
            xkwBaseUtil.sleep(2)
            #选择八年级
            xkwBaseUtil.find_element_by_xpath('//*[@id="gradeId"]/a[3]').click()
            xkwBaseUtil.sleep(2)
            
            xkwBaseUtil.find_element_by_id('saveBtn').click()
            xkwBaseUtil.sleep(2)
            xkwBaseUtil.find_element_by_class_name('layui-layer-btn0').click()
            xkwBaseUtil.sleep(2)
            
            #获取选择结果            
            xkwBaseUtil.get('http://user.zxxk.com/userinfo/userinfo')
            xkwBaseUtil.sleep(2)
            
            userinfo = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[1]/span').text
            stage = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[2]/span').text
            return [userinfo,stage]
        elif infotype==u'家长':
            #选择家长
            elements = xkwBaseUtil.find_element_by_class_names('radio-inline')
            elements[0].click() 
            xkwBaseUtil.sleep(2)
            #选择小学
            xkwBaseUtil.find_element_by_xpath('//*[@id="stageId"]/a[1]').click()
            xkwBaseUtil.sleep(2)
            #选择五年级
            xkwBaseUtil.find_element_by_xpath('//*[@id="gradeId"]/a[5]').click()
            xkwBaseUtil.sleep(2)
            xkwBaseUtil.find_element_by_id('saveBtn').click()
            xkwBaseUtil.sleep(2)
            xkwBaseUtil.find_element_by_class_name('layui-layer-btn0').click()
            xkwBaseUtil.sleep(2)
            
            #获取选择结果            
            xkwBaseUtil.get('http://user.zxxk.com/userinfo/userinfo')
            xkwBaseUtil.sleep(2)
            
            userinfo = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[1]/span').text
            stage = xkwBaseUtil.find_element_by_xpath('//*[@id="detailInfo"]/div/div/div[2]/div[1]/div[2]/span').text
            return [userinfo,stage]
        else:
            print('infotype can only input 教师、学生、家长！ ')
            return None
    
    def userOrder(self,ordertype):
        '''
        #功能：提交包月会员订单或者充值订单 返回相关订单号
        #参数 ordertype  订单类型  包括：cash 充值    monthly包月会员订单
        #返回值  return order_no
        order_no 订单号
        '''
        if ordertype == 'monthly':
            xkwBaseUtil.get('http://paycenter.zxxk.com/monthly')
            xkwBaseUtil.sleep(3)
            xkwBaseUtil.find_element_by_id('submit').click()
            xkwBaseUtil.sleep(5)
            xkwBaseUtil.switch_windows_handle()
            xkwBaseUtil.sleep(2)
            order_no = xkwBaseUtil.find_element_by_class_name('order_no').text
            return order_no
        elif ordertype == 'cash':
            xkwBaseUtil.get('http://paycenter.zxxk.com/pay/cash')
            xkwBaseUtil.sleep(3)
            #提交订单
            xkwBaseUtil.find_element_by_class_name('recharge-btn').click()
            xkwBaseUtil.sleep(5)
            #切换到订单支付页面
            xkwBaseUtil.switch_windows_handle()
            xkwBaseUtil.sleep(2)
            #获取订单号
            order_no = xkwBaseUtil.find_element_by_class_name('order_no').text
            return order_no
        else:
            print('ordertype can only input cash or monthly!')
            return None
        
    def getMyOrder(self,ordertype):
        '''
        #功能：我的订单页面获取提交的订单信息
        #参数 ordertype  订单类型  包括：cash 在线充值订单    monthly包月会员订单
        #返回值  return [orderNo,orderTime,orderPackage,orderMemberState,
        orderEffectDate,orderPay,orderState]
        orderNo 订单号
        orderTime 购买时间
        orderPackage 会员套餐
        orderMemberState 会员状态
        orderEffectDate 有效日期
        orderPay 实付金额
        orderState 订单状态
        
        Online recharge
        return [orderNo,rechargeType,paymentAamount,purchaseTime,
        storedPoint,advPoint,Point,paymentStatus]
        orderNo 订单编号  
        rechargeType 充值类型
        paymentAamount 支付金额
        purchaseTime 购买时间
        Point :普通点
        advPoint: 高级点
        storedPoint：储值
        paymentStatus 支付状态
        '''
        if ordertype == 'monthly':
            xkwBaseUtil.get('http://user.zxxk.com/order/monthlyorder')
            xkwBaseUtil.sleep(3)
            elements = xkwBaseUtil.find_element_by_class_names('state-gray')
            orderNo=elements[0].text
            orderTime = elements[1].text
            orderPackage=elements[2].text
            orderMemberState=elements[3].text
            orderEffectDate=elements[4].text
            orderPay=elements[5].text
            orderState = elements[6].text
            return [orderNo,orderTime,orderPackage,orderMemberState,orderEffectDate,orderPay,orderState]
        elif ordertype == 'cash':
            xkwBaseUtil.get('http://user.zxxk.com/order/payorder')
            xkwBaseUtil.sleep(3)
            #获取订单信息
            elements = xkwBaseUtil.find_element_by_class_names('state-gray')
            orderNo = elements[0].text
            rechargeType = elements[1].text
            paymentAamount = elements[2].text
            purchaseTime = elements[3].text
            storedPoint = elements[4].text
            advPoint = elements[5].text
            Point = elements[6].text
            paymentStatus = elements[7].text
            return [orderNo,rechargeType,paymentAamount,purchaseTime,storedPoint,advPoint,Point,paymentStatus]
        else:
            print('ordertype can only input cash or monthly!')
            return None
    
    def getVoucher(self):
        '''
        Features：领取代金券
        return voucherlist
        voucherlist 已列表返回所有面值
        '''
        voucherlist = []
        xkwBaseUtil.get('http://paycenter.zxxk.com/monthly')
        xkwBaseUtil.sleep(3)
        #领取8元代金券
        xkwBaseUtil.find_element_by_xpath('//*[@class="coupon-list"]/li[1]/div/a').click()
        xkwBaseUtil.sleep(2)
        xkwBaseUtil.get('http://user.zxxk.com/usercoupon/mycoupon')
        xkwBaseUtil.sleep(3)
        el = xkwBaseUtil.find_element_by_class_names('digit')
        for i in range(len(el)):
            voucherlist.append(el[i].text)
        return voucherlist
    
    def myCollect(self):
        '''
        Features：获取我的收藏页面收藏资源的id
        return 返回资料id，已列表返回
        '''
        Idlist=[]
        xkwBaseUtil.get('http://user.zxxk.com/collect/softlist')
        xkwBaseUtil.sleep(3)
        el = xkwBaseUtil.find_element_by_class_names('speed-seconds')
        for i in range(len(el)):
            Idlist.append(el[i].get_attribute('contentid'))
        return Idlist
    
    def cancelCollect(self,softID):
        '''
        Features：取消收藏
        return text
        text 返回取消成功后提示框文本信息
        '''
        xkwBaseUtil.get('http://user.zxxk.com/collect/softlist')
        xkwBaseUtil.sleep(3)
        el = xkwBaseUtil.find_element_by_class_names('speed-seconds')
        print('*****softID****%s'%softID)
        print('*****开始进入判断******')
        for i in range(len(el)):
            xkwBaseUtil.scrollElment(el[i])
            xkwBaseUtil.sleep(3)
            print(el[i].get_attribute('contentid'))
            if el[i].get_attribute('contentid')==softID:
                el[i].click()
                xkwBaseUtil.sleep(1)
                xkwBaseUtil.find_element_by_xpath('//*[@class="topspeed"]/div[2]/div/a[1]').click()
                xkwBaseUtil.sleep(3)
                text = xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/section/div[2]/div[2]/p').text
                xkwBaseUtil.sleep(2)
                xkwBaseUtil.find_element_by_xpath('//*[@id="MainContent"]/section/div[2]/div[2]/div/a').click()
                break
            else:
                pass
        print('******判断完成**********')
        return text
  
userinfo = UserInfo()

# homePage.login()
# softid = userinfo.myCollect()
# print(softid)
# csfid = randint(0,len(softid)-1)
# #print(softid[csfid])
# result = userinfo.cancelCollect(softid[csfid])
# print(result)
# #print(userinfo.myCollect())
