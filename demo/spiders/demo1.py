# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import random

from demo.items import Demo1Item


# class Demo1Spider(scrapy.Spider):
#     name = 'shaiwu'
#     # allowed_domains = ['smzdm.com']
#     start_urls = ["http://post.smzdm.com"]
#     def parse(self, response):
#         filename = 'response.txt'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#
#         for sel in response.xpath('//li[@class="list"]'):
#
#             # filename = 'items.txt'
#             # with open(filename, 'a') as f:
#             #     print('###'+sel)
#             #     f.write(sel+'\n')
#             item = Demo1Item()
#             item['title'] = sel.xpath('div[@class="item-info-box"]/h2[@class="item-name"]/a[@target="_blank"]/text()').extract()[0]
#             item['desc'] = sel.xpath('div[@class="item-info-box"]/p[@class="item-info"]/text()').extract()[0]
#             item['link'] = sel.xpath('a[@class="item-pic"]/img/@src').extract()[0]
#             print(type(item['link']))
#             yield item
#             print("--------------------\n")
#             print(item["title"])
#             print(item['desc'])
#             print(item['link'])
#             print("--------------------\n")
#
#             filename = 'items.txt'
#             with open(filename, 'a') as f:
#                 f.write("title: "+item["title"]+"\n"+
#                         "desc:  "+item["desc"]+"\n"+
#                         "link:  "+item['link']+'\n\n')


# class Demo1Spider(scrapy.Spider):
#     name = 'shaiwu'
#     start_urls = ['https://www.485tv.com/Html/88/index-14.html',
#                   'https://www.485tv.com/Html/88/index-15.html',
#                   'https://www.485tv.com/Html/88/index-16.html',
#                   'https://www.485tv.com/Html/88/index-17.html',
#                   'https://www.485tv.com/Html/88/index-18.html',
#                   'https://www.485tv.com/Html/88/index-19.html',
#                   'https://www.485tv.com/Html/88/index-20.html'
#                   'https://www.485tv.com/Html/88/index-21.html'
#                   'https://www.485tv.com/Html/88/index-22.html'
#                   'https://www.485tv.com/Html/88/index-23.html'
#                   'https://www.485tv.com/Html/88/index-24.html'
#                   'https://www.485tv.com/Html/88/index-25.html'
#                   'https://www.485tv.com/Html/88/index-26.html',
#                   'https://www.485tv.com/Html/88/index-27.html'
#                   'https://www.485tv.com/Html/88/index-28.html'
#                   'https://www.485tv.com/Html/88/index-29.html'
#                   'https://www.485tv.com/Html/88/index-30.html']
#     print('---------- start -----------')
#
#
#     def parse(self, response):
#         print('---------- parse -----------')
#         # print(response.body)
#         baseurl = 'https://485tv.com'
#         res = []
#         for sel in response.xpath('//li/a/@href').extract():
#             print('# %s' % sel)
#             item = baseurl+sel
#             filename = 'items.txt'
#             with open(filename, 'a') as f:
#                 f.write(item+'\n')
#                 res.append(item)
#
#         print('='*100)
#         print(res)
#         print('=' * 100)


class Demo1Spider(scrapy.Spider):
    name = 'shaiwu'

    with open('items.txt', 'r') as f:
        items = f.readlines()
        items1 = []
        for item in items:
            if item.find('\n') != -1:
                item = item[:-1]
            items1.append(item)
        print(items)
    start_urls = items1
    print('---------- start -----------')

    def progress(self, blk, blk_size, total_size):
        print('下载中... %d/%d  %.2f' % (blk * blk_size, total_size, (float)(blk * blk_size * 100 / total_size)))

    def parse(self, response):
        print('---------- parse -----------')

        downloadUrls = []
        for sel in response.xpath('//a/@href').extract():
            if sel.find('mp4') != -1:
                print(sel)
                with open('downloadurls.txt', 'a') as f1:
                    f1.write(sel+'\n')
                    downloadUrls.append(sel)

        #             下载
                    filename = 'mv/'+str(random.randint(1, 10000))+'.mp4'
                    urllib.request.urlretrieve(sel, filename, reporthook=self.progress)
                    break

