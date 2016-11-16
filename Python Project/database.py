#!/usr/bin/python

import MySQLdb
import os


os.system('cls')
print("-----------------------------welcome To Database Viewer----------------------------------------\n")
try:
    db_name = raw_input("\t\tEnter Database Name:")
    db = MySQLdb.connect("localhost","root","",db_name)



    flag = 1

    while flag:

        cursor = db.cursor()
        os.system('cls')
        cursor.execute("show tables")
        results = cursor.fetchall()

        print("Tables in Database : \n-------------")
        for row in results:
          table_name = row[0]
          # Now print fetched result
          print "%s\t" % \
                 (table_name)
        print("-------------")


        table_name=raw_input("Please Select Table To show:")
        os.system('cls')
        print ("------------------"+ table_name+" Table Enteries-------------------\n============================================================")

        sql = "SELECT * FROM "+table_name
        cursor.execute(sql)
        results = cursor.fetchall()
        widths = []
        columns = []
        tavnit = '|'
        separator = '+'
        for cd in cursor.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-"+"%ss |" % (w,)
            separator += '-'*w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)

        columns = cursor.description
        result = []
        for value in cursor.fetchall():
            tmp = {}
            for (index,column) in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)
        flag = input("Press 1 key to continue. | press 2 key to close. \n\n\t")
        if flag == 1:
            os.system('cls')
        else:
            flag = 0
            print "Database Viewer is close successfully..!!"
    db.close()
    
except MySQLdb.Error as e:
    print(e)

except :
    print("Unknown error occurred")
