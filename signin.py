from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import mysql.connector
import subprocess






# Function to open signup window
def signup_page():
    login_window.destroy()
    import signup



# Function to handle the forget password functionality
def forget_pass():
    def change_password():
        # Check if all fields are filled
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error','All Fields Are Requried', parent=window)
        # Check if password and confirm password fields are matching
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching', parent=window)
        else:
            # Connect to the database
            con = pymysql.connect(host='localhost', user='root', password='1234', database='userdata')
            mycursor = con.cursor()
            # Select the row for the given username
            query = 'SELECT * FROM data WHERE username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                # Update the password for the given username
                query = 'UPDATE data SET password=%s WHERE username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                # Show success message and destroy the window
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()

    # Create the forget password window
    window = Toplevel()
    window.title('Change Password')

    # Set the background image
    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    # Set the heading label
    heading_label = Label(window, text='REST PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480,y=60)

    # Set the username label and entry box
    userLabel = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=470, y=130)
    user_entry = Entry(window, width=25, fg='magenta2', font=('airal', 11, 'bold'), bd=0)
    user_entry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470,y=180)

    # Set the new password label and entry box
    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    passwordLabel.place(x=470, y=210)
    newpass_entry = Entry(window, width=25, fg='magenta2', font=('airal', 11, 'bold'), bd=0)
    newpass_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470,y=260)
    
    confirmLabel= Label(window, text='Confirm New Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    confirmLabel.place(x=470, y=290)
    
   #Create the Confirm Password Entry field
    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('airal', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)
    
#Create a separator line below the Confirm Password Entry field
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)
    
#Create the Submit Button
    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans', '16', 'bold'),
    width=19, cursor='hand2', activebackground='magenta2', activeforeground='white', command=change_password)
    submitButton.place(x=470, y=390)
    
#Run the window loop
    window.mainloop()
    
 # Function to handle the login functionality
def login_user():
    # Check if the username and password fields are empty
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            # Establish a connection to the database
            con=pymysql.connect(host='localhost', user='root', password='1234', database='userdata')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return

        # Execute a query to select a user with the provided username and password
        query = "SELECT * FROM data WHERE username=%s AND password=%s"
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()

        # If there is no matching user, show an error message
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            # If there is a matching user, show a success message and open the encrypted page
            messagebox.showinfo('Welcome','Login Successful')
            login_window.destroy()
            subprocess.Popen(["python", "Encryption_Decryption.py"])
            


def hide():
    # Change the eye icon to closed
    openeye.config(file='closeye.png')
    # Hide the password characters
    passwordEntry.config(show='*')
    # Change the button command to show the password
    eyeButton.config(command=show)
    
def show():
    # Change the eye icon to open
    openeye.config(file='openeye.png')
    # Show the password characters
    passwordEntry.config(show='')
    # Change the button command to hide the password
    eyeButton.config(command=hide)
    
def user_enter(event):
    # Delete the default "Username" text when the user clicks on the username entry
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    # Delete the default "Password" text when the user clicks on the password entry
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        
## GUI Part

# Create the login window and set its properties
login_window = Tk()
login_window.geometry('900x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

# Add a background image to the window
bgImage = ImageTk.PhotoImage(file= 'bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0,y=0)

# Add a heading label to the window
heading = Label(login_window, text= 'User Login', font=('Times New Roman', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

# Add a username entry widget
usernameEntry = Entry(login_window, width=25, font=('Times New Roman', 12, 'bold'), bd=0, fg= 'firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>', user_enter)

# Add a line separator below the username entry widget
frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

# Add a password entry widget
passwordEntry = Entry(login_window, width=25, font=('Times New Roman', 12, 'bold'), bd=0, fg= 'firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', password_enter)

# Add a line separator below the password entry widget
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

# Add an eye button to toggle password visibility
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

# Add a "Forgot Password?" button
ForgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Times New Roman', 12, 'bold'), fg='firebrick1', activeforeground='firebrick1', command=forget_pass)
ForgetButton.place(x=715, y=295)

# Add a "Login" button
loginButton = Button(login_window, text= 'Login', font= ('open Sans', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='white',
                     activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

# Add a separator label with text "OR"
orLabel = Label(login_window, text='-------------- OR --------------', font=('Open Sans',16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

# Add social media login options
facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640,y=440)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690,y=440)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel=Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740,y=440)

# Add a "Don't have an account?" label
signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans',9), fg='firebrick1', bg='white')
signupLabel.place(x=590, y=500)

# Add a "Create new one" button for new account creation
newaccountButton = Button(login_window, text= 'Create new one', font= ('open Sans', 9, 'bold underline'), fg='blue', bg='white', activeforeground='blue', activebackground='white', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=500)

# Start the main loop of the Tkinter window
login_window.mainloop()
