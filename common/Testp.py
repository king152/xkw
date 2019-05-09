'''
Created on 2019年5月8日

@author: king
@number:xy04952
'''
import configparser

config=configparser.ConfigParser()
config.read('..//conf//data.conf', 'utf-8')
mp=config.get("LoginAccount","MobilePhone")
print(mp)

