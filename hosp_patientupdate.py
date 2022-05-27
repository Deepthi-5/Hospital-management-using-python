import mysql.connector
import random
from tabulate import tabulate



def update_patientadd():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select * from patient_record where PID='{}'".format(pid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
        add=input("ENTER NEW ADDRESS: ")
        mycursor.execute("update patient_record set ADDRESS='{}' where PID='{}'".format(add,pid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")
                         


def update_patientmno():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select * from patient_record where PID='{}'".format(pid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
        mno=input("ENTER NEW MOBILE NO.: ")
        mycursor.execute("update patient_record set MOBILE_NO='{}' where PID='{}'".format(mno,pid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")
                         


def update_patienthi():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select * from patient_record where PID='{}'".format(pid))
    res=mycursor.fetchall()
    if res:
        print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
        ch=input("DOES PATIENT HAVE HEALTH INSURANCE? (Y/N): ")
        if ch in "Yy":
            l=[15,35,50,75]
            hi=random.choice(l)
            mycursor.execute("update patient_record set HI='{}' where PID='{}'".format(hi,pid))
        elif ch in "Nn":
            mycursor.execute("update patient_record set HI=NULL where PID='{}'".format(pid))
        mydb.commit()
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")
                         


def update_patientemail():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select * from patient_record where PID='{}'".format(pid))
    res=mycursor.fetchall()
    if res:
        print("s1")
        print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
        email=input("ENTER NEW EMAIL ADDRESS: ")
        mycursor.execute("update patient_record set EMAIL='{}' where PID='{}'".format(email,pid))
        mydb.commit()
        print("s2")
        print("RECORD UPDATED")
    else:
        print("RECORD NOT FOUND.")
                         

               
def patient_update():
    while True:
        print("============================")
        print("1.UPDATE ADDRESS")
        print("2.UPDATE MOBILE NO.")
        print("3.UPDATE HEALTH INSURANCE")
        print("4.UPDATE EMAIL")
        print("5.BACK TO MAIN MENU")
        print("============================")
       
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            update_patientadd()  
        elif choice==2:
            update_patientmno()
        elif choice==3:
            update_patienthi()
        elif choice==4:
            update_patientemail()  
        elif choice==5:
            return

        else:
            print("INVALID CHOICE. TRY AGAIN")
             

       

#patient_update()
