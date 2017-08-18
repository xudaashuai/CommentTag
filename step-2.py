import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
import json
from sklearn import metrics

# 打开词向量json数据 - 来自百度大脑api
of = open('w2c.json', encoding='utf-8')
w2c_data = json.loads(of.read())
data = []
# 转化成list形式，方便聚类
for (k, v) in w2c_data.items():
    data.append(v)
    data[-1].append(k)
# 储存结果
r = {}
# 使用20 - 500 个聚类核心分别聚类
for k in range(20, 500):
    print(k)
    kmeans = KMeans(n_clusters=k)
    t = [x[:-1] for x in data]
    # 聚类并输出聚类结果
    ans = kmeans.fit_predict(t)
    # 计算loss
    loss = metrics.calinski_harabaz_score(t, ans)
    # 将聚类结果转化成列表形式
    res = [[] for x in range(k)]
    for (i, t) in enumerate(ans):
        res[t].append(data[i][-1])
    r[k] = {
        'words': res,
        'loss': loss,
    }
# 保存结果
oof = open('k-means-result.json', 'w+', encoding='utf-8')
oof.write(json.dumps(r, ensure_ascii=False))
oof.flush()
