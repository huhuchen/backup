#!/bin/bash
now=$(date +%Y%m%d)
message=$(md5sum -c backup_${now}.md5)
result=$(echo $?)
if [ ! result ];then
    echo "$message"
fi
