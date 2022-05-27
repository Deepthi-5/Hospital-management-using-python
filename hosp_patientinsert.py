import mysql.connector
import datetime
import random


def check_pid(name):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    mycursor.execute("select * from patient_id")
    result=mycursor.fetchall()
    if result:
         mycursor.execute("select * from patient_id where STATUS='Available'")
         res=mycursor.fetchall()
         if res:
                  pid=res[0][0]
                  mycursor.execute("update patient_id set STATUS='Occupied',NAME=%s where pid=%s",(name,pid))
                  mydb.commit()
         else:
                if len(str(int(result[-1][0])+1))==1:
                        pid="000"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==2:
                        pid="00"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==3:
                        pid="0"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==4:
                        pid=str(int(result[-1][0])+1)
                command="insert into patient_id (pid,name,status) values (%s,%s,%s)"
                rec=pid,name,"Occupied"
                mycursor.execute(command,rec)
                mydb.commit()              
    else:
        pid="0001"
        command="insert into patient_id (pid,name,status) values (%s,%s,%s)"
        rec=pid,name,"Occupied"
        mycursor.execute(command,rec)
        mydb.commit()                          
    return pid

#check_pid(name)




   
def patient_insert():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    name=input("ENTER NAME: ")
    pid=check_pid(name)
    DOB=input("ENTER DATE OF BIRTH(YYYY-MM-DD): ")

    #calculating age
    b_year=int(DOB[0:4])
    DATE=str(datetime.date.today())
    c_year=int(DATE[0:4])
    age=c_year-b_year
   
    sex=input("ENTER SEX(M/F): ")
    address=input("ENTER ADDRESS: ")
    mobile_no=input("ENTER MOBILE NO: ")
    email=input("ENTER EMAIL ADDRESS: ")
   
    #assign random hlth insurance
    ans=input("DO YOU HAVE HEALTH INSURANCE?(Y/N): ")
    if ans in 'Yy':
        l=[15,25,35,50,75]
        hlth_ins= random.choice(l)
    elif ans in 'Nn':
        hlth_ins= None
       
    command="insert into PATIENT_RECORD (PID,PNAME,AGE,DOB,SEX,ADDRESS,MOBILE_NO,EMAIL,HI) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    result=(pid,name.upper(),age,DOB,sex.upper(),address,mobile_no,email,hlth_ins)
    mycursor.execute(command,result)
    mydb.commit()
    print()
    print("RECORD SAVED")
    print("PATIENT ID NO. IS: ",pid)

#patient_insert()

