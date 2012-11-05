#!/usr/bin/env python
#coding:utf-8

import subprocess
from os.path import dirname, abspath , join
import sys

PREFIX = dirname(abspath(__file__))
sys.path.append(PREFIX)

print "sys", sys.path
from settings import DATABASE_CONFIG
COMM_OPTION = "-h%s -P%s -u%s -p%s %s"

def backup_table(key, host, port, name, user, password):
    comm_option = COMM_OPTION%(host, port, user, password, name)

    """
    备份一个表数据的命令实例
    mysqldump --skip-opt --no-create-info 数据库名字 表名 --where="id<2000"
    """
    backup_table_option = "--skip-comments --no-data --default-character-set=utf8 --skip-opt --add-drop-table --create-options --quick --hex-blob"

    cmd = "%s %s %s" % ("mysqldump", backup_table_option, comm_option)
    #print cmd

    with open(join(PREFIX, "table_%s.sql"%key), "w") as backfile:
        subprocess.Popen(
            cmd.split(),
            stdout=backfile
        )

def backup_all():
    for key, value in DATABASE_CONFIG.iteritems():
        host, port, name, user, password = value.get("master").split(":")
        backup_table(key, host, port, name, user, password)
        #print key

if __name__ == "__main__":
    backup_all()

