import mysql.connector
import pymysql
import tkinter.messagebox
from tkinter.ttk import Combobox
from tkinter import *
import os
# connecting to the database
connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset='utf8',
                                       database="efooddelivery")
cursordb = connectiondb.cursor(buffered=True)
cursordb.execute("truncate table login")


def only_numbers(char):
    if char.isdigit():
        return TRUE
    elif char == "":
        return TRUE
    else:
        messagebox.showinfo('Information', 'Only digits are allowed !')
        return False

def only_chars(char):
    if char.isalpha():
        return TRUE
    elif char == "":
        return TRUE
    else:
        messagebox.showinfo('Information', 'Enter Valid Name. Numbers not allowed here !')
        return False


# Function for validating all other user input fields
def validateAllFields():
    print('.....mobileno get...',mobileno.get())
    mobile_no_sql = "select count(*) from customer where login_id = %s"
    cursordb.execute(mobile_no_sql, [(mobileno.get())])
    mobile_no_result = cursordb.fetchone()
    mobile_no = mobile_no_result[0]
    print('......in validate fields.....',mobile_no)
    if firstname.get() == "":
        messagebox.showinfo('Information', 'Please enter first name to Proceed')
    elif lastname.get() == "":
        messagebox.showinfo('Information', 'Please enter last name to Proceed')
    elif address.get() == "":
        messagebox.showinfo('Information', 'Please enter address to Proceed')
    elif city.get() == "":
        messagebox.showinfo('Information', 'Please enter city to Proceed')
    elif len(postalcode.get()) != 6:
        messagebox.showinfo('Information', 'Postal code should be 6 digits')
    elif nearbylandmark.get() == "":
        messagebox.showinfo('Information', 'Please enter nearbylandmark to Proceed')
    elif len(mobileno.get()) != 10:
        messagebox.showinfo('Information', 'Phone number should be 10 digits')
    elif len(mobileno.get()) == 10 and mobile_no == 1:
        print('inside not None check')
        messagebox.showinfo('Information', 'Phone number already exists !')
    elif len(cd_no.get()) != 16:
        messagebox.showinfo('Information', 'Card Number should be 16 digits')
    elif len(cvv.get()) != 3:
        messagebox.showinfo('Information', 'CVV should be 3 digits')
    else:
        register_user()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("1600x800")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=15, font=('Trajan Pro', 18, 'bold'), relief="groove",
          fg="white",
          bg="orange", width=500).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Registered Mobile Number :", fg="black", font=('Trajan Pro', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('Trajan Pro', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="orange", fg='white', relief="groove", font=('Trajan Pro', 12, 'bold'),
           command=login_verification).pack()
    Label(root2, text="")

def order_open():
    logged_message.destroy()
    os.system('menu.py')
def order_open1():
    registered_message.destroy()
    os.system('menu.py')

def failed_destroy():
    failed_message.destroy()


def logged(cid_pass):
    root2.destroy()
    username_verification.set("")
    password_verification.set("")
    cid_pass1 = cid_pass
    print(cid_pass1)
    global logged_message
    #logged_message = Toplevel(root2)
    logged_message = Toplevel()
    logged_message.title("Welcome")
    logged_message.geometry("500x125")
    Label(logged_message, text="Login Successful!... Welcome", fg="green",
          font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Place order", bg="orange", fg='white', relief="groove", font=('Trajan Pro', 12, 'bold'),
           command=order_open).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x125")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="orange", fg='white', relief="groove", font=('Trajan Pro', 12, 'bold'),
           command=failed_destroy).pack()

def CID(cid):
    LoginCID.cid = cid
    print('...inside global...',LoginCID.cid)

