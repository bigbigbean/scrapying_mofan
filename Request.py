import requests
import webbrowser

# get的用法
param = {"wd":"莫烦Python"}  # 搜索的信息
# param = {"wd":"tensorflow"}
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
# http://www.baidu.com/s?wd=%E8%8E%AB%E7%83%A6Python
webbrowser.open(r.url)


# post的用法 text:name
data = {'firstname':'Mingyang','lastname':'Wang'}
l = requests.post('http://pythonscraping.com/pages/files/processing.php',data=data)
print(l.text)
# Hello there, Mingyang Wang!

# post的用法 upload image
file = {'uploadFile':open('1.png','rb')}
i = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(i.text)
# The file 1.png has been uploaded.

# post的用法 登录 网页功能是坏的
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)

# Hey Morvan! Looks like you're still logged into the site!
