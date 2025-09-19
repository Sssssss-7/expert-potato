import requests
from bs4 import BeautifulSoup
url = "https://www.python.org"
response = requests.get(url)

print("原始HTML前200字：\n", response.text[:200])

soup = BeautifulSoup(response.text,"html.parser")

print("标题对象：",soup.title)

print("第一个链接：",soup.find('a'))

print("网页标题",soup.title.string)
for link in soup.find_all('a')[:5]:
    print("链接",link.get("href"))
