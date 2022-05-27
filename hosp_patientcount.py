import mysql.connector
from tabulate import tabulate

def totalpatientcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from patient_record")
    count=mycursor.fetchall()
    print("TOTAL PATIENT COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY ALL PATIENT RECORD?(Y/N): ")
    if ch in "Yy":
            mycursor.execute("select * from patient_record")
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE"],tablefmt='fancy_grid'))
            else:
                print("NO RECORD FOUND")
    mydb.commit()




def femalepatientcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from patient_record where sex='F'")
    count=mycursor.fetchall()
    print("FEMALE PATIENT COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY PATIENT RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from patient_record where sex='F'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()

def malepatientcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from patient_record where sex='M'")
    count=mycursor.fetchall()
    print("FEMALE PATIENT COUNT: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY PATIENT RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from patient_record where sex='M'")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()



   
def hipatientcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from patient_record where hi IS NOT NULL")
    count=mycursor.fetchall()
    print("COUNT OF PATIENT WITH HEALTH INSURANCE: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY PATIENT RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from patient_record where hi IS NOT NULL")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()

def nohipatientcount():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("select count(*) from patient_record where hi IS NULL")
    count=mycursor.fetchall()
    print("COUNT OF PATIENT WITHOUT HEALTH INSURANCE: ",count[0][0])
    ch=input("WOULD YOU LIKE TO DISPLAY PATIENT RECORD?(Y/N): ")
    if ch in "Yy":
        mycursor.execute("select * from patient_record where hi IS NULL")
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    mydb.commit()





def displaypatientappointmentname():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    name=input("ENTER PATIENT NAME: ")
    mycursor.execute("select pid from patient_record where pname='{}'".format(name))
    result=mycursor.fetchall()
    if result:
        pid=result[0][0]
        mycursor.execute("select sid,sname,dept,service_cost,slot,pid from doctor_record where pid='{}'".format(pid))
        res=mycursor.fetchall()
        if res:
            print(tabulate(res,headers=["DOCTOR ID","DOCTOR NAME","DEPARTMENT","SERVICE COST","SLOT","PATIENT ID"],tablefmt='fancy_grid'))
        else:
            print("NO RECORD FOUND")
    else:
        print("NO RECORD FOUND")

         
def displaypatientappointmentid():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select sid,sname,dept,service_cost,slot,pid from doctor_record where pid='{}'".format(pid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["DOCTOR ID","DOCTOR NAME","DEPARTMENT","SERVICE COST","SLOT","PATIENT ID"],tablefmt='fancy_grid'))
    else:
        print("NO RECORD FOUND")




def patient_count():
    while True:
        print("="*50)
        print("1.TOTAL PATIENT RECORD COUNT")
        print("2.TOTAL FEMALE/MALE PATIENT COUNT")
        print("3.COUNT OF PATIENTS WITH/WITHOUT HI")
        print("4.PATIENT APPOINTMENT")
        print("5.BACK TO MENU")
        print("="*50)
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            totalpatientcount()
        elif choice==2:
            while True:
                print()
                print("FIND COUNT OF")
                print("="*50)
                print("1.FEMALE PATIENTS")
                print("2.MALE PATIENTS")
                print("3.BACK TO MENU")
                print("="*50)
                ch=int(input("ENTER CHOICE: "))
                if ch==1:
                    femalepatientcount()
                elif ch==2:
                    malepatientcount()
                elif ch==3:
                    break
                else:
                    print("INVALID CHOICE.TRY AGAIN")
        elif choice==3:
            while True:
                print()
                print("FIND COUNT OF")
                print("="*50)
                print("1.PATIENTS WITH HEALTH INSURANCE")
                print("2.PATIENTS WITHOUT HEALTH INSURANCE")
                print("3.BACK TO MENU")
                print("="*50)
                ch=int(input("ENTER CHOICE: "))
                if ch==1:
                    hipatientcount()
                elif ch==2:
                    nohipatientcount()
                elif ch==3:
                    break
                else:
                    print("INVALID CHOICE.TRY AGAIN")
        elif choice==4:
            while True:
                 print()
                 print("="*50)
                 print("1.PATIENT NAME")
                 print("2.PATIENT ID")
                 print("3.BACK TO MENU")
                 print("="*50)
                 ch=int(input("ENTER CHOICE: "))
                 if ch==1:
                     displaypatientappointmentname()
                 elif ch==2:
                     displaypatientappointmentid()
                 elif ch==3:
                     break
                 else:
                     print("INVALID CHOICE.TRY AGAIN")
        elif choice==5:
            return
        else:
            print("INVALID CHOICE.TRY AGAIN.")

           
#patient_count()

def find_pid():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    name=input("ENTER PATIENT NAME: ")
    mycursor.execute("select pid,pname from patient_record where pname='{}'".format(name))
    result=mycursor.fetchall()
    if result:
        print(tabulate(result,headers=["PATIENT NAME","PATIENT ID"],tablefmt='fancy_grid'))
    else:
        print("NO RECORD FOUND")
