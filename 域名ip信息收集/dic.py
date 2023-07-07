import os
import queue
import sys
import threading
import time
import dns.resolver
import requests
import socket

q=queue.Queue()
def domainscan():
    while not q.empty():
        url=q.get()
        print(url)

    try:
        ip=socket.gethostbyname(url)
        f = open("dicyes.txt", "a+")
        f.write(url+'  '+ip+'\n')
        f.close
        time.sleep(0.1)
    except Exception as e:
        pass

def file(url,file,num):
    path = os.path.dirname(os.path.realpath(__file__))
    url=url.replace('www.','')
    print(url)
    for dir in open(path+'/'+file):
        dir = dir.replace("\n", '')
        url_dir = dir + '.' + url
        q.put(url_dir)

    for i in range(int(num)):
        t=threading.Thread(target=domainscan)
        t.start()

def show():
    print('ps:scan.py kxsy.work dir.txt 10')
    print("\n")
    print("脚本名 域名 字典 线程")
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
        q.put(dir)
    for i in range(int(num)):
        t=threading.Thread(target=domainscan)
        t.start()
'''