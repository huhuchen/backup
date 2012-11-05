backup
======

my backup pro


请在settings中设置需要备份的数据库，以及备份数据在当前服务器的存放目录


在backup.sh 中设置备份服务器的地址及用户名：
ex：
remote_addr=stdyun@218.245.3.70:~/stdyun.backup/ 


md5_check.sh为在备份服务器上运行的crontab脚本
