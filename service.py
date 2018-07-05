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
    d1 = dynamic['desc']
    d1['card'] = dynamic['card']
    print(d1)
    key = {'dynamic_id': dynamic['desc']['dynamic_id']}
    dycol = db['dynamic']
    dycol.update(key, d1, upsert=True)