def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from customer where login_id = %s and password = %s"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            cid_sql = "select cid from customer where login_id = %s and password = %s"
            cursordb.execute(cid_sql, [(user_verification), (pass_verification)])
            cidresult = cursordb.fetchone()
            print(cidresult)
            cid_pass=cidresult[0]
            print(cid_pass)
            #cursordb.execute("insert into login (cid) values({}".format(cid_pass))
            cursordb.execute("insert into login (cid) values(%s)" %(cid_pass))
            #cid_login_insert_query = """INSERT INTO login (cid) VALUES (%s) """
            #cid_login_record = (cid_pass)
            #cursordb.execute(cid_login_insert_query, cid_login_record)
            connectiondb.commit()
            logged(cid_pass)
            #CID(cid_pass)
            break
    else:
        failed()




def register_user():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    addresss_info = address.get()
    city_info = city.get()
    postalcode_info = postalcode.get()
    nearbylandmark_info = nearbylandmark.get()
    mobileno_info = mobileno.get()
    password_info = password.get()
    cd_no_info = cd_no.get()
    cvv_info = cvv.get()
    global cid

    cursordb.execute("select max(cid)+1 from customer")
    cid = cursordb.fetchone()[0]

    print(cid)

    mySql_insert_query = """INSERT INTO customer (cid,first_name,last_name,address,city, postal_code,nearby_landmark,login_id,password,cd_no,cvv) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s) """

    record = (
    cid, firstname_info, lastname_info, addresss_info, city_info, postalcode_info, nearbylandmark_info, mobileno_info,
    password_info,cd_no_info,cvv_info)
    cursordb.execute(mySql_insert_query,record)
    connectiondb.commit()

    cid_sql = "select cid from customer where login_id = %s"
    cursordb.execute(cid_sql, [(mobileno_info)])
    cidresult = cursordb.fetchone()
    print('......register user...',cidresult)
    cid_pass = cidresult[0]
    print(cid_pass)
    cursordb.execute("insert into login (cid) values(%s)" % (cid_pass))
    connectiondb.commit()


    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    postalcode_entry.delete(0, END)
    nearbylandmark_entry.delete(0, END)
    mobileno_entry.delete(0, END)
    password_entry.delete(0, END)
    cd_no_entry.delete(0,END)
    cvv_entry.delete(0,END)

    registered()


def registered():
    register_screen.destroy()
    global registered_message
    registered_message = Toplevel(root)
    registered_message.title("Welcome")
    registered_message.geometry("500x125")
    Label(registered_message, text="Registered Successfully!... Welcome", fg="green",
          font="bold").pack()
    Label(registered_message, text="").pack()
    Button(registered_message, text="Place order", bg="orange", fg='white', relief="groove", font=('Trajan Pro', 12, 'bold'),
           command=order_open1).pack()



