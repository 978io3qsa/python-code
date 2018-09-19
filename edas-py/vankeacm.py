import acm
import time

ENDPOINT = "addr-sz-internal.edas.aliyun.com:8080"
NAMESPACE = "vanke-yiyun-prod"
AK = "LTAIry88qsasWzSD"
SK = "4A4Zzz2DtdgaU6xplhtq7NkgRUMFAs"

# get config
client = acm.ACMClient(ENDPOINT, NAMESPACE, AK, SK)
client.set_options(region_id="cn-shenzhen")
client.list_all()