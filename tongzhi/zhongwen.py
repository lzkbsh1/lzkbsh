import http.client
import hashlib
import json
import urllib
import random


def baidu_translate(content):
    appid = '20191218000367407'  # 这个appid 请访问 http://api.fanyi.baidu.com/ 注册认证后获得
    secretKey = 'MnFJgUOPIJmlncyEcgWK'  # 这个秘钥 请访问 http://api.fanyi.baidu.com/ 注册认证后控制台查看
    httpClient = None
    myurl = '/api/trans/vip/translate'  # 百度翻译接口
    q = content
    fromLang = 'auto'  # 源语言
    toLang = "zh"  # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()


