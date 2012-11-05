#!/bin/bash
remote_addr=stdyun@218.245.3.70:~/stdyun.backup/ 
now=$(date +%Y%m%d)
python backup_table.py
scp  *${now}.sql ${remote_addr} 
python backup_data.py
scp  *${now}.sql.lzma ${remote_addr}
md5sum *${now}.sql.lzma *${now}.sql  > backup_${now}.md5
scp backup_${now}.md5 ${remote_addr}
old_date=$(date -d "7 days ago" +%Y%m%d)
result=$(find *${old_date}*)
if [ result ];then
    rm *${old_date}* 
fi    
