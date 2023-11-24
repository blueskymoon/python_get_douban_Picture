# 下载豆瓣图片-刘涛图片.py
import requests
from bs4 import BeautifulSoup
import os


#  获取访问的header表头
def read_header():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    return headers

#   获取每一页的数据
def get_url_data():
    for page in range(0, 450, 30):
        print("开始爬取第{}页".format(page))
        headers = read_header()
        url = "https://movie.douban.com/celebrity/1011562/photos/?type=C&start={}&xsortby=like&size=a&subtype=a".format(
            page)
        res = requests.get(url, headers=headers).text
        data = get_poster_url(res)  # get_poster_url中的picture_list列表，列表内存储的是图片的网址
        download_picture(data)  # 将网址作为实参给到download_picture这个模块中


def get_poster_url(res):
    content = BeautifulSoup(res, "html.parser")
    # print(content)
    data = content.find_all('div', {'class': 'cover'})  # 没有抓到东西bug
    # for z in data:
    # print(z)
    picture_list = []
    for d in data:
        plist = d.find('img')['src']
        picture_list.append(plist)
    return picture_list


def download_picture(pic_l):
    if not os.path.exists(r'picture_刘涛'):  # 如果在当前文件夹中不存在picture,则使用os.mkdir函数创建名字为picture的文件夹
        os.mkdir(r'picture_刘涛')
    for i in pic_l:  # 循环读取pic_l的网址赋值给i
        read_header()
        pic = requests.get(i)  # 使用requests.get() 获取网址内容赋值给pic
        p_name = i.split('/')[7]  # 使用split()函数以'/'为分割线，获取列表中的第8个字符给p_name
        # print(p_name)
        with open('picture1\\' + p_name, 'wb') as f:  # with open 作为打开文件和关闭文件的简写，'wb'是写入二进制数据。
            f.write(pic.content)


if __name__ == '__main__':
    get_url_data()
