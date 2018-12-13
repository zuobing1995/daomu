# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    baseUrl='http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset=0
    start_urls = [baseUrl+str(offset)]

    def parse(self, response):
        item=DouyuItem()
        #先把响应转成python格式
        res=json.loads(response.text)
        #得到所有主播信息
        #如果r_list为空,表示爬取完毕
        r_list=res['data']
        if not r_list:
            return
        for i in r_list:
            item['imglink']=i['vertical_src']
            item['nickname']=i['nickname']
            item['cityname']=i['anchor_city']

            yield item

        #实现翻页功能
        self.offset+=20
        yield scrapy.Request(self.baseUrl+str(self.offset),
            callback=self.parse)
