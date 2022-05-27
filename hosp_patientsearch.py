import mysql.connector
from tabulate import tabulate
#search all patients with and without insurance(?)
#search all patients?
#search all male and female patients?

def search_pname():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            name=input("ENTER PATIENT NAME: ")
            mycursor.execute("select * from patient_record where PNAME='{}'".format(name))
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("RECORD NOT FOUND")

def search_mno():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            m_no=input("ENTER MOBILE NO.: ")
            mycursor.execute("select * from patient_record where MOBILE_NO='{}'".format(m_no))
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("RECORD NOT FOUND")
def search_pid():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            pid=input("ENTER PATIENT ID: ")
            mycursor.execute("select * from patient_record where PID='{}'".format(pid))
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("RECORD NOT FOUND")

def display_fm():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            sex=input("ENTER SEX (M/F): ")
            mycursor.execute("select * from patient_record where sex='{}'".format(sex))
            res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("NO RECORDS EXIST")

def display_hi():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            ch=input("DISPLAY RECORDS OF PATIENTS WITH/WITHOUT HEALTH INSURANCE(W/WO): ")
            if ch.upper()=="W":
                mycursor.execute("select * from patient_record where HI IS NOT NULL")
                res=mycursor.fetchall()
            elif ch.upper()=="WO":
                mycursor.execute("select * from patient_record where HI IS NULL")
                res=mycursor.fetchall()
            if res:
                print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("NO RECORDS EXIST")

def display_all():
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
            mycursor=mydb.cursor()
            mycursor.execute("select * from patient_record")
            res=mycursor.fetchall()
            if res:
                ch=input("ARE YOU SURE YOU WANT TO DISPLAY ALL RECORDS? (Y/N): ")
                if ch in "Yy":
                    print(tabulate(res,headers=["PATIENT ID","PATIENT NAME","AGE","DATE OF BIRTH","SEX","ADDRESS","MOBILE NO","EMAIL","HEALTH INSURANCE STATUS"],tablefmt='fancy_grid'))
            else:
                print("NO RECORDS EXIST")
   
def patient_search():
        while True:
          print("\t\t\t\t***SEARCH MENU***")
          print("=======================")
          print("1.SEARCH BY NAME")
          print("2.SEARCH BY MOBILE NO.")
          print("3.SEARCH BY PATIENT ID")
          print("4.DISPLAY ALL FEMALE/MALE PATIENTS")
          print("5.DISPLAY ALL PATIENTS WITH/WITHOUT HEALTH INSURANCE")
          print("6.DISPLAY ALL PATIENT RECORDS")
          print("7.BACK TO MAIN MENU")
          print("=======================")
          choice=int(input("ENTER CHOICE: "))  
          if choice==1:
              search_pname()
             
          elif choice==2:
              search_mno()

          elif choice==3:
              search_pid()

             
          elif choice==4:
              display_fm()

          elif choice==5:
              display_hi()

          elif choice==6:
              display_all()

          elif choice==7:
              return
           
          else:
             print("INVALID CHOICE. TRY AGAIN")


#patient_search()


            
