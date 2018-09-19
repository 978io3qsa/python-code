#!/usr/bin/env pytohn
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeSlowLogsRequest
from aliyunsdkcore.profile import region_provider
import json

#region_provider.modify_point('rds', '<regionId>', 'rds.<regionId>.aliyuncs.com')

clt = client.AcsClient('LTAIry88qsasWzSD','4A4Zzz2DtdgaU6xplhtq7NkgRUMFAs','cn-shenzhen')

# 
request = DescribeSlowLogsRequest.DescribeSlowLogsRequest()
request.set_accept_format('json')

request.add_query_param('DBInstanceId', 'rm-wz9o8wqp2j6os324m')
request.add_query_param('StartTime', '2018-07-20Z')
request.add_query_param('EndTime', '2018-08-03Z')

result = clt.do_action_with_exception(request)

result2 = json.loads(result)

###print result2


print len(result2['Items']['SQLSlowLog'])

for item in result2['Items']['SQLSlowLog'] :
    print u'日期：' + item['CreateTime']
    print u'执行时间（s）：' + str(item['MySQLTotalExecutionTimes'])
    print u'数据库：' + item['DBName']
    print u'sql语句：' + item['SQLText']
