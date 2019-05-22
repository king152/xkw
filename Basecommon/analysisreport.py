'''
Created on 2019年5月21日
@author: king
@job number:xy04952
'''
# coding:utf-8

from bs4 import BeautifulSoup


class AnalysReport:
    
    def __init__(self):
        pass
    
    def report(self,reportname):
        
        try :
            
            # 打开html文件，读取报告内容
            with open(reportname, "r",encoding='utf-8') as fp:
                f = fp.read()  # 读报告
            soup = BeautifulSoup(f, "html.parser")
            status = soup.find_all(class_="attribute")
            result = status[2]
            flag = "Failure" in result or "Error" in str(result)
            if flag:
                print("\n***存在失败或者错误用例执行结果！，正在发送邮件*****")
                return True
            else:
                print('\n*****用例执行全部通过,不需要发送邮件！！*****')
                return False
        except Exception as e :
            return [True , e]
              
analysReport=AnalysReport()