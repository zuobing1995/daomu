# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item

class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,spider):
        imagelink=item["imglink"]
    #1. 获取图片的链接

    #2. 向图片的链接发请求,响应会保存在settings.pyzhong 
    # IMAGES_STORE路径中
        yield scrapy.Request(imagelink)

