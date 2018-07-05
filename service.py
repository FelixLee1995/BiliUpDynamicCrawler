from pymongo import MongoClient
import pymongo
import loadconf

client = MongoClient(loadconf.loadMongoUrl())

db = client['dynamic']


def getEndTimeStamp(upid, originTime):
    upinfo = db['upinfo']
    up= upinfo.find_one({"uid": upid})
    if up and up['updatetime']:
        if up['updatetime'] > originTime:
            return up['updatetime']
    return originTime



def insertDynamic(dynamic):
    d1 = dynamic['desc']
    d1['card'] = dynamic['card']
    key = {'dynamic_id': dynamic['desc']['dynamic_id']}
    dycol = db['dynamic']
    dycol.update(key, d1, upsert=True)


def refreshUpdateTime(upid):
    dycol = db['dynamic']
    key = {'uid': upid}
    res = dycol.find(key).sort('timestamp', pymongo.DESCENDING).limit(1)
    if res.count() > 0:
        time = res[0]['timestamp']
    upcol = db['upinfo']
    data = {'updatetime': time, 'uid': upid}
    upcol.update(key, data, upsert=True)

