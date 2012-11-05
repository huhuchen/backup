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

def backup_data(key, host, port, name, user, password):
    comm_option = COMM_OPTION%(host, port, user, password, name)

    backup_data_option = "--no-create-info --quick --default-character-set=utf8 --skip-opt --hex-blob"

    now = datetime.datetime.now().strftime("%Y%m%d")
    cmd = "%s %s %s | lzma > %s/%s_data_%s.sql.lzma" % ("mysqldump", backup_data_option, comm_option, DATA_BACKUP_DIRNAME, key, now)
    subprocess.Popen(cmd, shell=True)

def backup_all():
    for key, value in DATABASE_CONFIG.iteritems():
        host, port, name, user, password = value.get("master").split(":")
        backup_data(key, host, port, name, user, password)


if __name__ == "__main__":
    backup_all()
