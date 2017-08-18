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
                    print(result)
            else:
                for item in response['items']:
                    print(item['prop'], item['adj'])
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
                print(i / 100, success_count, no_result_count, error_count)
                before = success_count

    print('finish', success_count, no_result_count, error_count)
    return result, no_result_count


if __name__ == '__main__':
    #result, no_result_count = get_words()
    #print result
    result={'\u5957\u9910': set(['\u4fbf\u5b9c']), '\u80a5\u80a0': set(['\u4e0d\u9519']), '\u51fa\u54c1': set(['\u7cbe\u81f4']), '\u70e7\u70e4': set(['\u597d\u5403']), '\u9c8d\u9c7c': set(['\u5c0f']), '\u559d': set(['\u5f88\u597d']), '\u83dc\u5473\u9053': set(['\u8fd8\u53ef\u4ee5', '\u4e0d\u9519']), '\u5149\u7ebf': set(['\u660f\u6697']), '\u7530\u87ba': set(['\u597d\u5403']), '\u4e1c\u897f': set(['\u96be\u5403', '\u5f88\u597d', '\u4e00\u822c', '\u8d35', '\u597d\u5403', '\u591a', '\u4e0d\u9519']), '\u5730\u65b9': set(['\u633a\u597d']), '\u9009\u62e9': set(['\u591a']), '\u597d\u5403': set(['\u4e0d\u8d35']), '\u5238': set(['\u5212\u7b97']), '\u725b\u8169': set(['\u4e0d\u9519']), '\u4e0a\u83dc': set(['\u6162']), '\u670d\u52a1': set(['\u4e5f\u597d', '\u8fd8\u597d', '\u5f88\u597d']), '\u670d\u52a1\u4e1a': set(['\u4e0d\u9519']), '\u70e7\u9ea6': set(['\u597d\u5403']), '\u83dc\u54c1': set(['\u6f02\u4eae', '\u7cbe\u81f4', '\u65b0\u9c9c']), '\u9505\u5e95': set(['\u4e0d\u9519']), '\u7092\u996d': set(['\u597d\u5403']), '\u73af\u5883\u5473\u9053': set(['\u8fd8\u53ef\u4ee5']), '\u79cd\u7c7b': set(['\u4e0d\u591a']), '\u9910\u5385': set(['\u8fd8\u53ef\u4ee5']), '\u996e\u54c1\u5473\u9053': set(['\u8fd8\u53ef\u4ee5']), '\u603b\u4f53\u611f\u89c9': set(['\u4e0d\u9519']), '\u6001\u5ea6': set(['\u5f88\u597d', '\u4e0d\u9519', '\u4e00\u822c', '\u4e0d\u70ed\u60c5', '\u4eb2\u5207', '\u4e0d\u597d', '\u597d']), '\u6750\u6599': set(['\u4e0d\u65b0\u9c9c']), '\u8089\u8d28': set(['\u5f88\u597d']), '\u4efd\u91cf': set(['\u9002\u4e2d', '\u8db3', '\u5c0f']), '\u51c9\u9762': set(['\u597d\u5403']), '\u5403': set(['\u4e0d\u597d', '\u8fd8\u53ef\u4ee5', '\u4e0d\u9519', '\u4e00\u822c']), '\u5c0f\u4f19\u4f34': set(['\u4e00\u8d77']), '\u51e4\u722a': set(['\u597d\u5403']), '\u867e\u5473\u9053': set(['\u975e\u5e38\u597d', '\u4e00\u822c']), '\u4e0a\u9910': set(['\u6162']), '\u8fd8\u4f1a': set(['\u518d\u6765', '\u6765', '\u518d\u53bb']), '\u53e3\u5473': set(['\u4e5f\u597d', '\u591a', '\u6e05\u6de1', '\u8d5e']), '\u6392\u9aa8': set(['\u597d\u5403']), '\u5927\u4f17\u70b9\u8bc4': set(['\u7ed9\u529b']), '\u670d\u52a1\u6001\u5ea6': set(['\u4e5f\u597d', '\u8fd8\u884c', '\u5f88\u597d', '\u4e00\u822c', '\u5dee', '\u633a\u597d', '\u597d']), '\u670b\u53cb': set(['\u805a\u9910']), '\u4e1c\u897f\u611f\u89c9': set(['\u4e0d\u65b0\u9c9c']), '\u5927\u867e': set(['\u4e00\u822c']), '\u8bc4\u4ef7': set(['\u8fd8\u53ef\u4ee5']), '\u725b\u6392': set(['\u4e0d\u719f']), '\u9762\u6761': set(['\u597d\u5403']), '\u54c1\u79cd': set(['\u5355\u4e00', '\u4e30\u5bcc']), '\u4f4d\u7f6e': set(['\u597d\u627e', '\u5bbd\u655e']), '\u82b1\u751f': set(['\u9999']), '\u9171\u6599\u5473\u9053': set(['\u597d']), '\u571f\u8c46': set(['\u597d\u5403']), '\u9cb6\u9c7c': set(['\u4e0d\u9519']), '\u670d\u52a1\u5458\u670d\u52a1\u6001\u5ea6': set(['\u5f88\u597d']), '\u7ae0\u9c7c': set(['\u4e0d\u9519']), '\u88c5\u4fee': set(['\u6f02\u4eae', '\u5f88\u597d']), '\u670d\u52a1\u4eba\u5458': set(['\u70ed\u60c5', '\u4e00\u822c']), '\u4e0a\u83dc\u901f\u5ea6': set(['\u5feb', '\u7ed9\u529b']), '\u996d': set(['\u4e0d\u592a\u597d\u5403']), '\u53a8\u5e08\u624b\u827a': set(['\u5dee\u52b2']), '\u4ea4\u901a': set(['\u65b9\u4fbf']), '\u9f99\u867e': set(['\u597d\u5403']), '\u56e2\u8d2d\u4ef7\u683c': set(['\u4fbf\u5b9c']), '\u9992\u5934': set(['\u597d\u5403']), '\u56e2\u8d2d': set(['\u5212\u7b97', '\u7ed9\u529b', '\u8fd8\u53ef\u4ee5', '\u8d35', '\u65b9\u4fbf', '\u591a', '\u4e0d\u9519']), '\u6247\u8d1d': set(['\u597d\u5403']), '\u9910': set(['\u6162']), '\u9178\u9178': set(['\u8fa3\u8fa3', '\u751c\u751c']), '\u82b1\u751f\u7c73': set(['\u9999']), '\u7092\u9e21': set(['\u597d\u5403']), '\u4ef7\u683c': set(['\u5f88\u597d', '\u4e0d\u4f4e', '\u5c0f', '\u4e0d\u8d35', '\u5408\u9002', '\u8d35', '\u5b9e\u60e0']), '\u56e2\u8d2d\u5238': set(['\u5212\u7b97']), '\u8089\u7c7b': set(['\u4e0d\u9519']), '\u70e4\u8089': set(['\u8fd8\u53ef\u4ee5']), '\u54c1\u8d28': set(['\u8fd8\u884c']), '\u901f\u5ea6': set(['\u7ed9\u529b', '\u6162', '\u5feb']), '\u6d77\u9c9c': set(['\u65b0\u9c9c']), '\u670d\u52a1\u5458\u6001\u5ea6': set(['\u633a\u597d', '\u5f88\u597d']), '\u5e74\u7cd5': set(['\u597d\u5403']), '\u91cf': set(['\u5c11', '\u8db3']), '\u82b1\u7532': set(['\u4e0d\u65b0\u9c9c']), '\u611f\u89c9': set(['\u4e0d\u65b0\u9c9c', '\u4e0d\u9519']), '\u8fa3\u6912': set(['\u4e0d\u9519']), '\u83dc\u8272': set(['\u4e0d\u9519', '\u7cbe\u81f4']), '\u9505\u5e95\u5473\u9053': set(['\u5f88\u597d']), '\u5e97\u9762': set(['\u4e0d\u884c', '\u4e0d\u9519', '\u5dee']), '\u4e09\u6587\u9c7c': set(['\u65b0\u9c9c']), '\u5c31\u9910\u73af\u5883': set(['\u5f88\u597d']), '\u86cb\u7cd5': set(['\u597d\u5403']), '\u725b\u6392\u5473\u9053': set(['\u4e0d\u9519']), '\u8001\u677f\u6001\u5ea6': set(['\u633a\u597d']), '\u867e': set(['\u4e0d\u9519', '\u65b0\u9c9c', '\u597d\u5403']), '\u4e00\u5982': set(['\u65e2\u5f80']), '\u5730\u7406\u4f4d\u7f6e': set(['\u5f88\u597d']), '\u6446\u76d8': set(['\u597d\u770b']), '\u98df\u6750': set(['\u8fd8\u884c', '\u65b0\u9c9c']), '\u751f\u610f': set(['\u4e0d\u9519']), '\u6027\u4ef7\u6bd4': set(['\u9ad8', '\u8fd8\u884c', '\u4f4e']), '\u9762\u5473\u9053': set(['\u4e0d\u9519']), '\u5bff\u53f8\u5473\u9053': set(['\u4e0d\u9519']), '\u603b\u4f53\u5370\u8c61': set(['\u4e0d\u9519']), '\u6298\u6263': set(['\u5c0f']), '\u62ab\u8428': set(['\u597d\u5403']), '\u540c\u4e8b': set(['\u4e00\u8d77']), '\u670d\u52a1\u73af\u5883': set(['\u4e00\u822c']), '\u83dc\u54c1\u5473\u9053': set(['\u4e0d\u9519']), '\u4e00\u5bb6': set(['\u8fd8\u4e0d\u9519']), '\u4eba\u5458': set(['\u70ed\u60c5']), '\u7a7a\u8c03': set(['\u4e0d\u7ba1\u7528']), '\u997c': set(['\u597d\u5403']), '\u5473\u9053': set(['\u8fa3', '\u5f88\u8d5e', '\u8fd8\u884c', '\u68d2\u68d2', '\u5f88\u597d', '\u6b63\u5b97', '\u4e5f\u597d', '\u4e00\u822c', '\u8fd8\u4e0d\u9519', '\u786e\u5b9e', '\u8fd8\u597d', '\u54b8', '\u5dee\u52b2', '\u4e0d\u9519', '\u751c', '\u8d5e']), '\u9e2d\u638c': set(['\u597d\u5403']), '\u725b\u8089\u997c': set(['\u597d\u5403']), '\u73af\u5883': set(['\u8fd8\u884c', '\u5f88\u597d', '\u9ad8\u5927', '\u4e00\u822c', '\u5dee', '\u633a\u597d', '\u8fd8\u597d', '\u975e\u5e38\u597d', '\u4e0d\u9519']), '\u8c03\u6599': set(['\u4e0d\u884c']), '\u5976\u8336': set(['\u4e0d\u9519']), '\u725b\u8089': set(['\u5ae9']), '\u828b\u5706': set(['\u597d\u5403']), '\u9001\u8d27': set(['\u53ca\u65f6']), '\u6c34\u5e73': set(['\u9ad8']), '\u4ef7\u5ec9': set(['\u7269\u7f8e']), '\u725b\u8089\u6c64': set(['\u5f88\u597d']), '\u867e\u5b50': set(['\u4e0d\u7b97\u5c0f', '\u597d\u5403']), '\u53e3\u611f': set(['\u4e0d\u9519']), '\u9e21\u7fc5': set(['\u4e0d\u592a\u597d\u5403']), '\u867e\u7403': set(['\u8fd8\u4e0d\u9519']), '\u8c46\u76ae': set(['\u597d\u5403'])}
    f = open('dict.txt', 'w+')
    for x in result:
        #f.write(x)
        print(x, end=' ')
        f.write(' ')
        print(' '.join(result[x]))
        continue
        for t in result[x]:
            #f.write(t)
            print(t)
            f.write(' ')
        f.write('\n')
    f.flush()
    f.close()
