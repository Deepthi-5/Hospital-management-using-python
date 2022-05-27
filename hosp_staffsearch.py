import mysql.connector
from tabulate import tabulate

def staff_search():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    while True:
        print("="*50)
        print("1.SEARCH BY NAME")
        print("2.SEARCH BY STAFF ID")
        print("3.BACK TO MENU")
        print("="*50)
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            name=input("ENTER STAFF NAME: ")
            mycursor.execute("select * from staff_record where NAME='{}'".format(name))
            result=mycursor.fetchall()
            mydb.commit()
            if result:
                print(tabulate(result,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
            else:
                print("RECORD NOT FOUND")
             
        elif choice==2:
            sid=input("ENTER STAFF ID: ")
            mycursor.execute("select * from staff_record where SID='{}'".format(sid))
            result=mycursor.fetchall()
            mydb.commit()
            if result:
                print(tabulate(result,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
            else:
                print("RECORD NOT FOUND")
           
        elif choice==3:
            return
       
   
#staff_search()
