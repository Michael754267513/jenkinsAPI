# jenkinsAPI
自动运行一个指定jenkins job

需要安装 ConfigParser 和 jenkinsAPI 模块

配置文件在/etc/jenkionsapi/config

[config]

jenkins_url=http://192.168.12.172:8080      jenkins 地址

username=michael                            用户名

password=laoshu                             密码


运行一个job.

python Jenkinsapi.py test   运行一个jenkins里面test job
