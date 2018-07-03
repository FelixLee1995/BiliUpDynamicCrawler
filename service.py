from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['dynamic']


def getEndTimeStamp(upid, originTime):
    upinfo = db['upinfo']
    up= upinfo.find_one({"bilimid": upid})
    if up and up['updatetime']:
        if up['updatetime'] > originTime:
            return up['updatetime']
    return originTime



def insertDynamic(dynamic):
    upinfo