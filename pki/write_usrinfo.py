#！/usr/bin/env python
# _*_ coding:utf-8 _*_

import sqlite3
def write_usrinfo():

 conn = sqlite3.connect('D:\cyy_project\TAC\pki_demo(1)\pki_demo\db.sqlite3')#注意完整路径，否则找不到数据表
 cur = conn.cursor()

#执行数据库的操作cur.execute
 cur.execute('select id,userID,address,pubkeyInfo from pki_userinfo')
 rows = cur.fetchall()

 for row in rows:
  print(row)
 f=open('D:\cyy_project\TAC\pki_demo(1)\pki_demo\static\document\main_pki_userinfo.csv', 'w')
 for row in rows:
  f.write("{}\n".format(str(row)))
 f.close()
 conn.commit()
 conn.close()

