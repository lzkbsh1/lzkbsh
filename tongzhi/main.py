###用于从网站https://cve.circl.lu/和https://cvetrends.com/
import re
import time
import requests
import schedule as schedule
from bs4 import BeautifulSoup
from WeChat import wechat
from zhongwen import baidu_translate
def Round_one(soup, CVEE, list, check = '', q = 0):#因为观察不会一次性更新两页，所以我只用来两个循环
  i = 0
  while True:
     b = soup.find("tbody").find_all(attrs={"id": re.compile('^CVE')})[i]
     c = str(b.find_all('td')[1].text).strip()
     e = str(b.find_all('td')[2].text).strip()
     f = str(b.find_all('td')[3].text).strip()
     f = baidu_translate(f)
     g = str(b.find_all('td')[4].text).strip()
     if i >= 49 :
       if check == '':
         CVE = str(soup.find("tbody").find_all(attrs={"id": re.compile('^CVE')})[0].find_all('td')[1].text).strip()
         aa = open('1.txt', 'w')
         aa.write(CVE)
         aa.close()
       q += 50
       url = "https://cve.circl.lu/r/" + str(q)
       a = requests.get(url="https://cve.circl.lu/r/"+str(q))
       soup = BeautifulSoup(a.content, "lxml")
       Round_one(soup, CVEE, list, '1', q)
       break
     elif c == CVEE:
       CVE = str(soup.find("tbody").find_all(attrs={"id": re.compile('^CVE')})[0].find_all('td')[1].text).strip()
       aa = open('1.txt', 'w')
       aa.write(CVE)
       aa.close()
       return list
     else:
       list.append('CVE号：'+str(c)+';CVSS:'+str(e)+';Detail:'+str(f)+';upgradetime:'+str(g)+'\n')
     i += 1
def main():
    list = []
    aa = open('1.txt', 'r+')
    CVE = aa.read()
    aa.close()
    a = requests.get(url="https://cve.circl.lu/")
    soup = BeautifulSoup(a.content, "lxml")
    list = Round_one(soup, CVE, list)
    print(11)
    for i in list:
        print(i)
        time.sleep(1)
        wechat(i)
if __name__ == '__main__':
 schedule.every(10).minutes.do(main)
 print(1)
 while True:
     schedule.run_pending()
     time.sleep(1)