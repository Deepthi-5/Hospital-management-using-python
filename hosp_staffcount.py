import mysql.connector
from tabulate import tabulate


def totalstaffcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record")
    count=mycursor.fetchall()
    print("TOTAL STAFF COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY ALL STAFF RECORD?(Y/N): ")
    if ch in "Yy":
            mycursor.execute("select * from staff_record")
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
            else:
                print("NO RECORD FOUND")
    mydb.commit()


   
def doctorcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record where designation='DOCTOR'")
    count=mycursor.fetchall()
    print("DOCTOR COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY ALL DOCTOR RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from staff_record where designation='DOCTOR'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()


   
def nursecount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record where designation='NURSE'")
    count=mycursor.fetchall()
    print("NURSE COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY ALL NURSE RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from staff_record where designation='NURSE'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()


   
def staffcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record where designation='STAFF'")
    count=mycursor.fetchall()
    print("ADDITIONAL STAFF COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY ALL ADDITIONAL STAFF RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from staff_record where designation='STAFF'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()



def dayshiftcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record where shift='DAY'")
    count=mycursor.fetchall()
    print("DAY SHIFT STAFF COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY STAFF RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from staff_record where shift='DAY'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()



def nightshiftcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from staff_record where shift='NIGHT'")
    count=mycursor.fetchall()
    print("DAY SHIFT STAFF COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY STAFF RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from staff_record where shift='NIGHT'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["STAFF ID","STAFF NAME","MOBILE NO","DATE OF ADMISSION","DEPARTMENT","DESIGNATION","SHIFT","SERVICE COST"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()



def displaystaffappointmentname():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    name=input("ENTER DOCTOR NAME: ")
    mycursor.execute("select slot,availability,pid from doctor_record where sname='{}'".format(name))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["SLOT","AVAILABILITY","PID"],tablefmt='fancy_grid'))
    else:
        print("NO RECORD FOUND")
       

         
def displaystaffappointmentid():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    sid=input("ENTER DOCTOR ID: ")
    mycursor.execute("select sname from doctor_record where sid='{}'".format(sid))
    res1=mycursor.fetchall()
    if res1:
        print("DOCTOR NAME: ",res1[0][0])
    mycursor.execute("select slot,availability,pid from doctor_record where sid='{}'".format(sid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["SLOT","AVAILABILITY","PID"],tablefmt='fancy_grid'))
    else:
        print("NO RECORD FOUND")




def staff_count():
    while True:
        print("="*50)
        print("1.TOTAL STAFF RECORD COUNT")
        print("2.TOTAL DOCTOR/NURSE/STAFF COUNT")
        print("3.TOTAL STAFF IN DAY/NIGHT SHIFT")
        print("4.APPOINTMENTS OF DOCTOR")
        print("5.BACK TO MENU")
        print("="*50)
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            totalstaffcount()
        elif choice==2:
            while True:
                print()
                print("FIND COUNT OF")
                print("="*50)
                print("1.DOCTOR")
                print("2.NURSE")
                print("3.STAFF")
                print("4.BACK TO MENU")
                print("="*50)
                ch=int(input("ENTER CHOICE: "))
                if ch==1:
                    doctorcount()
                elif ch==2:
                    nursecount()
                elif ch==3:
                    staffcount()
                elif ch==4:
                    break
                else:
                    print("INVALID CHOICE.TRY AGAIN")
        elif choice==3:
            while True:
                print()
                print("FIND COUNT OF")
                print("="*50)
                print("1.DAY")
                print("2.NIGHT")
                print("3.BACK TO MENU")
                print("="*50)
                ch=int(input("ENTER CHOICE: "))
                if ch==1:
                    dayshiftcount()
                elif ch==2:
                    nightshiftcount()
                elif ch==3:
                    break
                else:
                    print("INVALID CHOICE.TRY AGAIN")
        elif choice==4:
            while True:
                 print()
                 print("="*50)
                 print("1.DOCTOR NAME")
                 print("2.DOCTOR ID")
                 print("3.BACK TO MENU")
                 print("="*50)
                 ch=int(input("ENTER CHOICE: "))
                 if ch==1:
                     displaystaffappointmentname()
                 elif ch==2:
                     displaystaffappointmentid()
                 elif ch==3:
                     break
                 else:
                     print("INVALID CHOICE.TRY AGAIN")
        elif choice==5:
            return
        else:
            print("INVALID CHOICE.TRY AGAIN.")

           
#staff_count()


def find_sid():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    name=input("ENTER STAFF NAME: ")
    mycursor.execute("select sid,name from staff_record where name='{}'".format(name))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result,headers=["STAFF NAME","STAFF ID"],tablefmt='fancy_grid'))
    else:
        print("NO RECORD FOUND")
