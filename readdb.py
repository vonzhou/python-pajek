#!/usr/bin/python

import MySQLdb
#from igraph import *

# connect the db
db = MySQLdb.connect("localhost", "root", "root", "test");

cursor = db.cursor()

#store it to file
f = open("nodes.data", "w")

#get all the ids
sql1 = "select uid from user"

try:
    cursor.execute(sql1)
    results = cursor.fetchall()
    for row in results:
        #print(row[0])
        f.write(row[0]+'\n')
except:
    print("ERROR")


f2 = open("edges.data", "w")
sql2 = "select *from userrelation"

try:
    cursor.execute(sql2)
    results = cursor.fetchall()
    for row in results:
        suid = row[0]
        tuid = row[1]
        #print("suid=%s,tuid=%s"%(suid,tuid))
        f2.write(suid + ' ' +  tuid + '\n')
except:
    print("ERROR")

f.close()
f2.close()
db.close()
