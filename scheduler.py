import schedule
import time
import loadconf
from crawlerjob import dynamicCrawler



def job():
    print("CrawlerJob starts at " + str(time.time()))
    dynamicCrawler(loadconf.loadInterval(), loadconf.loadStartTimeStamp(), loadconf.loadUpList())


schedule.every(loadconf.loadInterval()).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
