#!/usr/bin/env python
#coding:utf-8

import subprocess
from os.path import dirname, abspath , join
import sys
import datetime

PREFIX = dirname(abspath(__file__))
sys.path.append(PREFIX)

from settings import DATABASE_CONFIG, DATA_BACKUP_DIRNAME
COMM_OPTION = "-h%s -P%s -u%s -p%s %s"

def backup_table(host, port, name, user, password):
    comm_option = COMM_OPTION%(host, port, user, password, name)

    """
    备份一个表数据的命令实例
    mysqldump --skip-opt --no-create-info 数据库名字 表名 --where="id<2000"
    """
    backup_table_option = "--skip-comments --no-data --default-character-set=utf8 --skip-opt --add-drop-table --create-options --quick --hex-blob"

    now = datetime.datetime.now().strftime("%Y%m%d")
    cmd = "%s %s %s" % ("mysqldump", backup_table_option, comm_option)
    filename = "%s/%s_table_%s.sql" % (DATA_BACKUP_DIRNAME, name, now)
    with open(filename, "w") as backfile:
        subprocess.call(
            cmd.split(),
            stdout=backfile,
            shell=True
        )

def backup_all():
    for db_paras in DATABASE_CONFIG:
        host, port, name, user, password = db_paras.split(":")
        backup_table(host, port, name, user, password)
        #print key

if __name__ == "__main__":
    backup_all()

