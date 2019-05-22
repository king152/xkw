'''
Created on 2019年5月21日
@author: king
@job number:xy04952
'''
from Basecommon.xkw_basecommon import xkwBaseUtil
from time import sleep
from PIL import Image
import pytesseract

# xkwBaseUtil.set_driver(u'谷歌')
# xkwBaseUtil.get('http://manage.zxxk.com/MasterLogin.asp')
# xkwBaseUtil.maximize_window()
# sleep(5)
# imgname = xkwBaseUtil.get_save_screenshot() #截图
# verifyimg_ele = xkwBaseUtil.find_element_by_id('CheckCodeImg')
# left = verifyimg_ele.location['x']
# top = verifyimg_ele.location['y']
# right = verifyimg_ele.location['x']+verifyimg_ele.size['width']
# bottom = verifyimg_ele.location['y']+verifyimg_ele.size['height']
# print(left,top,right,bottom)
# img = Image.open(imgname)
# img = img.crop((left-2,top-4,right+2,bottom+4))
# img.save('verifyimage.png')
# sleep(5)
for i in range(10):
    code = pytesseract.image_to_string(Image.open('verifyimage.png'))
    print(code)
