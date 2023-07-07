import sys
import tcp
import dir
import dic
import qw
def show():
    print("ps:main.py 脚本名 目标 字典 线程数字")
    print("\n")
    print('ps:mian.py dirs www.baidu.com dir.txt 10')
    print("脚本名 域名 字典 线程")


if __name__ == '__main__':
    if sys.argv[1]=='dirs':
        url = sys.argv[2]
        file = sys.argv[3]
        num = sys.argv[4]
        dir.file(url,file,num)
     #   dir.thread(num)
    elif sys.argv[1]=='dics':
        url = sys.argv[2]
        file = sys.argv[3]
        num = sys.argv[4]
        dic.file(url, file, num)
    elif sys.argv[1]=='tcp':
        ip = sys.argv[2]
        port = sys.argv[3]
        num = sys.argv[4]
        tcp.file(ip,port,num)
    elif sys.argv[1]=='ip':
        url=sys.argv[2]
        qw.ip_check(url)
    elif sys.argv[1]=='whois':
        url=sys.argv[2]
        qw.whois_check(url)
    elif sys.argv[1]=='cdn':
        url=sys.argv[2]
        qw.cdn_check(url)
    else:
        show()
        sys.exit()


