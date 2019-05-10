'''
Created on 2019年5月9日
@author: king
@job number:xy04952
'''

import os
import time
import shutil
import configparser

class Creatdirectory:
    '''
     Check if the current directory exists, create a directory if it does not exist, 
     and store the screenshot
    '''
    #Init data
    def __init__(self):
        self.pic_directory=time.strftime("%Y-%m-%d", time.localtime(time.time()))
        self.filedirectory='../Report/image/'+self.pic_directory
        config=configparser.ConfigParser()
        config.read('..//conf//data.conf', 'utf-8')
        self.deletefiledir=config.get("browserDownloaddir","chromeDownloaddir")

    #Check folder exists, no folder creation exists
    def checkdirectory(self):
        if os.path.exists(self.filedirectory):
            pass
            #print("文件夹已存在，不需要创建")
        else:
            try:
                os.makedirs(self.filedirectory)
                #print('文件夹创建成 %s:'% self.filedirectory)
            except Exception as e:
                print(e)
    
    #Delete files from the specified folder
    def deletefile(self):
        self.filelist=[]  
        try:  
            self.filelist=os.listdir(self.deletefiledir)                #列出该目录下的所有文件名
            for f in self.filelist:
                self.filepath = os.path.join(self.deletefiledir,f)   #将文件名映射成绝对路劲        
                if os.path.isfile(self.filepath):            #判断该文件是否为文件或者文件夹
                    os.remove(self.filepath)                #若为文件，则直接删除
                elif os.path.isdir(self.filepath):
                    shutil.rmtree(self.filepath,True)       #若为文件夹，则删除该文件夹及文件夹内所有文件
            #print("删除成功")
        except Exception as e:
            print(e)
            
    #Gets the file name of the specified directory
    def get_dir_filename(self):
        filelists=[]
        filelist = []
        try:
            filelists=os.listdir(self.deletefiledir)
            filelist = filelists[0].split('.')
            return filelist[0]
        except Exception as e:
            print(e)

creatdirectory=Creatdirectory()


