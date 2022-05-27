import mysql.connector
import random
from tabulate import tabulate

def update_staffname():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    sid=input("ENTER STAFF ID: ")
    mycursor.execute("select * from staff_record where SID='{}'".format(sid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DOA","DEPT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancygrid'))
        add=input("ENTER NEW NAME: ")
        mycursor.execute("update staff_record set NAME='{}' where SID='{}'".format(add,sid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")

def update_staffmn():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    sid=input("ENTER STAFF ID: ")
    mycursor.execute("select * from staff_record where SID='{}'".format(sid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DOA","DEPT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancygrid'))
        add=input("ENTER NEW MOBILE NO: ")
        mycursor.execute("update staff_record set MOBILE_NO='{}' where SID='{}'".format(add,sid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")

def update_staffservicecost():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    sid=input("ENTER STAFF ID: ")
    mycursor.execute("select * from staff_record where SID='{}'".format(sid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DOA","DEPT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancygrid'))
        add=input("ENTER NEW SERVICE COST: ")
        mycursor.execute("update staff_record set SERVICE_COST='{}' where SID='{}'".format(add,sid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")

def update_staffshift():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    sid=input("ENTER STAFF ID: ")
    mycursor.execute("select * from staff_record where SID='{}'".format(sid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DOA","DEPT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancygrid'))
        add=input("ENTER NEW SHIFT: ")
        mycursor.execute("update staff_record set SHIFT='{}' where SID='{}'".format(add,sid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")


def staff_update():
    while True:
        print("==============================")
        print("1.UPDATE NAME")
        print("2.UPDATE MOBILE NO.")
        print("3.UPDATE SERVICE COST")
        print("4.UPDATE SHIFT")
        print("5.BACK TO MAIN MENU")
        print("==============================")

        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            update_staffname()
        elif choice==2:
            update_staffmn()
        elif choice==3:
            update_staffservicecost()
        elif choice==4:
            update_staffshift()
        elif choice==5:
            return
        else:
            print("INVALID CHOICE. TRY AGAIN")

           
#staff_update()
