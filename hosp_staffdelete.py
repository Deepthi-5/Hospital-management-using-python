import mysql.connector

def staff_delete():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    while True:
        print("="*50)
        print("1.DELETE BY NAME")
        print("2.DELETE BY STAFF ID")
        print("3.BACK TO MENU")
        print("="*50)
        choice=int(input("ENTER CHOICE: "))
        if choice==1:
            name=input("ENTER NAME OF STAFF TO BE DELETED: ")
            mycursor.execute("select designation from staff_record where name='{}'".format(name))
            res=mycursor.fetchall()
            if res:
                dsgn=res[0][0]
                mycursor.execute("delete from staff_record where name='{}'".format(name))
                if dsgn.upper()=="DOCTOR":
                    mycursor.execute("update doctor_record set sid=NULL,sname=NULL,dept=NULL,service_cost=NULL,slot=NULL where sname='{}'".format(name))
                mycursor.execute("update staff_id set status='Available',name=NULL where name='{}'".format(name))
                mydb.commit()
                print("RECORD DELETED")  
            else:
                print("RECORD NOT FOUND")
               
        elif choice==2:
            sid=input("ENTER STAFF ID OF STAFF TO BE DELETED: ")
            mycursor.execute("select designation from staff_record where sid='{}'".format(sid))
            res=mycursor.fetchall()
            if res:
                dsgn=res[0][0]
                mycursor.execute("delete from staff_record where sid='{}'".format(sid))
                if dsgn.upper()=="DOCTOR":
                    mycursor.execute("update doctor_record set sid=NULL,sname=NULL,dept=NULL,service_cost=NULL,slot=NULL where sid='{}'".format(sid))
                mycursor.execute("update staff_id set status='Available',name=NULL where sid='{}'".format(sid))
                mydb.commit()
                print("RECORD DELETED")
            else:
                print("RECORD NOT FOUND")

        elif choice==3:
            return

        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")

#staff_delete()
