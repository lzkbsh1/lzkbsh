import sys
import requests, re
from selenium import webdriver
import chromedriver_autoinstaller
import os


def status_code(url):
    req = requests.get(url)
    return req.status_code


def checkurl(url):
    if url[:4] != "http":
        return "http://" + url
    else:
        return url


def jietu(url, C, u):
    url = checkurl(url)
    try:
        x = driver.get(url)
        a = status_code(url)
        b = C + "\\" + str(u) + ".png"
        driver.save_screenshot(b)  # 使用 save_screenshot 进行截图
        print("[" + driver.title + "]" + url + ":" + str(a))
        return "[" + driver.title + "]" + "_" + url + "_" + str(a)
    except:
        return ""


if __name__ == '__main__':

    chromedriver_autoinstaller.install()  # 检测是否有安装chmoredriver模块
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    x = [];
    u = 0
    A = sys.argv[1]
    C = sys.argv[2]
    os.mkdir(C)
    with open(A, "r") as urls:
        for url in urls:
            a = jietu(url.strip(), C, u)
            u += 1
            x.append(a)
        urls.close()
    driver.quit()
    AA = C + ".txt"
    with open(AA, "w") as file:
        for i in x:
            file.write(i + "\n")
        file.close()

    filenames = []
    dataclasse = []
    j = -1
    for root, dirs, files in os.walk(C):
        for filename in files:
            if filename[-3:] == 'png':
                filenames.append(filename)
    with open(AA, "r") as f:
        for i in f.readlines():
            j += 1
            try:
                a = i.strip().split("_")
                a[0] = a[0].replace("[", "")
                a[0] = a[0].replace("]", "")
                # filenames[j],a[1],a[0],a[2]
                data = "{0}_{1}_{2}_{3}".format(a[0], a[1], a[2], filenames[j])
                print(data)
                dataclasse.append(data)
            except:
                pass
    file_start = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    * {
        padding: 1;
        margin: 0;
    }

    img {

    }

    .main {
        height: 334px;
        width: 300px;
        position: relative;
        top: 20%;
        border: 1px solid #aaa;
        box-shadow: 0px 1px 1px 1px #aaa;
        /* transform: translateY(50%); */
        /* background-color: skyblue; */
        margin: 0 auto;
        margin-top: 10px;
        border-radius: 10px;
        overflow: hidden;
    }

    h3 {
        font-size: 16px;
        line-height: 40px;
        text-align: center;
        /* background-color: #ddd; */
        height: 40px;
        font-weight: normal;
        border-bottom: 1px solid #aaa;
    }

    .b_main {
        padding-top: 3px;
        /* background-color: aqua; */
        height: 160px;
    }

    .footbox {
        display: flex;
        flex-direction: column;
        height: 130px;
    }

    .item1 {
        flex: 2;
        /* background-color: pink; */
        display: flex;
        flex-direction: column;
        border-top: 1px solid #aaa;
        background-color: rgb(248, 248, 248);
        /* border-bottom: 1px solid #ccc; */
    }

    .item1_1 {
        flex: 1;
        /* border: 1px black solid; */
        font-size: 16px;
        padding-left: 10px;
        padding-top: 10px;
        color: rgb(96, 95, 95);
        /* line-height: 16px; */
    }

    .item1_2 {
        flex: 2;
        /* border: 1px black solid; */
        display: flex;
        padding: 5px;

    }

    .item1_2 .item1_2_1 {
        flex: 1;

        margin-right: 5px;
    }

    .item1_2 .show {
        font-size: 12px;
        padding: 5px;
        background-color: rgb(120, 194, 120);
        border-radius: 10px;
        color: white;
        height: 16px;
        text-align: center;
    }
    a:visited{
    color: skyblue;
    }

    .item2 {
        flex: 1;
        /* background-color: yellow; */
        display: flex;
        flex-direction: row;
        /* border-bottom: 1px solid #ccc; */
    }

    .item2_1 {
        /* border: 1px solid #ccc; */
        flex: 1;
        text-align: center;
        padding-top: 10px;
        background-color: #eee;
    }

    .view {
        text-align: center;
        color: skyblue;
        border: skyblue 2px solid;
        border-radius: 5px;

        font-weight: 700;
        width: 100px;
        font-size: 16px;
        margin: auto;
    }
</style>

<body>
    '''
    file_end = '</div></body></html>'
    x = open(C + "\\" + C + ".html", "w", encoding="utf-8")
    x.write(file_start)
    for i in dataclasse:
        a = i.strip().split("_")
        message = '''
       <div class="main">
       <h3>{1}</h3>
        <div class="b_main">
            <img src="{3}" width="300" alt="" srcset="">
        </div>
        <div class="footbox">
            <div class="item1">
                <div class="item1_1">{0}</div>
                <div class="item1_2">
                    <div class="item1_2_1 show">{2}</div>
                </div>
            </div>
            <div class="item2">
                <div class="item2_1">
                    <div class="view">
                    <a href="{1}" target="_blank">{0}</a>
                    </div>
                </div>
            </div>
        </div></div>'''.format(a[0], a[1], a[2], a[3])
        x.write(message)
    x.write(file_end)
    x.close()