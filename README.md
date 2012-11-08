backup
======
 

----------------------------------
数据库备份工具，目前支持功能：

支持mysql

同时备份多个数据库

备份数据库表结构

备份数据

压缩数据

数据文件MD5验证

传输备份数据至备份服务器

--------------------------------
使用说明

settings中设置需要备份的数据库信息，以及备份数据在当前服务器的存放目录

backup.sh中设置备份服务器参数
ex: remote_addr=username@111.111.111.111:~/backup/ 

md5_check.sh为在备份服务器上运行的crontab脚本


bash backup.sh
bash md5_check.sh
