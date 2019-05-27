'''
Created on 2019年5月9日

@author: king
@number:xy04952
'''
#-*-encoding:utf-8-*-

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from aip import AipOcr




class XkwBaseUtil:
    def __init__(self):
        self.driver = None

    # 设置驱动
    def set_driver(self, browser_type):
        try:
            browser_type = browser_type.lower()
            if 'ie' == browser_type:
                self.browser_type = 'Ie'
                self.driver = webdriver.Ie()
            elif '谷歌' == browser_type:
                self.browser_type = 'Chrome'
                self.driver = webdriver.Chrome()
            elif '火狐' == browser_type:
                self.browser_type = 'Firefox'
                self.driver = webdriver.Firefox()
            else: 
                print("浏览器只支持IE、谷歌、火狐")
            #return ''
        except Exception as e:
            print('设置浏览器驱动出错：%s' % e)


    def get_driver(self):
        return self.driver


    # 打开网址
    def get(self, url):
        try:
            self.driver.get(url)
            return ''
        except Exception as e:
            return [False, '打开网址：%s 失败,原因：%s' % (url, e)]

    # 模拟浏览器 后退
    def back(self):
        try:
            self.driver.back()
            return ''
        except Exception as e:
            return [False, '模拟浏览器后退，失败，原因：%s' % e]

    # 浏览器 前进
    def forward(self):
        try:
            self.driver.forward()
            return ''
        except Exception as e:
            return [False, '模拟浏览器前进，失败，原因：%s' % e]

    # 退出
    def close(self):
        try:
            # self.driver.close()
            self.driver.quit()
        except Exception as e:
            return [False, '%s' % e]

    # 智能等待
    def implicitly_wait(self, second):
        try:
            self.driver.implicitly_wait(second)
            return 'success'
        except Exception as e:
            return [False, '%s' % e]

    # 休眠
    def sleep(self, second):
        try:
            time.sleep(second)
            return 'success'
        except Exception as e:
            return [False, e]

    #浏览器最大化
    def maximize_window(self):
        try:
            self.driver.maximize_window()
            return 'success'
        except Exception as e:
            return [False, '%s' % e]

    # 获取页面标题
    def get_page_title(self):
        try:
            page_title = self.driver.title
            return page_title
        except Exception as e:
            return [False, '获取页面标题失败 %s' % e]
    
    #根据元素id 获取元素名称
    def get_element_by_id_name(self,Id):
        try:
            Idname = self.driver.find_element_by_id(Id).text
            return Idname
        except Exception as e:
            return [False, '获取元素名称失败 %s' % e]

    #根据元素class 获取元素名称
    def get_element_by_class_name(self,Class):
        try:
            Classname = self.driver.find_element_by_class_name(Class).text
            return Classname
        except Exception as e:
            return [False, '获取元素名称失败 %s' % e]
    
    #根据元素 name 获取元素名称
    def get_element_by_name_name(self,name):
        try:
            Name = self.driver.find_element_by_name(name).text
            return Name
        except Exception as e:
            return [False, '获取元素名称失败 %s' % e]
        
    # 根据id查找元素
    def find_element_by_id(self,Id):
        try:
            element = self.driver.find_element_by_id(Id)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据xpath查找元素
    def find_element_by_xpath(self, xpath):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据name查找元素
    def find_element_by_name(self, name):
        try:
            element = self.driver.find_element_by_name(name)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据link查找元素
    def find_element_by_link(self, link):
        try:
            element = self.driver.find_element_by_link(link)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据link_text查找元素
    def find_element_by_link_text(self, link_text):
        try:
            element = self.driver.find_element_by_link_text(link_text)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据partial_link_text查找元素
    def find_element_by_partial_link_text(self, partial_link_text):
        try:
            element = self.driver.find_element_by_partial_link_text(partial_link_text)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据css selector查找元素
    def find_element_by_css_selector(self, css_selector):
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据tag_name查找元素
    def find_element_by_tag_name(self,tag_name):
        try:
            element = self.driver.find_element_by_tag_name(tag_name)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据标签class name查找(查找单个)
    def find_element_by_class_name(self, class_name):
        try:
            element = self.driver.find_element_by_class_name(class_name)
            return element
        except Exception as e:
            return [False, '%s' % e]

    # 根据标签class name查找，查找多个
    def find_element_by_class_names(self, class_name):
        try:
            elements = self.driver.find_element_by_class_name(class_name)
            return elements
        except Exception as e:
            return [False, '%s' % e]
        
    #定位iframe 里面的元素
    def find_to_iframe_element(self,iframeid,elementid):
        try:
            self.driver.switch_to_frame(iframeid)
            element=self.driver.find_element_by_id(elementid)
            return element
        except Exception as e:
            return [False, '%s' % e]
        
    #富文本框输入内容,iframe 存在id属性
    def iframeid_imput_content(self,iframeid,content):
        try:
            js = 'document.getElementById('+iframeid+').contentWindow.document.body.innerHTML="%s"' %(content)
            self.driver.execute_script(js)
        except Exception as e :
            return [False, '%s' % e]
    
    #富文本框输入内容,iframe 不存在id属性
    def iframeclass_imput_content(self,iframeclass,content):
        try:
            js="document.getElementsByClassName(\"wind_editor_iframe\")[0].contentWindow.document.body.innerHTML=\"%s\"" %(content)
            self.driver.execute_script(js)
        except Exception as e :
            return [False, '%s' % e]
        
    #接收警告框
    def alert_accept(self):
        try:
            self.driver.switch_to_alert().accept()
        except Exception as e :
            return [False, '%s' % e]
    
    #获取警告框的文本
    def get_alert_content(self):
        try:
            return self.driver.switch_to_alert().text
        except Exception as e :
            return [False, '%s' % e]
    
    #获取警告框的文本
    def dismiss_alert(self):
        try:
            self.driver.switch_to_alert().dismiss()
        except Exception as e :
            return [False, '%s' % e]
    
    # 鼠标移动到界面元素上
    def move_to_element(self, element):
        try:
            chain = ActionChains(self.driver)
            chain.move_to_element(element).perform()
            return [True, '移动操作成功']
        except Exception as e:
            return [False, '移动操作失败：%s' % e]

    #鼠标悬停显示二级菜单，再通过class属性定位二级菜单界面元素
    def move_to_element_Locatelement_calss(self,Parent_element,link_text):
        try:
            chain = ActionChains(self.driver)
            chain.move_to_element(Parent_element).perform()
            element=self.driver.find_element_by_link_text(link_text)
            return element
        except Exception as e:
            [False, '移动操作定位失败：%s' % e]

    #鼠标悬停显示二级菜单，再通过xpath属性定位二级菜单界面元素
    def move_to_element_Locatelement_xpath(self,Parent_element,Locatelement):
        try:
            chain = ActionChains(self.driver)
            chain.move_to_element(Parent_element).perform()
            element=self.driver.find_element_by_xpath(Locatelement)
            return element
        except Exception as e:
            [False, '移动操作定位失败：%s' % e]

    #鼠标悬停显示二级菜单，再通过css属性定位二级菜单界面元素
    def move_to_element_Locatelement_css(self,Parent_element,css_selector):
        try:
            chain = ActionChains(self.driver)
            chain.move_to_element(Parent_element).perform()
            element=self.driver.find_elements_by_css_selector(css_selector)
            return element
        except Exception as e:
            [False, '移动操作定位失败：%s' % e]

    # 拖动滚动条至元素可见
    def scroll_to_element_for_visible(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return [True, '拖动滚动条至元素可见成功']
        except Exception as e:
            return [False, '拖动滚动条至元素可见失败：%s' % e]

    #执行js脚本
    def execute_js(self,JS):
        '''
                          去掉元素的readonly属性 'document.getElementById("datehome").removeAttribute("readonly");'
                          直接采用js设定日期'document.getElementById("datehome").value="2019-05-10";'
        '''
        try:
            self.driver.execute_script(JS)
        except Exception as e:
            return [False, '执行JS脚本失败：%s' % e]    
 
    def execute_js_text(self,JS):
        try:
            Text = self.driver.execute_script(JS)
            return Text
        except Exception as e:
            return [False, '执行JS脚本失败：%s' % e]     
       
       

    #用Js的方式拖动垂直滚动条到底部、顶部：
    def scroll_to_top_or_bottom(self, direction):
        try:
            if direction == '底部':
                js = 'document.documentElement.scrollTop=10000'
            elif direction == '顶部':
                js = 'document.documentElement.scrollTop=0'
            self.driver.execute_script(js)
            return [True, '拖动滚动条至%s成功' % direction]
        except Exception as e:
            return [False, '拖动滚动条至元素可见失败：%s' % e]

    # 切换到指定名称的窗口
    def switch_to_window_by_name(self, name):
        try:
            self.driver.switch_to.window(name)
            return [True, 'success']
        except Exception as e:
            return [False, '%s' % e]

    # 切换到指定标题名称的窗口(标题相同的话，按先后顺序取一个)
    def switch_to_window_by_title(self, title):
        try:
            # current_handle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                self.driver.switch_to_window(handle)
                page_title = self.driver.title
                if page_title == title:
                    self.driver.switch_to_window(handle)
                    return [True, 'success']
            return [False, '未找到当前页面标题为“%s”的窗口' % title]
        except Exception as e:
            return [False, '%s' % e]
    #切换窗口
    def switch_windows_handle(self):
        try:
            current_handle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle !=current_handle:
                    self.driver.close()
                    self.driver.switch_to.window(handle)                  
            return [True, 'success']
        except Exception as e:
            return [False, '%s' % e]

    # 切换到指定URL的窗口(标题相同的话，按先后顺序取一个)
    def switch_to_window_by_url(self, url):
        try:
            handles = self.driver.window_handles
            # logger.info('当前窗口句柄有：%s' % handles)
            for handle in handles:
                self.driver.switch_to_window(handle)
                url_for_handle = self.driver.current_url
                if url_for_handle == url:
                    self.driver.switch_to_window(handle)
                    return [True, 'success']
            return [False, '未找到当前URL为“%s”的窗口' % url]
        except Exception as e:
            return [False, '%s' % e]

    #关闭当前窗口
    def close_current_window(self):
        try:
            self.driver.close()
            handles = self.driver.window_handles
            if handles: # 如果存在其它窗口，默认切换至前一次新开的窗口
                self.driver.switch_to_window(handles[len(handles)-1])
            return [True, 'success']
        except Exception as e:
            return [False, '%s' % e]

    #切换frame
    def switch_to_frame(self, type,idelement):
        try:
            if type=='id':
                Frame = self.driver.find_element_by_id(idelement)
                self.driver.switch_to_frame(Frame)
            elif type == 'name':
                Frame = self.driver.find_element_by_name(idelement)
                self.driver.switch_to_frame(Frame)
            elif type=='tag':
                Frame = self.driver.find_element_by_tag_name(idelement)
                self.driver.switch_to_frame(Frame)
            else:
                print('定位方式传参错误！')
            return [True, 'success']
        except Exception as e:
            return [False, '%s' % e]
        
    #退出iframe
    def logout_iframe(self):
        try:
            self.driver.switch_to_default_content()
        except Exception as e:
            return [False, '%s' % e]
    
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()    
    
    def get_VerificatCodepic(self,class_Element):
        try :
            APP_ID='16315444'
            API_KEY='CVx0Yc9PMsvOLcl9rhaahuBm'
            SECRET_KEY='LRVBwgRoewNDPapSy08LrCHwUhtAvCxh'
            imgname = self.get_save_screenshot() #截图
            verifyimg_ele = xkwBaseUtil.find_element_by_class_name(class_Element)
            left = verifyimg_ele.location['x']
            top = verifyimg_ele.location['y']
            right = verifyimg_ele.location['x']+verifyimg_ele.size['width']
            bottom = verifyimg_ele.location['y']+verifyimg_ele.size['height']
            img = Image.open(imgname)
            img = img.crop((left-2,top-4,right+2,bottom+4))
            img.save('../pic/verifyimage.png')
            img = self.get_file_content('../pic/verifyimage.png')
            code=AipOcr(APP_ID, API_KEY, SECRET_KEY).basicAccurate(img)
            result_list = str(code['words_result'])
            result_str = result_list[12:16]
            print(result_list)
            return result_str
        except Exception as e:
            print(e)
    
    #判断元素是否存在
    def is_exist_element(self,elem):
        try:
                
            s = self.driver.find_elements_by_css_selector(elem)
            if len(s) == 0:
                print("不存在%s元素" % elem)
                return False 
            elif len(s) == 1:
                return True  
            else:
                print ("存在%s个元素分别是%s" %(len(s), s))
                return False
        except Exception as e:
            return [False, '%s' % e]

    # 截图
    def get_screenshot(self):
        try:
            pic_directory=time.strftime("%Y-%m-%d", time.localtime(time.time()))
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = './Report/image/'+pic_directory+'/' + current_time +'.png'
            self.driver.get_screenshot_as_file(pic_path)
            print(pic_path)
            return [True, '截图成功']
        except Exception as e:
            return [False, '截图失败：%s' % e]
        
    def get_save_screenshot(self):
        try:
            current_time=time.strftime("%Y-%m-%d", time.localtime(time.time()))
            pic_path =  '../pic/'+current_time +'.png'
            self.driver.get_screenshot_as_file(pic_path)
            return pic_path
        except Exception as e:
            return [False, '截图失败：%s' % e]
        
    def add_img(self):
        return self.driver.get_screenshot_as_base64()
    
    def scrollelment(self,type,elment):
        try:
            if type == 'id':
                target = self.driver.find_element_by_id(elment)
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            elif type =='class':
                target = self.driver.find_element_by_class_name(elment)
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            elif type == 'xpath':
                target = self.driver.find_element_by_xpath(elment)
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            elif type == 'name':
                target = self.driver.find_element_by_name(elment)
                self.driver.execute_script("arguments[0].scrollIntoView();", target)
            else:
                print('目前只支持 id name class xpath方式')
        except Exception as e:
            return [False, '移动失败：%s' % e]

xkwBaseUtil=XkwBaseUtil()