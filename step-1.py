# coding:utf-8
# Created by xudas on 2017/6/12.
from aip import AipNlp as Nlp

"""
输入 comments.txt 
    一行为一句评论的txt文件
输出 dict.txt 
    每一行的开头是属性词，后面的词是对这个词的形容词（不重复）
以上
"""
# change to your
client = Nlp('app-id', 'app-key', 'app-secret')


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
    result, no_result_count = get_words()
    print result
    print no_result_count
    f = open('dict.txt', 'w+')
    for x in result:
        f.write(x)
        f.write(' ')
        for t in result[x]:
            f.write(t)
            f.write(' ')
        f.write('\n')
    f.flush()
    f.close()
