#!/bin/bash
remote_addr=stdyun@218.245.3.70:~/stdyun.backup/ 
python backup_table.py
scp  table_ns1.sql ${remote_addr} 
python backup_data.py
now=$(date +"%Y%m%d")
new_filename=stdyun_ns1_${now}.sql.lzma
mv stdyun_ns1.sql.lzma ${new_filename}
scp  ${new_filename} ${remote_addr}
md5sum ${new_filename} table_ns1.sql  > backup.md5
scp backup.md5 ${remote_addr}
