
# -*- coding: utf-8 -*-
import pexpect
import sys
import yaml



#读取yaml文件
def getConfig(yaml_file_path):
    yamf = open(yaml_file_path)
    yamlConfig = yaml.load(yamf)
    return yamlConfig

#获取ip,用户名，密码，命令列表
def getUserParms(ymalConfig,index):
    ip = ymalConfig['hosts'][index]['ip']
    user = ymalConfig['hosts'][index]['user']
    password = ymalConfig['hosts'][index]['password']
    cmdList = ymalConfig['hosts'][index]['commands']

    return ip, user, password, cmdList

#运行命令
def runComds(ip,user,password,cmdList,logFile):
    host = pexpect.spawn('ssh ' + user + '@' + ip)
    fout = file(logFile,'w')
    host.logfile = fout
    
    #密码认证
    host.expect("password")
    host.sendline(password)

    for cmd in cmdList :
        host.expect('#')
        print 'execute command: ' + cmd
        host.sendline(cmd)
    host.expect('#')

if __name__ == '__main__':
    config = getConfig(r'devops-py/setting.yaml')
    ip, user, password, cmdList = getUserParms(config,0)
    #print ip, user, password, cmdList
    runComds(ip, user, password, cmdList,u'devops-py/running.log')


