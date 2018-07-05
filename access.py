import requests
import json
import service


def accessDynamicByUp(bilimid,end):
    offset = '0'
    flag = True
    while flag:
        if offset == -1:
            break
        offset = accessDynamic(bilimid, offset, end)


def accessDynamic(bilimid, offset_dynamicID, end):
    headers = {'Host': 'api.vc.bilibili.com', 'Referer': 'https://t.bilibili.com/',
               'Origin': 'https://t.bilibili.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/64.0.3282.140 Safari/537.36'}
    if offset_dynamicID == '0':
        url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=' + str(bilimid)
    else:
        url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=' + str(bilimid) + '&offset_dynamic_id=' + str(offset_dynamicID)
    resp = requests.get(url,  headers=headers)
    return resp2dynamiclist(resp.content.decode('utf-8'), end)

    # return resp.content.decode('utf-8')


def resp2dynamiclist(respcontent,end):
    dynamiclist = []
    jsoncontent= json.loads(respcontent)
    print(jsoncontent)
    dynamiclist = jsoncontent['data']['cards']
    offset = 0
    print(len(dynamiclist))
    for item in dynamiclist:
        offset = item['desc']['dynamic_id']
        if offset > end:
            service.insertDynamic(item)
        else:
            return -1
    if offset != 0:
        return offset
    else:
        return -1

if __name__ == '__main__':
    accessDynamicByUp(19553445, 1514736000)
    # print(html)
