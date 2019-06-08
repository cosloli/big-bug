import common
# import crawler
from crawler import *
from collections.abc import Iterable, Callable
from contextlib import contextmanager

# tmp
import os
import random

class CrawlerServer:
    '''
        提供爬虫服务
        （访问数据库，调用爬虫）
    '''
    def __init__(self):
        self.C = CrawlerService(self.save_fn)
        pass

    @contextmanager
    def run_crawler(self):
        '''
            CrawlerService 的上下文管理器
            优势是出错后能跳到__exit__部分把关闭工作给做了
        '''
        self.C.start()
        yield
        self.C.close()
            

    def add_crawl_job(self, core: CrawlJobCore):
        self.C.add_crawl_job(core)

    def add_urls(self, crawl_job_name: str, urls: Iterable):
        self.C.add_urls(crawl_job_name, urls)

    def save_fn(self,
                crawl_job_core: CrawlJobCore,
                url: str,
                result_list: list):
        '''
            该函数用于保存爬取的数据
        '''
        '''
            TODO 现在这里只是临时的函数
        '''
        d = "tmptmptmp"
        if not os.path.exists(d):
            os.mkdir(d)
        core_name = crawl_job_core.name
        path=os.path.join(d,core_name + url.split("/")[2])+str(random.randint(0,10000))+".txt"
        with open(path,"w") as fw:
            fw.write(str(result_list))
        pass