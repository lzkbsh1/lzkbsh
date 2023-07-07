import sys
import os
import tarfile
import wsgiref.validate
import re
import requests
import threading
import time
import queue

q=queue.Queue()
headers = { # HTTP 头设置
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
	'Referer' : 'http://www.google.com',
	'Cookie': 'whoami=wyscan_dirfuzz',
}
def scan():
    while not q.empty():
        urls=q.get()
        #print(urls)

        try:
            code = requests.get(urls,headers=headers,timeout=10).status_code
            if code==200 or code==403 :
                f=open("dirsyes.txt","a+")
                f.write(urls+'\n')
                f.close
                time.sleep(10)
            else:
                print(urls+'|'+str(code))
                time.sleep(1)
        except Exception as e:

            pass

def show():
    print("ps:scan.py 目标 字典 线程数字")
    print("\n")



def file(url,file,num):
    path = os.path.dirname(os.path.realpath(__file__))
    for dir in open(path+'/'+file):
        dir=dir.replace("\n",'')
        url_dir=url+dir
        q.put(url_dir)

    for i in range(int(num)):
        t=threading.Thread(target=scan)
        t.start()

def thread(num):
    for i in range(int(num)):
        t=threading.Thread(target=scan)
        t.start()
'''
if __name__ == '__main__':
    path=os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv)<4:
        show()
        sys.exit()
    url=sys.argv[1]
    file=sys.argv[2]
    num=sys.argv[3]
    for dir in open(path+'/'+file):
        dir=dir.replace("\n",'')
        url_dir=url+'/'+dir
        q.put(url_dir)
        scan()


    for i in range(int(num)):
        t=threading.Thread(target=scan)
        t.start()
'''
