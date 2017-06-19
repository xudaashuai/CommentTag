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
client = Nlp('9688683', 'wndZFKVBmUTM5cfMb7C8UaOA', 'T80yWu0WAkbOFoKRVQ9p8lZMzj6rLq7S')


def get_words():
    success_count = 0
    result = {}
    no_result_count = 0
    before = -100
    error_count = 0
    comments_file = open('comments.txt')
    comments = comments_file.readlines()
    for i, text in enumerate(comments):
        try:
            response = client.commentTag(text)
            if 'error_code' in response:
                if response['error_code'] == 282130:
                    no_result_count += 1
                else:
                    error_count += 1
                    print result
            else:
                for item in response['items']:
                    print item['prop'], item['adj']
                    if item['prop'] not in result:
                        result[item['prop']] = set()
                    result[item['prop']].add(item['adj'])
                    success_count += 1
        except Exception as e:
            error_count += 1
        finally:
            if i % 100 == 0:
                if before == success_count:
                    break
                print i / 100, success_count, no_result_count, error_count
                before = success_count

    print 'finish', success_count, no_result_count, error_count
    return result, no_result_count


if __name__ == '__main__':
    #result, no_result_count = get_words()
    #print result
    result={u'\u5957\u9910': set([u'\u4fbf\u5b9c']), u'\u80a5\u80a0': set([u'\u4e0d\u9519']), u'\u51fa\u54c1': set([u'\u7cbe\u81f4']), u'\u70e7\u70e4': set([u'\u597d\u5403']), u'\u9c8d\u9c7c': set([u'\u5c0f']), u'\u559d': set([u'\u5f88\u597d']), u'\u83dc\u5473\u9053': set([u'\u8fd8\u53ef\u4ee5', u'\u4e0d\u9519']), u'\u5149\u7ebf': set([u'\u660f\u6697']), u'\u7530\u87ba': set([u'\u597d\u5403']), u'\u4e1c\u897f': set([u'\u96be\u5403', u'\u5f88\u597d', u'\u4e00\u822c', u'\u8d35', u'\u597d\u5403', u'\u591a', u'\u4e0d\u9519']), u'\u5730\u65b9': set([u'\u633a\u597d']), u'\u9009\u62e9': set([u'\u591a']), u'\u597d\u5403': set([u'\u4e0d\u8d35']), u'\u5238': set([u'\u5212\u7b97']), u'\u725b\u8169': set([u'\u4e0d\u9519']), u'\u4e0a\u83dc': set([u'\u6162']), u'\u670d\u52a1': set([u'\u4e5f\u597d', u'\u8fd8\u597d', u'\u5f88\u597d']), u'\u670d\u52a1\u4e1a': set([u'\u4e0d\u9519']), u'\u70e7\u9ea6': set([u'\u597d\u5403']), u'\u83dc\u54c1': set([u'\u6f02\u4eae', u'\u7cbe\u81f4', u'\u65b0\u9c9c']), u'\u9505\u5e95': set([u'\u4e0d\u9519']), u'\u7092\u996d': set([u'\u597d\u5403']), u'\u73af\u5883\u5473\u9053': set([u'\u8fd8\u53ef\u4ee5']), u'\u79cd\u7c7b': set([u'\u4e0d\u591a']), u'\u9910\u5385': set([u'\u8fd8\u53ef\u4ee5']), u'\u996e\u54c1\u5473\u9053': set([u'\u8fd8\u53ef\u4ee5']), u'\u603b\u4f53\u611f\u89c9': set([u'\u4e0d\u9519']), u'\u6001\u5ea6': set([u'\u5f88\u597d', u'\u4e0d\u9519', u'\u4e00\u822c', u'\u4e0d\u70ed\u60c5', u'\u4eb2\u5207', u'\u4e0d\u597d', u'\u597d']), u'\u6750\u6599': set([u'\u4e0d\u65b0\u9c9c']), u'\u8089\u8d28': set([u'\u5f88\u597d']), u'\u4efd\u91cf': set([u'\u9002\u4e2d', u'\u8db3', u'\u5c0f']), u'\u51c9\u9762': set([u'\u597d\u5403']), u'\u5403': set([u'\u4e0d\u597d', u'\u8fd8\u53ef\u4ee5', u'\u4e0d\u9519', u'\u4e00\u822c']), u'\u5c0f\u4f19\u4f34': set([u'\u4e00\u8d77']), u'\u51e4\u722a': set([u'\u597d\u5403']), u'\u867e\u5473\u9053': set([u'\u975e\u5e38\u597d', u'\u4e00\u822c']), u'\u4e0a\u9910': set([u'\u6162']), u'\u8fd8\u4f1a': set([u'\u518d\u6765', u'\u6765', u'\u518d\u53bb']), u'\u53e3\u5473': set([u'\u4e5f\u597d', u'\u591a', u'\u6e05\u6de1', u'\u8d5e']), u'\u6392\u9aa8': set([u'\u597d\u5403']), u'\u5927\u4f17\u70b9\u8bc4': set([u'\u7ed9\u529b']), u'\u670d\u52a1\u6001\u5ea6': set([u'\u4e5f\u597d', u'\u8fd8\u884c', u'\u5f88\u597d', u'\u4e00\u822c', u'\u5dee', u'\u633a\u597d', u'\u597d']), u'\u670b\u53cb': set([u'\u805a\u9910']), u'\u4e1c\u897f\u611f\u89c9': set([u'\u4e0d\u65b0\u9c9c']), u'\u5927\u867e': set([u'\u4e00\u822c']), u'\u8bc4\u4ef7': set([u'\u8fd8\u53ef\u4ee5']), u'\u725b\u6392': set([u'\u4e0d\u719f']), u'\u9762\u6761': set([u'\u597d\u5403']), u'\u54c1\u79cd': set([u'\u5355\u4e00', u'\u4e30\u5bcc']), u'\u4f4d\u7f6e': set([u'\u597d\u627e', u'\u5bbd\u655e']), u'\u82b1\u751f': set([u'\u9999']), u'\u9171\u6599\u5473\u9053': set([u'\u597d']), u'\u571f\u8c46': set([u'\u597d\u5403']), u'\u9cb6\u9c7c': set([u'\u4e0d\u9519']), u'\u670d\u52a1\u5458\u670d\u52a1\u6001\u5ea6': set([u'\u5f88\u597d']), u'\u7ae0\u9c7c': set([u'\u4e0d\u9519']), u'\u88c5\u4fee': set([u'\u6f02\u4eae', u'\u5f88\u597d']), u'\u670d\u52a1\u4eba\u5458': set([u'\u70ed\u60c5', u'\u4e00\u822c']), u'\u4e0a\u83dc\u901f\u5ea6': set([u'\u5feb', u'\u7ed9\u529b']), u'\u996d': set([u'\u4e0d\u592a\u597d\u5403']), u'\u53a8\u5e08\u624b\u827a': set([u'\u5dee\u52b2']), u'\u4ea4\u901a': set([u'\u65b9\u4fbf']), u'\u9f99\u867e': set([u'\u597d\u5403']), u'\u56e2\u8d2d\u4ef7\u683c': set([u'\u4fbf\u5b9c']), u'\u9992\u5934': set([u'\u597d\u5403']), u'\u56e2\u8d2d': set([u'\u5212\u7b97', u'\u7ed9\u529b', u'\u8fd8\u53ef\u4ee5', u'\u8d35', u'\u65b9\u4fbf', u'\u591a', u'\u4e0d\u9519']), u'\u6247\u8d1d': set([u'\u597d\u5403']), u'\u9910': set([u'\u6162']), u'\u9178\u9178': set([u'\u8fa3\u8fa3', u'\u751c\u751c']), u'\u82b1\u751f\u7c73': set([u'\u9999']), u'\u7092\u9e21': set([u'\u597d\u5403']), u'\u4ef7\u683c': set([u'\u5f88\u597d', u'\u4e0d\u4f4e', u'\u5c0f', u'\u4e0d\u8d35', u'\u5408\u9002', u'\u8d35', u'\u5b9e\u60e0']), u'\u56e2\u8d2d\u5238': set([u'\u5212\u7b97']), u'\u8089\u7c7b': set([u'\u4e0d\u9519']), u'\u70e4\u8089': set([u'\u8fd8\u53ef\u4ee5']), u'\u54c1\u8d28': set([u'\u8fd8\u884c']), u'\u901f\u5ea6': set([u'\u7ed9\u529b', u'\u6162', u'\u5feb']), u'\u6d77\u9c9c': set([u'\u65b0\u9c9c']), u'\u670d\u52a1\u5458\u6001\u5ea6': set([u'\u633a\u597d', u'\u5f88\u597d']), u'\u5e74\u7cd5': set([u'\u597d\u5403']), u'\u91cf': set([u'\u5c11', u'\u8db3']), u'\u82b1\u7532': set([u'\u4e0d\u65b0\u9c9c']), u'\u611f\u89c9': set([u'\u4e0d\u65b0\u9c9c', u'\u4e0d\u9519']), u'\u8fa3\u6912': set([u'\u4e0d\u9519']), u'\u83dc\u8272': set([u'\u4e0d\u9519', u'\u7cbe\u81f4']), u'\u9505\u5e95\u5473\u9053': set([u'\u5f88\u597d']), u'\u5e97\u9762': set([u'\u4e0d\u884c', u'\u4e0d\u9519', u'\u5dee']), u'\u4e09\u6587\u9c7c': set([u'\u65b0\u9c9c']), u'\u5c31\u9910\u73af\u5883': set([u'\u5f88\u597d']), u'\u86cb\u7cd5': set([u'\u597d\u5403']), u'\u725b\u6392\u5473\u9053': set([u'\u4e0d\u9519']), u'\u8001\u677f\u6001\u5ea6': set([u'\u633a\u597d']), u'\u867e': set([u'\u4e0d\u9519', u'\u65b0\u9c9c', u'\u597d\u5403']), u'\u4e00\u5982': set([u'\u65e2\u5f80']), u'\u5730\u7406\u4f4d\u7f6e': set([u'\u5f88\u597d']), u'\u6446\u76d8': set([u'\u597d\u770b']), u'\u98df\u6750': set([u'\u8fd8\u884c', u'\u65b0\u9c9c']), u'\u751f\u610f': set([u'\u4e0d\u9519']), u'\u6027\u4ef7\u6bd4': set([u'\u9ad8', u'\u8fd8\u884c', u'\u4f4e']), u'\u9762\u5473\u9053': set([u'\u4e0d\u9519']), u'\u5bff\u53f8\u5473\u9053': set([u'\u4e0d\u9519']), u'\u603b\u4f53\u5370\u8c61': set([u'\u4e0d\u9519']), u'\u6298\u6263': set([u'\u5c0f']), u'\u62ab\u8428': set([u'\u597d\u5403']), u'\u540c\u4e8b': set([u'\u4e00\u8d77']), u'\u670d\u52a1\u73af\u5883': set([u'\u4e00\u822c']), u'\u83dc\u54c1\u5473\u9053': set([u'\u4e0d\u9519']), u'\u4e00\u5bb6': set([u'\u8fd8\u4e0d\u9519']), u'\u4eba\u5458': set([u'\u70ed\u60c5']), u'\u7a7a\u8c03': set([u'\u4e0d\u7ba1\u7528']), u'\u997c': set([u'\u597d\u5403']), u'\u5473\u9053': set([u'\u8fa3', u'\u5f88\u8d5e', u'\u8fd8\u884c', u'\u68d2\u68d2', u'\u5f88\u597d', u'\u6b63\u5b97', u'\u4e5f\u597d', u'\u4e00\u822c', u'\u8fd8\u4e0d\u9519', u'\u786e\u5b9e', u'\u8fd8\u597d', u'\u54b8', u'\u5dee\u52b2', u'\u4e0d\u9519', u'\u751c', u'\u8d5e']), u'\u9e2d\u638c': set([u'\u597d\u5403']), u'\u725b\u8089\u997c': set([u'\u597d\u5403']), u'\u73af\u5883': set([u'\u8fd8\u884c', u'\u5f88\u597d', u'\u9ad8\u5927', u'\u4e00\u822c', u'\u5dee', u'\u633a\u597d', u'\u8fd8\u597d', u'\u975e\u5e38\u597d', u'\u4e0d\u9519']), u'\u8c03\u6599': set([u'\u4e0d\u884c']), u'\u5976\u8336': set([u'\u4e0d\u9519']), u'\u725b\u8089': set([u'\u5ae9']), u'\u828b\u5706': set([u'\u597d\u5403']), u'\u9001\u8d27': set([u'\u53ca\u65f6']), u'\u6c34\u5e73': set([u'\u9ad8']), u'\u4ef7\u5ec9': set([u'\u7269\u7f8e']), u'\u725b\u8089\u6c64': set([u'\u5f88\u597d']), u'\u867e\u5b50': set([u'\u4e0d\u7b97\u5c0f', u'\u597d\u5403']), u'\u53e3\u611f': set([u'\u4e0d\u9519']), u'\u9e21\u7fc5': set([u'\u4e0d\u592a\u597d\u5403']), u'\u867e\u7403': set([u'\u8fd8\u4e0d\u9519']), u'\u8c46\u76ae': set([u'\u597d\u5403'])}
    f = open('dict.txt', 'w+')
    for x in result:
        #f.write(x)
        print x,
        f.write(' ')
        print u' '.join(result[x])
        continue
        for t in result[x]:
            #f.write(t)
            print t
            f.write(' ')
        f.write('\n')
    f.flush()
    f.close()
