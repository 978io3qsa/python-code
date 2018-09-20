#-*- coding: utf-8 -*-

from aliyunsdkcore import client
from aliyunsdkcms.request.v20180308 import QueryMetricListRequest
import time
import json
import getInstances



ak, sk, domain = getInstances.getAkSkDomain('aliyun-mon/config.ini')

ecs_dict = getInstances.getECSList('aliyun-mon/config.ini')

print ak,sk,domain
print ecs_dict

'''

clt = client.AcsClient(
    "LTAIry88qsasWzSD", 
    "4A4Zzz2DtdgaU6xplhtq7NkgRUMFAs",
    "cn-shenzhen")
request = QueryMetricListRequest.QueryMetricListRequest()
request.set_accept_format('json')
request.set_Project('acs_ecs_dashboard')
request.set_Metric('diskusage_utilization')
start_time = "2018-08-01"
timestamp_start = int(time.mktime(time.strptime(start_time, "%Y-%m-%d"))) * 1000

end_time = "2018-09-01"
timestamp_end = int(time.mktime(time.strptime(end_time, "%Y-%m-%d"))) * 1000

request.set_StartTime(timestamp_start)
request.set_EndTime(timestamp_end)
request.set_Dimensions("{'instanceId':'i-wz94obs9dvxg9zu1n2s3'}")
request.set_Period('86400')
result = clt.do_action_with_exception(request)

deal_result = json.loads(result)

end_result =  json.loads(deal_result['Datapoints'])

print len(end_result)

for item in end_result:
    if item['diskname'] == '/':
        print(u'根分区磁盘使用率： %.2f' %item['Average']) 
    
    

   '''