import service

def dynamicCrawler(interval, startTimeStamp, upList):
    for up in upList:
        end = service.getEndTimeStamp(up['bilimid'], startTimeStamp)


