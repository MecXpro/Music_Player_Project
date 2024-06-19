from tkinter import *
from tkinter import messagebox
import psycopg2
    
def verify_login(username, password):
    user_id=None
    try:
        
        conn = psycopg2.connect(
            dbname="project",  
            user="postgres",   
            password="rohan@3381", 
            host="localhost",         
            port="5432"               
        )
        cursor = conn.cursor()

    
        cursor.execute("SELECT user_id FROM userdetail WHERE username = %s AND password = %s", (username, password))
        user_id = cursor.fetchone()
        

        if user_id:
            user_id=user_id[0]
           
            root.destroy() 
           
            import music_player
            music_player.create_signup_window()
                  
            
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        messagebox.showerror("Database Error", "Failed to connect to the database.")
    return user_id

   
      
def signin():
    username = user.get()
    password = code.get()
    user_id=verify_login(username, password)
   
def signup():
    username = user.get()
    password = code.get()
    
def open_signup_page():
    root.destroy()  
    import signup 
    signup.create_signup_window()

root = Tk()
root.title('Music Player login')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='/home/rohan/Desktop/Music Player/images/login.png') 
Label(root, image=img, bg='white').place(x=40, y=-50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Arial', 23, 'bold'))
heading.place(x=100, y=5)
#_________________________________________________________________________________________________________________________________________
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
user.place(x=45, y=100)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

#_________________________________________________________________________________________________________________________________________
def on_enter(e):
    user_id.delete(0,'end')
def on_leave(e):
    name1=user_id.get()
    with open("user_id.txt","w")as file:
          file.write(name1)
    if name1=='':
        user.insert(0,'user_id')

user_id = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
user_id.place(x=45, y=50)
user_id.insert(0, 'user_id')
user_id.bind('<FocusIn>', on_enter)
user_id.bind('<FocusOut>',on_leave)

#__________________________________________________________________________________________________________________________________________

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Arial', 11))
code.place(x=45, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)

Button(frame, width=39, pady=7, text='Log in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)


Button(root, text="Don't have an account? Sign up here", bg='white', fg='#57a1f8', border=0, font=('Arial', 10, 'underline'), command=open_signup_page).place(x=480, y=430)

root.mainloop()
