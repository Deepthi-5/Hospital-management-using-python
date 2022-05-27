import mysql.connector
from tabulate import tabulate
from hosp_patientinsert import *



def addtobilling(pid):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    mycursor.execute("select pname,hi from patient_record where pid='{}'".format(pid))
    res1=mycursor.fetchall()
    mycursor.execute("select sname,dept,slot,service_cost from doctor_record where pid='{}'".format(pid))
    res2=mycursor.fetchall()
    mydb.commit()
   
    pname=res1[0][0]
    hi=res1[0][1]
    sname=res2[0][0]
    dept=res2[0][1]
    slot=res2[0][2]
    initial_cost=res2[0][3]
    if hi:
        discount_cost=(hi/100)*initial_cost
    else:
        discount_cost=0
    total_cost=initial_cost-discount_cost
    date=datetime.date.today()
    paystatus="NOT PAID"

    com1="insert into billing (pid,pname,sname,dept,slot,initial_cost,discount_cost,total_cost,date,paystatus) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    rec1=(pid,pname,sname,dept,slot,initial_cost,discount_cost,total_cost,date,paystatus)
    mycursor.execute(com1,rec1)
    mydb.commit()



def choose_dept():
        while True:
                print()
                print("\t\t***CHOOCE SERVICE***")
                print("="*50)
                print("1.ORTHODONTIST")
                print("2.ENDODONTIST")
                print("3.IMPLANTOLOGIST")
                print("4.GENERAL DENTIST")
                print("5.PAEDODONTICS")
                print("6.PERIODONTAL")
                print("7.BACK TO MENU")
                print("="*50)
                choice=int(input("ENTER DEPARTMENT: "))
                print()
                if choice==1:
                        dept="ORTHODONTIST"
                        break
                elif choice==2:
                        dept="ENDODONTIST"
                        break
                elif choice==3:
                        dept="IMPLANTOLOGIST"
                        break
                elif choice==4:
                        dept="GENERAL DENTIST"
                        break
                elif choice==5:
                        dept="PAEDODONTICS"
                        break
                elif choice==6:
                        dept="PERIODONTAL"
                        break
                elif choice==7:
                        return
                else:
                    print("INVALID CHOICE. TRY AGAIN")
        return dept

   


def outpatient():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    print()
    print("="*50)
    pid=input("ENTER PATIENT ID: ")
    mycursor.execute("select * from patient_record where pid='{}'".format(pid))
    res1=mycursor.fetchall()
    if res1:
        print(tabulate(res1,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
        while True:
            print()
            print("\t\t**APPOINTMENT PREFERENCES**")
            print("="*50)
            print("1.NO PREFERENCE")
            print("2.CHOOSE DOCTOR AND SLOT")
            print("3.CHOOSE DOCTOR")
            print("4.CHOOSE SLOT")
            print("5.BACK TO MENU")
            print("="*50)
            pref=int(input("ENTER CHOICE: "))
            if pref==1:
                dept=choose_dept()
                mycursor.execute("select * from doctor_record where availability='Y' and dept='{}'".format(dept))      
            elif pref==2:
                name=input("ENTER DOCTOR NAME: ")
                mycursor.execute("select slot,availability from doctor_record where sname='{}'".format(name))
                res2=mycursor.fetchall()
                if res2:
                    print(tabulate(res2,headers=["SLOT","AVAILABILITY"],tablefmt='fancy_grid'))
                    slot=input("ENTER SLOT: ")
                    mycursor.execute("select * from doctor_record where availability='Y' and sname='{}' and slot='{}'".format(name,slot))
                else:
                    print("NO RECORD FOUND.")
                    continue

            elif pref==3:
                name=input("ENTER DOCTOR NAME: ")
                mycursor.execute("select * from doctor_record where availability='Y' and sname='{}'".format(name))
            elif pref==4:
                dept=choose_dept()
                mycursor.execute("select sname,slot,availability from doctor_record where dept='{}'".format(dept))
                res2=mycursor.fetchall()
                if res2:
                    print(tabulate(res2,headers=["DOCTOR NAME","SLOT","AVAILABILITY"],tablefmt='fancy_grid'))
                    slot=input("ENTER SLOT: ")
                    mycursor.execute("select * from doctor_record where availability='Y' and slot='{}'".format(slot))
                else:
                    print("NO RECORD FOUND.")
                    continue
            elif pref==5:
                return
            else:
                print("INVALID CHOICE. TRY AGAIN")
            res4=mycursor.fetchall()
            if res4:
                sno=res4[0][0]
                name=res4[0][2]
                slot=res4[0][5]
                print("="*50)
                print("PID: ",pid)
                print("DOCTOR NAME: ",name)
                print("AVAILABLE SLOT: ",slot)
                mycursor.execute("update doctor_record set availability='N',pid='{}' where sno='{}'".format(pid,sno))
                mydb.commit()
                addtobilling(pid)
                return
            else:
                print("NO DOCTORS AVAILABLE")
           
    else:
        print("NO RECORD FOUND.")
        print("="*50)
        ch1=input("WOULD YOU LIKE TO CREATE A NEW RECORD?(Y/N): ")
        if ch1 in "Yy":
            patient_insert()
            outpatient()
        else:
            return
       
#outpatient()