def register():
    global register_screen
    register_screen = Toplevel()
    register_screen.title("Register")
    register_screen.geometry("1000x800")

    global firstname
    global lastname
    global address
    global city
    global postalcode
    global nearbylandmark
    global mobileno
    global password
    global cd_no
    global cvv
    global firstname_entry
    global lastname_entry
    global address_entry
    global city_entry
    global postalcode_entry
    global nearbylandmark_entry
    global mobileno_entry
    global password_entry
    global cd_no_entry
    global cvv_entry
    firstname = StringVar()
    lastname = StringVar()
    address = StringVar()
    city = StringVar()
    postalcode = StringVar()
    nearbylandmark = StringVar()
    mobileno = StringVar()
    password = StringVar()
    cd_no=StringVar()
    cvv=StringVar()

    Label(register_screen, text="Please enter details below", bg="orange",font=('Trajan Pro',20,'bold')).place(x=0,y=0)
    Label(register_screen, text="").place()
    firstname_lable = Label(register_screen, text="First Name * ",font=('Trajan Pro',12))
    firstname_lable.place(x=10,y=100)
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.place(x=10,y=125)
    valid_firstname= register_screen.register(only_chars)
    firstname_entry.config(validate="key", validatecommand=(valid_firstname, '%P'))
    lastname_lable = Label(register_screen, text="Last Name * ",font=('Trajan Pro',12))
    lastname_lable.place(x=10,y=200)
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.place(x=10,y=225)
    valid_lastname= register_screen.register(only_chars)
    lastname_entry.config(validate="key", validatecommand=(valid_lastname, '%P'))
    address_lable = Label(register_screen, text="Address * ",font=('Trajan Pro',12))
    address_lable.place(x=10,y=300)
    address_entry = Entry(register_screen, textvariable=address)
    address_entry.place(x=10,y=325)
    city_lable = Label(register_screen, text="City * ",font=('Trajan Pro',12))
    city_lable.place(x=10,y=400)
    city_entry = Entry(register_screen, textvariable=city)
    city_entry.place(x=10,y=425)
    postalcode_lable = Label(register_screen, text="Postal Code * ",font=('Trajan Pro',12))
    postalcode_lable.place(x=10,y=500)
    postalcode_entry = Entry(register_screen, textvariable=postalcode)
    postalcode_entry.place(x=10,y=525)
    valid_postalcode = register_screen.register(only_numbers)
    postalcode_entry.config(validate="key", validatecommand=(valid_postalcode, '%P'))
    nearbylandmark_lable = Label(register_screen, text="Nearby Landmark * ",font=('Trajan Pro',12))
    nearbylandmark_lable.place(x=10,y=600)
    nearbylandmark_entry = Entry(register_screen, textvariable=nearbylandmark)
    nearbylandmark_entry.place(x=10,y=625)
    mobileno_lable = Label(register_screen, text="Mobile Number * ",font=('Trajan Pro',12))
    mobileno_lable.place(x=500,y=100)
    mobileno_entry = Entry(register_screen, textvariable=mobileno)
    mobileno_entry.place(x=500,y=125)
    valid_mobileno = register_screen.register(only_numbers)
    mobileno_entry.config(validate="key", validatecommand=(valid_mobileno, '%P'))
    password_lable = Label(register_screen, text="Password * ",font=('Trajan Pro',12))
    password_lable.place(x=500,y=200)
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.place(x=500,y=225)
    cd_no_lable = Label(register_screen, text="Card Number * ",font=('Trajan Pro',12))
    cd_no_lable.place(x=500,y=300)
    cd_no_entry = Entry(register_screen, textvariable=cd_no)
    cd_no_entry.place(x=500,y=325)
    valid_cd_no = register_screen.register(only_numbers)
    cd_no_entry.config(validate="key", validatecommand=(valid_cd_no, '%P'))
    cvv_lable = Label(register_screen, text="cvv * ",font=('Trajan Pro',12))
    cvv_lable.place(x=500,y=400)
    cvv_entry = Entry(register_screen, textvariable=cvv,show="*")
    cvv_entry.place(x=500,y=425)
    valid_cvv = register_screen.register(only_numbers)
    cvv_entry.config(validate="key", validatecommand=(valid_cvv, '%P'))


    Label(register_screen, text="").place()
    Button(register_screen, text="Register", height="1", width="20", bg="orange", fg='white', relief="groove",
           font=("Trajan Pro", 13), command=validateAllFields).place(x=700,y=700)


def main_display():
    global root
    root = Tk()
    root.title("Yummy corner")
    root.geometry("1000x800")

    Label(root, text="Welcome to Yummy Corner", bg="orange", width="500", height="5", font=("Trajan Pro", 18)).pack()
    Label(root, text="").pack()
    Button(root, text="Login", height="5", width="20", bg="orange", fg='white', relief="groove", font=("Trajan Pro", 13),
           command=login).place(x=400,y=300)
    Label(root, text="").pack()
    Button(root, text="Register", height="5", width="20", bg="orange", fg='white', relief="groove",
           font=("Trajan Pro", 13), command=register).place(x=400,y=600)
    Label(root, text="").pack()

main_display()
root.mainloop()
