#!/bin/bash
remote_addr=stdyun@218.245.3.70:~/stdyun.backup/ 
python backup_table.py
scp  *.sql ${remote_addr} 
python backup_data.py
sleep 0.5s
scp  *.sql.lzma ${remote_addr}
md5sum *.sql.lzma *.sql  > backup.md5
scp backup.md5 ${remote_addr}
