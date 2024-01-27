from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from MyGlobals import *
connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset='utf8',
                                       database="efooddelivery")
cursordb = connectiondb.cursor(buffered=True)

cursordb.execute('use efooddelivery')

cid_sql = "select cid from login"
cursordb.execute(cid_sql)
cid_temp = cursordb.fetchone()
cid=cid_temp[0]
print('....inside menu...',cid)


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', "end", values=i)


def search():
    v = q.get()

    # date = '16-06-1998'
    cond1 = (len(v) == 10)
    cond2 = (len(v.split('-')) == 3)
    if cond1 and cond2:
        dd, mm, yyyy = v.split('-')
        cond3 = (1 <= int(dd) <= 31)
        cond4 = (1 <= int(mm) <= 12)
        cond5 = (1000 <= int(yyyy) <= 2021)
        if cond3 and cond4 and cond5:
            query = "select * from Order_History where date='{}' and cid={}".format(v,cid)
            cursordb.execute(query)
            rows = cursordb.fetchall()
            answer.config(text=' ')
            if len(rows) == 0:
                answer.config(text='No matching results')
                print("line44")
            if mm == "02" and (int(dd) == 30 or int(dd) == 31):
                answer.config(text='Oops!! Invaild Date Entered ')
                print("line47")
            update(rows)
        else:
            answer.config(text='Oops!! Invaild Date Entered ')
            print("line51")
    else:
        answer.config(text='Enter correct date in DD-MM-YYYY format')
        print("line54")




root = Tk()
q = StringVar()
wrapper1 = LabelFrame(root, text="Order History:", font=("arial", 11, 'italic'))
wrapper2 = LabelFrame(root, text="Search:", font=("arial", 13, 'italic'))

wrapper1.pack(fill="both", expand='yes', padx=20, pady=10)
wrapper2.pack(fill="both", expand='yes', padx=20, pady=10)

style = ttk.Style()
style.configure("Treeview.Heading", font=("rockwell", 15, "bold"), fg="blue")

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6,7), show="headings", height=15)
trv.pack()
trv.heading(1, text="Customer_id:")
trv.heading(2, text="Item_Name:")
trv.heading(3, text="Price:")
trv.heading(4, text="Quantity:")
trv.heading(5, text="Amount:")
trv.heading(6, text="Date:")
trv.heading(7,text="Time:")
query = "select * from Order_History where cid={}".format(cid)
cursordb.execute(query)
rows = cursordb.fetchall()
update(rows)

# search:

lbl = Label(wrapper2, text="Enter Date To Search:", font=("arial", 12, 'bold'))
lbl.pack(side=tk.LEFT, padx=10)
entry = Entry(wrapper2, textvariable=q)
entry.pack(side=tk.LEFT, padx=6)
butt = Button(wrapper2, text='Search', command=search)
butt.pack(side=tk.LEFT, padx=6)

answer = Label(wrapper1, text='', font=("arial", 16, 'bold'))
answer.pack(pady=20)

root.title("Order history")
root.geometry("800x700")
root.mainloop()
