# encoding: utf-8
import ConfigParser, time, sys
from jenkinsapi.jenkins import Jenkins

# 配置文件
path = '/etc/jenkionsapi/config'

# 创建一个连接
def get_server_instance(jenkins_url,username,password):
    server = Jenkins(jenkins_url, username=username, password=password)
    return server

# 判断job是否正在运行10s检测一次
def is_run_or_queue(jenkins_server,jobname):
    job_status = jenkins_server[jobname]
    while True:
        if job_status.is_queued_or_running():
           time.sleep(10)
        else:
            break

# 判断执行结果是否正确
def run_server_job(jenkins_server,jobname):
    job_status = jenkins_server[jobname]
    if job_status.is_queued_or_running():
        '''防止job重复执行'''
    else:
        jenkins_server.build_job(jobname)
    is_run_or_queue(jenkins_server,jobname)
    if job_status.get_last_build_or_none().get_status() == "SUCCESS":
        print '''job执行成功,执行编号: %s''' % job_status.get_last_build()
    else:
        print '''job执行失败,,执行编号: %s''' % job_status.get_last_build()


cf = ConfigParser.ConfigParser()

# 读取配置文件
cf.read(path)

# 读取文件配置,设置变量
jenkins_url = cf.get("config","jenkins_url")
username = cf.get("config","username")
password = cf.get("config","password")

# 创建一个连接
jenkins_server = get_server_instance(jenkins_url,username,password)
# 运行jenkins job: test
run_server_job(jenkins_server,sys.argv[1])