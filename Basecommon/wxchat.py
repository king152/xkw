'''
Created on 2019年5月17日
@author: king
@job number:xy04952
'''
#coding = utf-8
# from base64 import decode

# import itchat
# 
# itchat.auto_login(hotReload=True)
# 
# def send_onegroup(msg,gname):
#     #rooms = itchat.get_chatrooms(update = True)
#     rooms =itchat.search_chatrooms(gname)
#     if rooms is not None:
#         username = rooms[0]['UserName']
#         itchat.send(msg,toUserName=username)
#     else:
#         print('None group found') 

# u = '''{"UserId":28760514,"UserName":"马志远","Identity":200002,"UserGroupID":8,"SchoolId":456470,"endDataStr":null,"userFace":"00004.jpg","RegTime":"2018-11-21 09:10:10"}'''
# str = u.encode('utf-8')
# print(str)
# print(str.decode('utf-8'))
# 
# if __name__ == '__main__':
# #     send_onegroup('这是机器人发送的消息。。。。', u'会当凌绝顶')
#     pass


result =' <p class="attribute"><strong>状态:</strong> <span class="tj passCase">Pass</span>:1 <span class="tj failCase">Failure</span>:1 <span class="tj errorCase">Error</span>:1 <span class="tj">通过率</span>:33.3%</p>'
if "Failure" in result or "Error" in result :
    print('*****')
else:
    print('#####')