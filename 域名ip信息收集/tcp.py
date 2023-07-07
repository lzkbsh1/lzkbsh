import threading
import time
import socket
import queue
import sys


q=queue.Queue()

# 端口扫描
def tcp_test():
    while not q.empty():
        ips = q.get()
   # print(ips)
        host=ips.split('|')
        ip=host[0]
        port=int (host[1])
        #print(ip)
       # print(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(ip+' '+str(port) + '|open' + '\n')
            file = open('portopen.txt', 'a+')
            file.write(str(port) + '\n')
            file.close()
        else:
            print(ip+' '+str(port) + '|close' + '\n')
            time.sleep(0.1)
        s.close()

def file(ips,ports,num):
    res=[]
    #if IPy.IP(ips):
        #sys.exit()
   # print(ips)
    if '-' in ports:
        port=ports.split('-')
        port1=port[0]
        port2=port[1]
        for y in range(int(port1), int(port2) + 1):
            res.append(y)
    if ',' in ports:
        res=ports
    #for ip in ips:
    for port in res:

        ipport = ips + '|' + str(port)
        q.put(ipport)
        #print(ipport)

    for i in range(int(num)):
        al = threading.Thread(target=tcp_test)
        al.start()
'''
if __name__ == '__main__':
     ips = sys.argv[1]
     port = sys.argv[2]
     num = sys.argv[3]

     file(ips, port, num)

'''



''' 
        for port in range(1,65536):
            q.put(port)
        for i in range(20):
            al=threading.Thread(target=portscan)
            al.start()
'''