from tkinter import*
stu=""
staff=""
sts=""

def stusignup():
        global sts
        global s3
        sts=Toplevel(a)
        sts.geometry("1000x1000")
        sts.title("student signup")
        s3=PhotoImage(file="im1.gif")
        im3=Label(sts,image=s3).place(x=0,y=0)
        f1=Frame(sts,im3,height=60,width=300,bg='sky blue').place(x=350,y=10)
        t3=Label(sts,f1,text="Student signup",font=('ALGERIAN',26)).place(x=363,y=16)
        er1=Label(sts,text="Full Name:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=80)
        enr1=Entry(sts).place(x=150,y=80,width=250,height=33)
        er2=Label(sts,text="Parent Name:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=130)
        enr2=Entry(sts).place(x=150,y=130,width=250,height=33)
        er3=Label(sts,text="Age:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=180)
        z=StringVar()
        enr3=OptionMenu(sts,z,"3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20",).place(x=150,y=180,width=50,height=33)
        er4=Label(sts,text="D.O.B:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=230)
        enr4=Entry(sts).place(x=150,y=230,width=250,height=33)
        er5=Label(sts,text="Nationality:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=280)
        enr5=Entry(sts).place(x=150,y=280,width=250,height=33)
        savebtn2=Button(sts,text="save",relief=SOLID,height=1,width=15,bg='brown',font=('Britannic Bold',20)).place(x=400,y=440)
def stulogin():
        global stu
        global a2
        stu=Toplevel(a)
        stu.geometry("1000x1000")
        stu.title("student login\signin")
        a2=PhotoImage(file="im9.gif")
        im1=Label(stu,image=a2).place(x=0,y=0)
        f2=Frame(stu,im1,height=60,width=400,bg='grey').place(x=320,y=70)
        t2=Label(stu,f2,text="Student login/signup",font=('ALGERIAN',26)).place(x=330,y=77)
        en1=Label(stu,text="user name:",fg='black',font=("Calibri",16)).place(x=345,y=180)
        ent1=Entry(stu).place(x=450,y=180,width=250,height=33)
        en2=Label(stu,text="Password:",fg='black',font=("Calibri",16)).place(x=350,y=250)
        ent2=Entry(stu).place(x=450,y=250,width=250,height=33)
        logbtn1=Button(stu,text="Login",relief=GROOVE,height=1,width=15,bg='silver',font=('Britannic Bold',20)).place(x=400,y=300)
        en3=Label(stu,im1,text="New Students register by clicking signup",font=('Berlin Sans FB Demi',20)).place(x=290,y=380)
        signbtn1=Button(stu,text="Sign up",relief=SUNKEN,height=1,width=15,bg='chocolate',font=('Britannic Bold',20),command=stusignup).place(x=400,y=440)

def stafflogin():
        global staff
        global a3
        staff=Toplevel(a)
        staff.geometry("1000x1000")
        staff.title("Staff login/signin")
        a3=PhotoImage(file="im8.gif")
        im2=Label(staff,image=a3).place(x=0,y=0)
        f3=Frame(staff,im2,height=60,width=380,bg='pink').place(x=300,y=14)
        t3=Label(staff,f3,text="Staff login/signin",font=('ALGERIAN',26)).place(x=318,y=22)
        enn1=Label(staff,text="user name:",fg='black',font=("Calibri",16)).place(x=345,y=180)
        entr1=Entry(staff).place(x=450,y=180,width=250,height=33)
        enn2=Label(staff,text="Password:",fg='black',font=("Calibri",16)).place(x=350,y=250)
        entr2=Entry(staff).place(x=450,y=250,width=250,height=33)
        loginbtn1=Button(staff,text="Login",relief=GROOVE,height=1,width=15,bg='silver',font=('Britannic Bold',20)).place(x=400,y=300)
        enn3=Label(staff,im2,text="New Staffs register by clicking signup",font=('Berlin Sans FB Demi',20)).place(x=290,y=380)
        signinbtn1=Button(staff,text="Sign up",relief=SOLID,height=1,width=15,bg='chocolate',font=('Britannic Bold',20),command=staffsignup).place(x=400,y=440)
def staffsignup():
        global sta
        global s4
        sta=Toplevel(a)
        sta.geometry("1000x1000")
        sta.title("staff signup")
        s4=PhotoImage(file="im1.gif")
        im2=Label(sta,image=s4).place(x=0,y=0)
        f5=Frame(sta,im2,height=60,width=300,bg='sky blue').place(x=350,y=10)
        t3=Label(sta,f5,text="Staff signup",font=('ALGERIAN',26)).place(x=363,y=16)
        err1=Label(sta,text="Full Name:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=80)
        enrr1=Entry(sta).place(x=260,y=80,width=250,height=33)
        err2=Label(sta,text="Parent Name/Spouse Name:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=130)
        enrr2=Entry(sta).place(x=260,y=130,width=250,height=33)
        err3=Label(sta,text="Age:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=180)
        z1=StringVar()
        enrr3=OptionMenu(sta,z1,"23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","40+").place(x=150,y=180,width=50,height=33)
        err4=Label(sta,text="D.O.B:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=230)
        enrr4=Entry(sta).place(x=260,y=230,width=250,height=33)
        err5=Label(sta,text="Nationality:",fg='black',bg='aqua',font=("Calibri",16)).place(x=10,y=280)
        enrr5=Entry(sta).place(x=260,y=280,width=250,height=33)
        savebtn1=Button(sta,text="save",relief=SOLID,height=1,width=15,bg='brown',font=('Britannic Bold',20)).place(x=400,y=440)








    
a=Tk()
a.geometry("1000x1000")
a1=PhotoImage(file="stuimg.gif")
img=Label(a,image=a1)
img.place(x=0,y=0)
f=Frame(img,height=100,width=500,bg='purple').place(x=250,y=10)
t=Label(f,text="JD SCHOOL MANAGEMENT",fg="black",font=('ALGERIAN','26')).place(x=290,y=40)
b1=Button(img,text="Student detail",relief=FLAT,height=5,width=20,bg='orange',font=('ALGERIAN',22),command=stulogin).place(x=110,y=250)
b2=Button(img,text="Staff detail",relief=FLAT,height=5,width=20,bg='orange',font=('ALGERIAN',22),command=stafflogin).place(x=550,y=250)
a.mainloop()
