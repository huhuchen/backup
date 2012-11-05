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

def backup_data(host, port, name, user, password):
    comm_option = COMM_OPTION%(host, port, user, password, name)

    backup_data_option = "--no-create-info --quick --default-character-set=utf8 --skip-opt --hex-blob"

    now = datetime.datetime.now().strftime("%Y%m%d")
    cmd = "%s %s %s | lzma > %s/%s_data_%s.sql.lzma" % ("mysqldump", backup_data_option, comm_option, DATA_BACKUP_DIRNAME, name, now)
    subprocess.call(cmd, shell=True)



def backup_all():
    for db_paras in DATABASE_CONFIG:
        host, port, name, user, password = db_paras.split(":")
        backup_data(host, port, name, user, password)


if __name__ == "__main__":
    backup_all()
