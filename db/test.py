#encoding=utf-8

import sys
import MySQLdb as mdb

reload(sys)
sys.setdefaultencoding('utf-8')

con = None

try:
    con = mdb.Connect('localhost','root','jobin','zmld',charset='utf8')
    cur = con.cursor()
    cur.execute("show full columns from player")

    numRows = int(cur.rowcount)

if con:
    con.close()
