#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):

    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        github_url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (github_url.format(i) for i in range(1,5))

    def parse(self, response):
        for content in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            yield {
                    "name": content.xpath('.//div[1]/h3/a[@iterprop="name codeRepository"]/text()').re_first("(\w+)"),
                    "update_time": content.xpath('.//div[3]/relative-time/@datatime/text()').extract_first()
                    }
