import mysql.connector
import datetime
#add pid to doctor record
#every time new added to doctor record check sno


def check_sid(name):
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    mycursor.execute("select * from staff_id")
    result=mycursor.fetchall()
    if result:
         mycursor.execute("select * from staff_id where STATUS='Available'")
         res=mycursor.fetchall()
         if res:
                  sid=res[0][0]
                  mycursor.execute("update staff_id set STATUS='Occupied',NAME=%s where sid=%s",(name,sid))
                  mydb.commit()
         else:
                if len(str(int(result[-1][0])+1))==1:
                        sid="000"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==2:
                        sid="00"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==3:
                        sid="0"+str(int(result[-1][0])+1)
                elif len(str(int(result[-1][0])+1))==4:
                        sid=str(int(result[-1][0])+1)
                command="insert into staff_id (sid,name,status) values (%s,%s,%s)"
                rec=sid,name,"Occupied"
                mycursor.execute(command,rec)
                mydb.commit()        
    else:
        sid="0001"
        command="insert into staff_id (sid,name,status) values (%s,%s,%s)"
        rec=sid,name,"Occupied"
        mycursor.execute(command,rec)
        mydb.commit()          
                 
    return sid
#check_sid(name)




def check_did():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
   
    mycursor.execute("select sno from doctor_record where SNAME IS NULL")
    result=mycursor.fetchall()
    if result:
        sno=result[0][0]
        for i in range (sno,sno+12):
            mycursor.execute("delete from doctor_record where sno='{}'".format(i))
           
    else:
        mycursor.execute("select count(*) from doctor_record")
        result=mycursor.fetchall()
        if result:
            sno=result[0][0]+1
        else:
            sno=1
    return sno  
#check_did()


def staff_insert():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    name=input("ENTER STAFF NAME: ")
    sid=check_sid(name)
    mno=input("ENTER MOBILE NO: ")
    DOA=input("ENTER DATE OF ADMISSION(YYYY-MM-DD): ")
    shift=input("ENTER SHIFT(DAY/NIGHT):")
    dsgn=input("ENTER DESIGNATION(DOCTOR/NURSE/STAFF): ")
    if dsgn.upper()=="DOCTOR":
        while True:
            print("="*50)
            print("1.ORTHODONTIST")
            print("2.ENDODONTIST")
            print("3.IMPLANTOLOGIST")
            print("4.GENERAL DENTIST")
            print("5.PAEDODONTICS")
            print("6.PERIODONTAL")
            print("="*50)
            choice=int(input("ENTER DEPARTMENT: "))
            print()
            if choice==1:
                    dept="ORTHODONTIST"
                    cost=1500
                    break
            elif choice==2:
                    dept="ENDODONTIST"
                    cost=2000
                    break
            elif choice==3:
                    dept="IMPLANTOLOGIST"
                    cost=1200
                    break
            elif choice==4:
                    dept="GENERAL DENTIST"
                    cost=1000
                    break
            elif choice==5:
                    dept="PAEDODONTICS"
                    cost=1100
                    break
            elif choice==6:
                    dept="PERIODONTAL"
                    cost=2500
                    break
            else:
                print("INVALID CHOICE. TRY AGAIN")          




   
    if dsgn.upper()=="DOCTOR":
        comm1="insert into staff_record values (%s,%s,%s,%s,%s,%s,%s,%s)"
        rec1=(sid,name,mno,DOA,dept,dsgn,shift,cost)
        mycursor.execute(comm1,rec1)
        mydb.commit()
        sno=check_did()
        if shift.upper()=="DAY":
                l=["9AM_10AM","10AM_11AM","11AM_12PM","12PM_1PM","1PM_2PM","2PM_3PM","3PM_4PM","4PM_5PM","5PM_6PM","6PM_7PM","7PM_8PM","8PM_9PM"]
                availability="Y"
        elif shift.upper()=="NIGHT":
                l=["9PM_10PM","10PM_11PM","11PM_12AM","12AM_1AM","1AM_2AM","2AM_3AM","3AM_4AM","4AM_5AM","5AM_6AM","6AM_7AM","7AM_8AM","8AM_9AM"]
                availability="Y"
        mycursor.execute("select sno from doctor_record where SNAME IS NULL")
        res1=mycursor.fetchall()
        if res1:
            x=sno+11
            for i in l:
                com="update doctor_record set SID=%s,SNAME=%s,DEPT=%s,SERVICE_COST=%s,SLOT=%s,AVAILABILITY=%s where SNO=%s"
                rec=(sid,name,dept,cost,i,availability,sno)
                mycursor.execute(com,rec)
                if sno<x:
                    sno+=1
                else:
                    break
        else:
            for i in l:
                com="insert into doctor_record (SNO,SID,SNAME,DEPT,SERVICE_COST,SLOT,AVAILABILITY) values(%s,%s,%s,%s,%s,%s,%s)"
                rec=(sno,sid,name,dept,cost,i,availability)
                mycursor.execute(com,rec)
                sno+=1




 
    elif dsgn.upper()=="NURSE":
        cost=800
        dept=None
        command="insert into staff_record(SID,NAME,MOBILE_NO,DOA,DEPT,DESIGNATION,SHIFT,SERVICE_COST) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        rec=(sid,name.upper(),mno,DOA,dept,dsgn.upper(),shift.upper(),cost)
        mycursor.execute(command,rec)
    elif dsgn.upper()=="STAFF":
        cost=500
        dept=None
        command="insert into staff_record(SID,NAME,MOBILE_NO,DOA,DEPT,DESIGNATION,SHIFT,SERVICE_COST) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        rec=(sid,name.upper(),mno,DOA,dept,dsgn.upper(),shift.upper(),cost)
        mycursor.execute(command,rec)
    mydb.commit()
    print("RECORD SAVED")
    print("STAFF ID IS: ",sid)
    print("="*50)
   


#staff_insert()
