# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.spiders import CrawlSpider

from .. import items


class CrawlerSpider(CrawlSpider):
    name = 'crawler'

    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.allowed_domains = [self.domain]
        self.category_dict = {
            '메이플스토리 인벤 자유게시판': 1,
            '메이플스토리 인벤 메이플에 바란다 게시판': 2
        }

    def start_requests(self):
        for i in range(1, 2):  # 페이지 하나씩 넘어가기
            yield scrapy.Request(self.url + str(i), self.parse_board)

    def parse_board(self, response):  # 페이지에 있는 게시물 전체 가져오기
        board = response.xpath('//tr[contains(@class, "ls") and contains(@class, "tr")]')

        for i in range(len(board)):
            # 페이지마다 있는 게시물의 href에 접속해서 제목, 내용, 추천수, 조회수 가져오기
            self.post_url = response.xpath('//tr[contains(@class, "ls") and contains(@class, "tr")]/td[@class="bbsSubject"]/a[@class="sj_ln"]/@href')[i].extract()
            yield scrapy.Request(self.post_url, self.parse_post)

    def get_num(self, s):
        regex = re.compile(r'\d{1,3}[,{1}\d{3}]*')
        num = regex.search(s)
        start, end = list(num.span())[0], list(num.span())[1]
        s = s[start:end]
        s_list = s.split(',')
        result = ''
        for n in s_list:
            result += n
        return int(result)

    def get_str(self, s_list):
        result = ''
        for s in s_list:
            result += s
        return result

    def parse_post(self, response):
        item = items.ScrapyAppItem()
        item['title'] = response.xpath('//*[@id="tbArticle"]/div[3]/div[1]/div[1]/h1/text()')[0].extract()
        item['contents'] = self.get_str(response.xpath('//*[@id="imageCollectDiv"]//div/text()|'
                                                       '//*[@id="imageCollectDiv"]//font/text()|'
                                                       '//*[@id="imageCollectDiv"]//p/text()|'
                                                       '//*[@id="imageCollectDiv"]//span/text()|'
                                                       '//*[@id="imageCollectDiv"]//strong/text()').extract())
        item['published_date'] = response.xpath('//*[@id="tbArticle"]/div[1]/div/div[2]/text()')[0].extract()
        item['views'] = self.get_num(response.xpath('//*[@id="tbArticle"]/div[1]/div/div[3]/text()')[1].extract())
        item['recommends'] = response.xpath('//*[@id="bbsRecommendNum1"]/text()')[0].extract()
        item['url'] = response.xpath('//*[@id="viewUrl"]/text()')[0].extract()
        category = response.xpath('//div[@class="viewTopBoardName"]/a/text()')[0].extract()
        for k, v in self.category_dict.items():
            if k == category:
                item['category'] = v

        yield item
