#!/bin/bash

##define varibale
remote_addr=stdyun@218.245.3.70:~/stdyun.backup/ 
now=$(date +%Y%m%d)

##backup table
python backup_table.py
scp  *${now}.sql ${remote_addr} 

##backup data
python backup_data.py
scp  *${now}.sql.lzma ${remote_addr}

##create the md5 of backup file
md5sum *${now}.sql.lzma *${now}.sql  > backup_${now}.md5
scp backup_${now}.md5 ${remote_addr}

##delete expired data
old_date=$(date -d "7 days ago" +%Y%m%d)
find . -name "*${old_date}*" -exec rm {} \;
