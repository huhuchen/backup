#!/usr/bin/env python
#coding:utf-8

DATA_BACKUP_DIRNAME = "/home/stdyun/backup"

MYSQLPASSWD = "nssubdragon"
MYSQLUSER = "notifystack"
MYSQLPORT = "3306"
DB_HOST_ONLINE = "localhost:%s:ns_mfarm:%s:%s"%(MYSQLPORT, MYSQLUSER, MYSQLPASSWD)

DATABASE_CONFIG = {
    "ns1":{
        "master": DB_HOST_ONLINE,
        "tables": (
            "plan_recharge",
            "*",
        )
    },
}

