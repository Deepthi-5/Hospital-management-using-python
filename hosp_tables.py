#please save the file names as whatever i've given as the subject so that you don't have to make any changes
#don't forget to change the password in all the programs(or change your sql password)


import mysql.connector

def create_table():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd="Deepu123",charset="utf8",database="hospital_management")
    mycursor=mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS PATIENT_RECORD(PID VARCHAR(4) PRIMARY KEY , PNAME VARCHAR(50) , AGE INT(3) , DOB DATE , SEX VARCHAR(1), ADDRESS VARCHAR(100), MOBILE_NO VARCHAR(20) , EMAIL VARCHAR(50) , HI INT(2))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS PATIENT_ID(PID VARCHAR(4) PRIMARY KEY , NAME VARCHAR(50), STATUS VARCHAR(9))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS STAFF_RECORD(SID VARCHAR(4) PRIMARY KEY , NAME VARCHAR(50) ,MOBILE_NO VARCHAR(20), DOA DATE , DEPT VARCHAR(50), DESIGNATION VARCHAR(10),SHIFT VARCHAR(5),SERVICE_COST INT(10))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS STAFF_ID(SID VARCHAR(4) PRIMARY KEY , NAME VARCHAR(50) ,STATUS VARCHAR(10))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS DOCTOR_RECORD (SNO int(4)primary key,SID varchar(4),SNAME varchar(50),DEPT VARCHAR(20),SERVICE_COST INT(10),SLOT varchar(10),AVAILABILITY VARCHAR(1),PID VARCHAR(4))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS BILLING (PID VARCHAR(4),PNAME VARCHAR(50),SNAME VARCHAR(50),DEPT VARCHAR(20),SLOT VARCHAR(10),INITIAL_COST INT(10),DISCOUNT_COST INT(10),TOTAL_COST INT(10),DATE DATE,PAYSTATUS VARCHAR(8))")
    mydb.commit()

#create_table()
