# -*- coding:utf-8 -*-

import sys
from fabric.api import *
sys.path.append('../upload/') #引入文件路径
from project import Project

env.user = ""                      #登录账号
env.hosts = ['']                   #服务器ip
env.password = ''                  #登录密码
env.base_dir = ""                  #项目存放目录


#发布代码(开发环境)
@task
def deploy():

    ext_name="qq_arrow_"
    ext_num=[2110]

    # 本地要上传的文件夹
    local_dir = "D:/pro/trunk/UItraman/server/country_qq_release"

    # 排除文件(夹)
    exclude_list = [
        ".idea",
        "vendor",
        "gatewayworker",
        "environments",
        "backend",
        "console",
        "frontend/config",
        "common/config"
    ]

    for num in ext_num:
        # 服务器文件夹名称
        file_name = ext_name + str(num)

        # 上传到服务器
        Project.UploadProject(local_dir=local_dir, remote_dir=env.base_dir, exclude=exclude_list,file_name=file_name)



