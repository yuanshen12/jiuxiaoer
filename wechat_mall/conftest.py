import requests

num = requests.get('https://nn.jiuxiaoer.cn')
print(num.text)
