#!/usr/bin/env pytohn
#coding=utf-8

from aliyun.log import LogClient

endpoint = 'cn-shenzhen.log.aliyuncs.com'

ak = 'LTAIry88qsasWzSD'

sk = '4A4Zzz2DtdgaU6xplhtq7NkgRUMFAs'

client = LogClient(endpoint,ak,sk)

res = client.list_project()

res.log_print()