#-*- coding: utf-8 -*-

from aliyunsdkcore import client
from aliyunsdkcms.request.v20180308 import QueryMetricListRequest
from openpyxl import Workbook
import time
import json
import getInstances
import datetime





ak, sk, domain = getInstances.getAkSkDomain('aliyun-mon/config.ini')

ecs_dict = getInstances.getECSList('aliyun-mon/config.ini')

clt = client.AcsClient(ak, sk, domain)

def getDiskUsage(start_time, end_time, Period):
    request = QueryMetricListRequest.QueryMetricListRequest()
    request.set_accept_format('json')
    request.set_Project('acs_ecs_dashboard')
    request.set_Metric('diskusage_utilization')

    timestamp_start = int(time.mktime(time.strptime(start_time,"%Y-%m-%d"))) * 1000
    timestamp_end = int(time.mktime(time.strptime(end_time,"%Y-%m-%d"))) * 1000
    
    request.set_StartTime(timestamp_start)
    request.set_EndTime(timestamp_end)

    rootUsage = []
    appUsage = []
    resultList = []

    request.set_Period(Period)
    for item in ecs_dict.values():
        rootUsage.append(item)
        appUsage.append(item)
        request.set_Dimensions("{'instanceId': '" + item + "'}")
        data = clt.do_action_with_exception(request)
        result = json.loads(json.loads(data)['Datapoints'])
        for values in result:
            if values['diskname'] == '/' :
                rootUsage.append(round(values['Average'],2))
            if values['diskname'] == '/app' :
                appUsage.append(round(values['Average'],2))
        resultList.append(rootUsage)
        resultList.append(appUsage)
        rootUsage = []
        appUsage = []

    return resultList


if __name__ == '__main__':
   wb = Workbook()
   ws = wb.active
   ws.append(getDiskUsage('2018-09-18','2018-09-24','86400'))
   wb.save("diskUsage.xlsx")
