from tkinter import *
from tkinter import messagebox
import psycopg2

window=Tk()
window.title('SignUp')
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False,False)


def signin():
    username = user.get()
    password = code.get()

    try:
        conn = psycopg2.connect(
            dbname="project",  
            user="postgres", 
            password="rohan@3381",  
            host="localhost",  
            port="5432"  
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO userdetail (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
        conn.close()
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error registering user: {e}")


img=PhotoImage(file='/home/rohan/Desktop/Music Player/images/signup.png')
Label(window,image=img,bg='white').place(x=100,y=150)

frame=Frame(window,width=350,height=390,bg='white')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Arial',23,'bold'))
heading.place(x=100,y=5)

#####################-------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

####################--------------------------------------------------------

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')



code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#############################################################
# def on_enter(e):
#     confirm_code.delete(0,'end')
# def on_leave(e):
#     name=confirm_code.get()
#     if name=='':
#         confirm_code.insert(0,'Confirm Password')


# confirm_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
# confirm_code.place(x=30,y=220)
# confirm_code.insert(0,'Confirm Password')
# confirm_code.bind('<FocusIn>', on_enter)
# confirm_code.bind('<FocusOut>',on_leave)

# Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
#############################################################

Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signin).place(x=15,y=200)









window.mainloop()
