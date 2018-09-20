#-*- coding: utf-8 -*-

'''
   从配置文件获取 ecs、rds、slb等资源的实例 
'''
import configparser

def getAkSkDomain(configFile):
    conf = configparser.ConfigParser()
    conf.read(configFile)
    
    return


