import requests
from pyquery import PyQuery as pq
import re

url = 'https://www.zhihu.com/explore'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/74.0.3724.8 Safari/537.36'
}

html = requests.get(url=url,headers=headers).text
doc = pq(html)
items = doc('.explore-tab .explore-feed.feed-item').items()

for item in items:
    question = '问题：'+item.find('.question_link').text()
    author = '作者：'+item.find('.author-link').text()
    answer = '评论:\n'+pq(item.find('.content').html()).text()
    file = open('..\\explore.txt','a',encoding='utf-8')
    file.write('\n\n'.join([question,author,answer]))
    file.write('\n' + '-' * 150 +'\n')
    file.close()