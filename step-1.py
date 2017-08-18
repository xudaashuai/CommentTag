# coding:utf-8
# Created by xudas on 2017/6/12.
from  aip import AipNlp as Nlp

"""
输入 comments.txt 
    一行为一句评论的txt文件
输出 dict.txt 
    每一行的开头是属性词，后面的词是对这个词的形容词（不重复）
以上
"""
# change to your
sk='T80yWu0WAkbOFoKRVQ9p8lZMzj6rLq7S'
client = Nlp('9688683', 'wndZFKVBmUTM5cfMb7C8UaOA', 'T80yWu0WAkbOFoKRVQ9p8lZMzj6rLq7S')
response = client.commentTag('超爱你的')

print(response)
exit()


