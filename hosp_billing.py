import mysql.connector
import datetime
from tabulate import tabulate

   
def billing():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Deepu123',charset='utf8',database='hospital_management')
    mycursor=mydb.cursor()
    pid=input("ENTER PATIENT ID: ")
    print("="*50)
    print()
    mycursor.execute("select * from billing where paystatus='NOT PAID' and pid='{}'".format(pid))
    rec1=mycursor.fetchall()
    if rec1:
        date=rec1[0][8]
        print(tabulate(rec1,headers=["PATIENT ID","PATIENT NAME","DOCTOR NAME","DEPARTMENT","SLOT","INITIAL COST","DISCOUNT COST","TOTAL COST","DATE OF PAYMENT","PAY STATUS"],tablefmt='fancy_grid'))
        ch=input("PROCEED WITH PAYMENT?(Y/N): ")
        if ch in "Yy":
            mycursor.execute("update doctor_record set availability='Y',pid=NULL where pid='{}'".format(pid))
            mycursor.execute("update billing set paystatus='PAID' where pid='{}' and date='{}'".format(pid,date))
            mydb.commit()
            print("PAYMENT RECORDED.")
        else:
            print("PAYMENT NOT RECORDED.")
    else:
        print("RECORD NOT FOUND.")

#billing()    

