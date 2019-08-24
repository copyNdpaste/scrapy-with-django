# CrawlerWithScrapyAndDjango

CrawlerWithScrapyAndDjango. This crawler crawling posts of board.

Site urls are below. 'p' parameter means page.

http://www.inven.co.kr/board/maple/2299?p=

http://www.inven.co.kr/board/maple/2587?p=

### Set up

#### install requirements

`pip install -r requirements.txt`

#### database

`python manage.py migrate`

### Start Project

run django and scrapyd

#### run django

`python manage.py runserver`

#### run scrapyd

`cd scrapy_app`

`scrapyd`

send a job request to scrapyd. spider is assigned `spider name`

`curl http://localhost:6800/schedule.json -d project=default -d spider=crawler`

### Initial screen

![1566569741353](C:\Users\julsn\AppData\Roaming\Typora\typora-user-images\1566569741353.png)

### How to use

1. Select option `바란다 게시판` or `자유 게시판`.
2. Click the blue button `크롤링 시작`.
3. Wait until crawling is finished.
4. Check the crawled data on the table.
5. If you want to Check all data click the emerald button `전체보기`
6. If you want to visit original page, click the title that is hyper linked.

### After crawling

![1566570351664](C:\Users\julsn\AppData\Roaming\Typora\typora-user-images\1566570351664.png)



##### from 

https://github.com/adriancast/Scrapyd-Django-Template, https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e
