import os
import socket
import sys

from whois import whois
import time
import nmap

#域名反查ip地址
def ip_check(url):
 ip=socket.gethostbyname(url)
 print(ip)


#识别目标是否存在CDN
#采用nslookup执行端进行返回ip解析数目结果判断
#利用python执行系统命令

#os.system()无法操作结果
#cdn_data=os.system('nslookup www.xiaodi8.com')
#print(cdn_data)
def cdn_check(url):
 cdn_data=os.popen('nslookup '+url).read()
 print(cdn_data)
 x=cdn_data.count('.')
 print(x)



#whois查询
#第三方库进行whois查询
def whois_check(url):
    data=whois(url)
    print(data)

'''
if __name__ == '__main__':
    #whois_check('www.baidu.com')
    if sys.argv[1]=='whois':
        url=sys.argv[2]
        whois_check(url)
'''