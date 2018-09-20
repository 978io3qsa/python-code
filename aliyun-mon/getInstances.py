#-*- coding: utf-8 -*-

'''
   从配置文件获取 ecs、rds、slb等资源的实例 
'''
import configparser


def getAkSkDomain(configFile):
    conf = configparser.ConfigParser()
    conf.readfp( open(configFile))
    ak = conf.get('aksk','ak')
    sk = conf.get('aksk','sk')
    domain = conf.get('aksk','domain')
    return ak, sk, domain

def getECSList(configFile):
    conf = configparser.ConfigParser()
    conf.readfp(open(configFile))
    ecsList = {}
    for item in conf.options('ecs-list'):
        ecsList[item] = conf.get('ecs-list',item)
    return ecsList

if __name__ == '__main__':
    print getAkSkDomain('aliyun-mon/config.ini')
    print getECSList('aliyun-mon/config.ini')


