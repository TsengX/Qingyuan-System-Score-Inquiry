#python3 岭南师范学院基础教育学院||湛江幼专-清元系统-成绩查询
'''此项目纯属兴趣使然和实际需求，作者是个新手，代码没有模块化和规范化
有兴趣的话欢迎来共同完善，github：'''
import requests
#import urllib.parse
#import json
import time
from PIL import Image
from io import BytesIO
#from selenium import webdriver  预使用此库实现自动score.html文件
import configparser

#定义默认的服务器端口get_utl和post_url和yzm_url
get_url = 'http://221.4.246.228:8083/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2017-2018%D1%A7%C4%EA%B5%DA%D2%BB%D1%A7%C6%DA(%C8%FD%D1%A7%C6%DA)'
post_url = 'http://221.4.246.228:8083/loginAction.do'
yzm_url = 'http://221.4.246.228:8083/validateCodeAction.do?random='
get_url_footer = '/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2017-2018%D1%A7%C4%EA%B5%DA%D2%BB%D1%A7%C6%DA(%C8%FD%D1%A7%C6%DA)'
post_url_footer = '/loginAction.do'
yzm_url_footer = '/validateCodeAction.do?random='

#弹出会话框，供选择服务器
print("\n选择服务器端口：")
print("*服务器1")
print("*服务器2")
print("*服务器3")
print("*服务器4")
print("*服务器5")
print("*服务器6")
chose_ip = input("请输入数字1~6按回车选择服务器：")
config = configparser.ConfigParser()
config.read("Ipconfig.ini")
if chose_ip == '1':
    get_url = config.get("ip1","geturl") + get_url_footer
    post_url = config.get("ip1","posturl") + post_url_footer
    yzm_url = config.get("ip1","yzmurl") + yzm_url_footer
    host = config.get("ip1", "host")
elif chose_ip == '2':
    get_url = config.get("ip2","geturl") + get_url_footer
    post_url = config.get("ip2","posturl") + post_url_footer
    yzm_url = config.get("ip2","yzmurl") + yzm_url_footer
    host = config.get("ip2", "host")
elif chose_ip == '3':
    get_url = config.get("ip3","geturl") + get_url_footer
    post_url = config.get("ip3","posturl") + post_url_footer
    yzm_url = config.get("ip3","yzmurl") + yzm_url_footer
    host = config.get("ip3", "host")
elif chose_ip == '4':
    get_url = config.get("ip4","geturl") + get_url_footer
    post_url = config.get("ip4","posturl") + post_url_footer
    yzm_url = config.get("ip4","yzmurl") + yzm_url_footer
    host = config.get("ip4", "host")
elif chose_ip == '5':
    get_url = config.get("ip5","geturl") + get_url_footer
    pos_turl = config.get("ip5","posturl") + post_url_footer
    yzm_url = config.get("ip5","yzmurl") + yzm_url_footer
    host = config.get("ip5", "host")
elif chose_ip == '6':
    get_url = config.get("ip6","geturl") + get_url_footer
    post_url = config.get("ip6","posturl") + post_url_footer
    yzm_url = config.get("ip6","yzmurl") + yzm_url_footer
    host = config.get("ip6", "host")
else:
    print("\n你输入的数字不是 1~6 ，程序准备关闭，请重新打开...")
    time.sleep(3)
    exit()
print("使用服务器" + chose_ip + ":" + host + "登录......\n" )

session = requests.session()  # 建立会话，保持会话信息，cookies
r = session.get(post_url)
cookies = r.headers['Set-Cookie']  # 获取cookies
cookies = cookies.strip('; path=/')  # 删除指定字符，这里是由于 我学
                                            #校的教务系统在cookies加了干扰数据。

yam_headers = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookies,
    'Host': '221.4.246.228:8083',
    'Referer':'http://221.4.246.228:8083/loginAction.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
#这是获取验证码的表头


yamdata = session.get(yzm_url, headers=yam_headers)  # 获取验证码
tempIm = BytesIO(yamdata.content)  # 将数据流放入tempIm以字节的形式
im = Image.open(tempIm)  # 转换为图片的形式
im.show()  # 展示验证码
Code = input('请输入验证码:')

#将登录的账号密码赋给登录用
username = input("请输入账号：")
password = input("请输入密码：")

#需要提交的数据
logindata = {
    "zjh1" : "",
    "tips" : "",
    "lx" : "",
    "evalue" : "",
    "eflag" : "",
    "fs" : "",
    "dzslh" : "",
    "zjh" : username,
    "mm" : password,
    "v_yzm" : Code
}
#post用的headers
login_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '37',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '',
    'Host': host,
    'Origin': 'http://' + host,
    'Referer': 'http://' + host + '/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
#get成绩页面的headers
login_headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': host,
    'Origin': 'http://' + host,
    'Referer': 'http://' + host + '/gradeLnAllAction.do?type=ln&oper=qb',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}
#get用户信息页面的headers
login_headers2 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': host,
    'Referer': 'http://' + host + '/menu/menu.jsp',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

#将coolies添到headers，保存一个绘画的关键！
login_headers['Cookie'] = cookies
login_headers1['Cookie'] = cookies
login_headers2['Cookie'] = cookies

d = session.post(post_url, data=logindata, headers=login_headers)#将账号，密码，验证码和表头Post上去
#然后我们可以用过BeautifulSoup或者正则表达式，抓取d.text有用的信息，判断是否登录成功。

'''print(d.content.decode('gb2312'))'''

#get到成绩页面的html代码
s = session.get(get_url, headers=login_headers1)
mycontent = s.content.decode('gb2312')


error1 = mycontent.find("errorTop")

if error1 != -1:
    print("\n登录失败\n")
    print("你输入的验证码错误或账号或密码错误，请关闭程序，重新执行程序，重新输入！")
else:
    print("\n登录成功\n")
    score = mycontent.encode(encoding="gb2312")     #将成绩网页源代码保存到本地
    fp = open("score.html","w+b")
    fp.write(score)
    fp.close()

    #get到用户信息的页面，将学号，姓名输出
    i = session.get('http://' + host + '/xjInfoAction.do?oper=xjxx', headers=login_headers2)#将成绩页面的html代码打印出来
    mycontent1 = i.content.decode('gb2312')
    name = []
    a = mycontent1.find("姓名")
    name.append(mycontent1[a+66:a+71])
    print("姓名：" + name[0] + "学号：" + username)
    print("你的成绩已保存在根目录的score.html文件，打开即可查看")
    
print("\n请手动关闭程序或等待10秒自动关闭")
time.sleep(10)
exit()


