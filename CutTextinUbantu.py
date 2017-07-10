import psycopg2,random
import jieba
import string
import re

conn = psycopg2.connect("dbname=postgres user=postgres port=5439 password=123456")
cur=conn.cursor()
cur.execute("select text from meituan_comments")
result2=cur.fetchall()
file=open('result.txt','w',encoding='UTF-8')
Rs2=[]
regex=re.compile('[%s]' % re.escape('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，-。╮╯◇？、·【〜～~@#￥%……&*（）]+'))
a=1
for i in range(len(result2)):
    try:
        result= []
        if not result2[i]:
            continue
        str2="".join(result2[i])
        print(str2)
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
    except:
        print ('error')
        continue
file.close()

