from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from CommentTag.MyScrapyRedis.spiders import RedisCrawlSpider
import json
from scrapy.utils.serialize import ScrapyJSONEncoder
import pymongo

connection = pymongo.MongoClient('120.25.75.23', 27017)
tdb = connection.test
post = tdb.comments


class BSpider(RedisCrawlSpider):
    name = 'b'
    redis_key = 'b:start_ids'
    user_info_url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag?access_token={0}&text={1}"
    token = 'T80yWu0WAkbOFoKRVQ9p8lZMzj6rLq7S'

    def __init__(self, *a, **kwargs):
        super().__init__(*a, **kwargs)

    def make_request_from_data_str(self, data_str):
        text=post.find_one({'_id':data_str})['text']
        try:
            return Request(url=self.datastr_to_url(data_str), meta={'id': data_str}, dont_filter=False)
        except Exception as e:
            print(e)

    def datastr_to_url(self, data_str):
        return self.user_info_url.format(self.token, data_str.decode('utf-8').encode('GBK'))

    def parse(self, response):
        user_info_json = None
        if isinstance(response.body,bytes):
            user_info_json =json.loads( response.body.decode('utf-8'))
        else:
            user_info_json = json.loads(response.body)
        user_info_json['_id'] = user_info_json['id']
        post.update({"_id": user_info_json['_id']}, {"$setOnInsert":user_info_json}, upsert=True)
