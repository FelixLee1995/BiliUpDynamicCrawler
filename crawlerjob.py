import service
import access

def dynamicCrawler(interval, startTimeStamp, upList):
    for up in upList:
        end = service.getEndTimeStamp(up['bilimid'], startTimeStamp)
        access.accessDynamicByUp(up['bilimid'], end)

