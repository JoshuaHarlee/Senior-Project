# Import all modules and functions from tkinter
from tkinter import *
# Import messagebox from tkinter
from tkinter import messagebox
# Import ImageTk from PIL (Python Imaging Library)
from PIL import ImageTk
# Import pymysql for MySQL database connectivity
import pymysql

# Function to clear all input fields
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

# This function connects to a MySQL database and creates a new user in the 'data' table.
def connect_database():
    
    # Check if all fields are filled. If not, show an error message.
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    
    # Check if the password and confirm password fields match. If not, show an error message.
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    
    # Check if the user has accepted the terms and conditions. If not, show an error message.
    elif check.get()==0:
         messagebox.showerror('Error', 'Please Accept Terms & Conditions')  
    
    # If all conditions are met, try to connect to the database.
    else:
        try:
            con=pymysql.connect(host='localhost', user='root',password='1234')
            mycursor=con.cursor()
        except:
            # If there's a problem connecting to the database, show an error message and exit the function.
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
    # This block of code is wrapped in a try-except block to handle any exceptions that might occur
    try:
        # Creating a new database named 'userdata'
        query = 'create database userdata'
        mycursor.execute(query)

        # Setting the active database to the newly created 'userdata'
        query = 'use userdata'
        mycursor.execute(query)

        # Creating a new table named 'data' in the active database with specified columns and their data types
        query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
        mycursor.execute(query)
    except:
        # If there's an exception (e.g. database or table already exists), set the active database to 'userdata'
        mycursor.execute('use userdata')

    # Preparing a query to select rows from the 'data' table where the username matches the user input
    query = 'select * from data where username=%s'
    mycursor.execute(query, (usernameEntry.get(),))
    row = mycursor.fetchone()

    # Checking if a row with the entered username already exists in the table
    if row != None:
        # If it does, display an error message indicating that the username already exists
        messagebox.showerror('Error', 'Username Already exists')
    else:
        # If not, insert a new row into the 'data' table with the user's email, username, and password
        query = 'insert into data(email, username, password) values(%s,%s,%s)'
        mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))

        # Commit the changes to the database and close the connection
        con.commit()
        con.close()

        # Display a success message, indicating that the registration was successful
        messagebox.showinfo('Success', 'Registration is successful')

        # Clear the input fields and close the signup window
        clear()
        signup_window.destroy()

        # Import and run the 'signin' module to allow the user to sign in
        import signin

# Function to open the login page
def login_page():
    signup_window.destroy()
    import signin

# Create the signup window
signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)
background=ImageTk.PhotoImage(file='bg.jpg')

# Add background image to the window
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

# Create a frame for user input fields
frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

# Add heading to the frame
heading=Label(frame,text= 'CREATE AN ACCOUNT', font=('Microsoft  Yahei UI Light', 18, 'bold')
              ,bg='white', fg='firebrick1')
heading.grid(row=0,column=0, padx=10,pady=10)

# Add email label and entry field
emailLabel=Label(frame,text='Email', font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 bg='white',fg='firebrick1')

emailLabel.grid(row=1,column=0, sticky='w', padx=25, pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1' )
emailEntry.grid(row=2,column=0,sticky='w', padx=25, pady=(10,0))

# Add username label and entry field
usernameLabel=Label(frame,text='Username', font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0, sticky='w', padx=25, pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1' )
usernameEntry.grid(row=4,column=0,sticky='w', padx=25)

# Add password label and entry field
passwordLabel=Label(frame,text='Password', font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0, sticky='w', padx=25, pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1' )
passwordEntry.grid(row=6,column=0,sticky='w', padx=25)

# Add confirm password label and entry field
confirmLabel=Label(frame,text='Confirm Password', font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0, sticky='w', padx=25)

confirmEntry=Entry(frame,width=30,font=('Microsoft  Yahei UI Light', 10, 'bold'),
                 fg='white', bg='firebrick1' )
confirmEntry.grid(row=8,column=0,sticky='w', padx=25, pady=(10,0))

# Create IntVar for storing the state of the terms and conditions checkbox
check=IntVar()

# Add terms and conditions checkbox
termsandcondition=Checkbutton(frame,text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 9, 'bold')
                              , fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1'
                              ,cursor='hand2', variable=check)
termsandcondition.grid(row=9,column=0, pady=10,padx=15)

# Add signup button
signupButton=Button(frame,text='Signup',font=('Microsoft Yahei UI Light', 16, 'bold'),bd=0,bg='firebrick1', fg='white',
                     activebackground='firebrick1', activeforeground='white', width=17,
                     cursor='hand2', command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

# Add "already have an account?" label
alreadyaccount=Label(frame, text='Already have an account?', font=('Open Sans', '9', 'bold'),
                     bg='white', fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky= 'w',padx=25,pady=10)

# Add login button
loginButton=Button(frame,text= 'Log in', font= ('open Sans', 9, 'bold underline'),
                  fg='blue', bg='white', activeforeground='blue', 
                  activebackground='white', cursor='hand2', bd=0, command=login_page)
loginButton.place(x=184,y=396)

# Start the main event loop of the signup window
signup_window.mainloop()
