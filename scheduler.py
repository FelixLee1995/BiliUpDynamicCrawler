import schedule
import time
import loadconf
from crawlerjob import dynamicCrawler


def job():
    print("CrawlerJob starts at " + str(time.time()))
    dynamicCrawler(loadconf.loadInterval(), loadconf.loadStartTimeStamp(), loadconf.loadUpList())
    print("CrawlerJob ends at " + str(time.time()))


schedule.every(loadconf.loadInterval()).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
