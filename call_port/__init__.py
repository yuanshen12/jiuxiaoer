import requests

r = requests.get('https://m.jiuxiao2.cn/shop/adveryt-pic')

print(r.raise_for_status, end=' ')