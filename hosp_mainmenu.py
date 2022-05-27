from hosp_tables import *

from hosp_outpatient import *
from hosp_billing import *
from hosp_patientinsert import *
from hosp_patientdelete import *
from hosp_patientsearch import *
from hosp_patientupdate import *
from hosp_patientcount import *

from hosp_staffinsert import *
from hosp_staffdelete import *
from hosp_staffsearch import *
from hosp_staffupdate import *
from hosp_staffcount import *

#import stdiomask

def patientadm_menu():
    while True:
        print("\t\t\t***PATIENT ADMINISTRATION MENU***")
        print("="*75)
        print("1.OUT PATIENT RECORD")
        print("2.BILLING")
        print("3.INSERT NEW PATIENT RECORD")
        print("4.DELETE PATIENT RECORD")
        print("5.SEARCH PATIENT RECORD")
        print("6.UPDATE PATIENT RECORD")
        print("7.PATIENT RECORD COUNT")
        print("8.FIND PATIENT ID/APPOINTMENT")
        print("9.BACK TO MAIN MENU")
        print("="*75)
        choice=int(input("ENTER CHOICE: "))
        print()
        if choice==1:
            outpatient()
        elif choice==2:
            billing()
        elif choice==3:
            patient_insert()
        elif choice==4:
            patient_delete()
        elif choice==5:
            patient_search()
        elif choice==6:
            patient_update()
        elif choice==7:
            patient_count()
        elif choice==8:
            find_pid()
        elif choice==9:
            return
        else:
            print("INVALID CHOICE. TRY AGAIN.")


def staffadm_menu():
    while True:
        print("\t\t\t***STAFF ADMINISTRATION MENU***")
        print("="*75)
        print("1.INSERT STAFF RECORD")
        print("2.DELETE STAFF RECORD")
        print("3.SEARCH STAFF RECORD")
        print("4.UPDATE STAFF RECORD")
        print("5.STAFF RECORD COUNT")
        print("6.FIND STAFF ID/APPOINTMENTS")
        print("7.BACK TO MAIN MENU")
        print("="*75)
        choice=int(input("ENTER CHOICE: "))
        print()
        if choice==1:
            staff_insert()
        elif choice==2:
            staff_delete()
        elif choice==3:
            staff_search()
        elif choice==4:
            staff_update()
        elif choice==5:
            staff_count()
        elif choice==6:
            find_sid()
        elif choice==7:
            return
        else:
            print("INVALID CHOICE. TRY AGAIN.")
       


def main_menu():
    while True:
        print("\t\t\t***MAIN MENU***")
        print()
        print("="*75)
        print("A.PATIENT ADMINISTRATION")
        print("B.STAFF ADMINISTRATION")
        print("C.EXIT")
        print("="*75)
        choice=input("ENTER CHOICE: ")
        print()
        if choice in "aA":
            patientadm_menu()
        elif choice in "bB":
            staffadm_menu()
        elif choice in "cC":
            return
        else:
            print("INVALID CHOICE.TRY AGAIN.")



from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="image.jpeg")
        self.bg_label=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_Login=Frame(self.root,bg="white")
        Frame_Login.place(x=150,y=150,height=340,width=500)


        title=Label(Frame_Login,text="Login Here",font=("impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_Login,text="Employee Login Area",font=("goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)
        bl_user=Label(Frame_Login,text="Username",font=("impact",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_Login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
       
        pbl_user=Label(Frame_Login,text="Password",font=("impact",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_Login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget=Button(Frame_Login,text="forget password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login=Button(self.root,command=self.login,text="Login",bg="white",fg="#d77337",bd=0,font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    def login(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txt_pass.get()!="1234" or self.txt_user.get()!="admin":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showerror("Welcome",f"Welcome {self.txt_user.get()}\n Your Password:{self.txt_pass.get()}",parent=self.root)
            main_menu()
                                 
       
root=Tk()
obj=Login(root)
root.mainloop()        
