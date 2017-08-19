from  aip import AipNlp as Nlp
import pymongo, redis,re

connection = pymongo.MongoClient('120.25.75.23', 27017)
tdb = connection.test
post = tdb.comments
#client = redis.Redis(host='101.236.6.203', port=6379, db=0,password='19980819')

nlp = Nlp('9688683', 'wndZFKVBmUTM5cfMb7C8UaOA', 'T80yWu0WAkbOFoKRVQ9p8lZMzj6rLq7S')
for i in range(100):
    r = post.find().limit(10000)
    t=[]
    for k, item in enumerate(r):
        if r['propadj'] ==None or r['pro'] ==None:
            continue
        print(k)
        if not item['text']:
            continue
        text=item['text'].replace('#','')
        r=nlp.commentTag(text)
        if 'error_code' in item:
            if r['error_code'] !=282130:
                print(r)
        propadj={}
        if 'items' in r:
            for it in r['items']:
                propadj[it['prop']]=it['adj']
        post.update({"_id": item['_id']}, {"$set": {"propadj": propadj,'pro':True}})
    print(i)