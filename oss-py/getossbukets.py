from aliyunsdkcore import client
import oss2
from aliyunsdkcore.profile import region_provider
import json

auth = oss2.Auth('LTAIruyemIEd4LeQ','DRZbgui8rT0kAiP0kAJJGrxffIA3DJ')

service = oss2.Service(auth, 'http://oss-cn-hangzhou.aliyuncs.com')


print([b.name for b in oss2.BucketIterator(service)])