import mysql.connector

def patient_delete():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    while True:
        print("1.DELETE BY PATIENT NAME")
        print("2.DELETE BY PATIENT ID")
        print("3.BACK TO MENU")
        #print("4.EXIT")
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            pname=input("ENTER NAME OF PATIENT TO BE DELETED: ")
            mycursor.execute("select * from patient_record where pname='{}'".format(pname))
            result=mycursor.fetchall()
            if result:
               mycursor.execute("delete from patient_record where PNAME='{}'".format(pname))
               mycursor.execute("update patient_id set STATUS='Available', NAME=NULL where NAME='{}'".format(pname))
               mydb.commit()
               print("RECORD DELETED")
            else:
                print("RECORD NOT FOUND")
           
        elif choice==2:
            pid=input("ENTER PATIENT ID TO BE DELETED: ")
            mycursor.execute("select * from patient_record where pid='{}'".format(pid))
            result=mycursor.fetchall()
            if result:
                mycursor.execute("delete from patient_record where PID='{}'".format(pid))
                mycursor.execute("update patient_id set STATUS='Available',NAME=NULL where PID='{}'".format(pid))
                mydb.commit()
                print("RECORD DELETED")
            else:
                print("RECORD NOT FOUND")
           
                   
        elif choice==3:
            return
       
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")
       

       
#patient_delete()

           
