# -*- coding:utf-8 -*-

import os
from fabric.api import *


class Project:

    # 打包 解包 删除打包
    def UploadProject(local_dir=None, remote_dir="", exclude=[],file_name=""):
        from tempfile import mkdtemp
        local_dir = local_dir or os.getcwd()
        local_dir = local_dir.rstrip(os.sep)
        local_path, local_name = os.path.split(local_dir)
        tar_file = "%s.tar.gz" % local_name
        target_tar = os.path.join(remote_dir, tar_file)
        tmp_folder = mkdtemp()
        tar_path = os.path.join(tmp_folder, tar_file)

        exclude_file = ""
        for file in exclude:
            exclude_file += " --exclude=" + file

        cmd = "tar -czf %s %s -C %s %s" % (tar_path, exclude_file, local_path, local_name)
        local(cmd)
        put(tar_path, target_tar)
        with cd(remote_dir):
            try:
                run("tar -xzf %s" % tar_file)
                run("cd %s" % remote_dir)
                if(Project.remote_file(remote_dir+file_name)==False):
                    run("mv -f %s %s" % (local_name,file_name))
                else:
                    run("cp -r %s %s" % (local_name+"/*", file_name+"/"))
                    run("rm -rf %s" % local_name)
            finally:
                run("rm -f %s" % tar_file)
                local("rd /s/q %s" % tmp_folder)



    #文件是否存在
    def remote_file(file_path):
        if int(run(" [ -e " + file_path + " ] && echo 11 || echo 10")) == 11:
            return True
        else:
            return False

