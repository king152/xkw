'''
Created on 2019年5月21日
@author: king
@job number:xy04952
'''
from Basecommon.xkw_basecommon import xkwBaseUtil
from time import sleep
from PIL import Image
from aip import AipOcr
import configparser


class AutoIdentifyVerificatCode:
    def __init__(self):
        try:
            config=configparser.ConfigParser()
            config.read('E:\\pythonscript\\xkw.zxxk\\conf\\data.conf', 'utf-8')
            self.APP_ID=config.get("baiduAi","APP_ID")
            self.API_KEY=config.get("baiduAi","API_KEY")
            self.SECRET_KEY=config.get("baiduAi","SECRET_KEY")
            self.url = config.get("baiduAi","Mangen_URL")
            self.ID_Element=config.get("baiduAi","ID_Element")
        except Exception as e:
            print(e) 
        
    def get_VerificatCodepic(self):
        try :
            xkwBaseUtil.set_driver(u'谷歌')
            xkwBaseUtil.get(self.url)
            xkwBaseUtil.maximize_window()
            sleep(20)
            imgname = xkwBaseUtil.get_save_screenshot() #截图
            verifyimg_ele = xkwBaseUtil.find_element_by_id(self.ID_Element)
            left = verifyimg_ele.location['x']
            top = verifyimg_ele.location['y']
            right = verifyimg_ele.location['x']+verifyimg_ele.size['width']
            bottom = verifyimg_ele.location['y']+verifyimg_ele.size['height']
            img = Image.open(imgname)
            img = img.crop((left-2,top-4,right+2,bottom+4))
            img.save('../pic/verifyimage.png')
        except Exception as e:
            print(e)

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
        
    def get_code(self):
        try:
            self.get_VerificatCodepic()
            img = self.get_file_content('../pic/verifyimage.png')
            code=AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY).basicAccurate(img)
            result_list = str(code['words_result'])
            result_str = result_list[12:16]
            print(result_list)
            return result_str
        except Exception as e:
            print(e)
    def login(self):
        xkwBaseUtil.find_element_by_name('UserName').send_keys('125522')
        xkwBaseUtil.find_element_by_name()              

autocode=AutoIdentifyVerificatCode() 

#调式信息
# autocode.__init__()
# print(autocode.get_code())
