# coding=utf-8
import psycopg2,random
import jieba
import string
import re

conn = psycopg2.connect("dbname=postgres user=postgres port=5439 password=123456")
cur=conn.cursor()
cur.execute("select commentbody from comment")
result=cur.fetchall()
file=open('/home/hygwork/result2.txt','w',encoding='UTF-8')
Rs2=[]
regex=re.compile('[%s]' % re.escape('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，-。╮╯◇？、·【〜～~@#￥%……&*（）]+'))
a=1
for i in range(len(result)):
    result=[]
    str2=result[i]
    m=regex.sub('',str2)
    print(m)
    seg_list = jieba.cut(m)
    for w in seg_list :
        result.append(w)
    for x in result:
        file.write(x)
        file.write(' ')
    print('the '+str(a) +' row\n')
    a=a+1
file.close()


