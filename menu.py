from tkinter import*
import random
import time
from datetime import*
from tkinter import Tk,StringVar,ttk,messagebox
import mysql.connector
from MyGlobals import *
import os

# connecting to the database
connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset='utf8',
                                       database="efooddelivery")
cursordb = connectiondb.cursor(buffered=True)

global cid

root=Tk()
root.geometry("1800x1050")
root.title(("Yummy Corner"))

cid_sql = "select cid from login"
cursordb.execute(cid_sql)
cid_temp = cursordb.fetchone()
cid=cid_temp[0]
print('....inside menu...',cid)




#==========================FRAMES=========================================================

tops=Frame(root,width=1800,height=50,bd=10,relief="raise",bg="orange")
tops.pack(side=TOP)
Labelmenu=Label(root,text="MENU",fg="white",relief="raised",font=("Calibri",25,"bold"),width=50,bg="blue",bd=1)
Labelmenu.place(x=500,y=4)

topsleft1=Frame(root,width=600,height=1000,bd=1,relief="raise")
topsleft1.pack(side=LEFT)

topsleft2=Frame(topsleft1,width=600,height=350,bd=1,relief="raise")
topsleft2.pack(side=TOP)

topsleft3=Frame(topsleft1,width=600,height=350,bd=1,relief="raise")
topsleft3.pack(side=BOTTOM)

topsleft4=Frame(topsleft1,width=600,height=350,bd=1,relief="raise")
topsleft4.pack(side=BOTTOM)

topsleft5=Frame(root,width=1200,height=350,bd=1,relief="raise")
topsleft5.pack(side=TOP)

topsleft6=Frame(topsleft5,width=600,height=350,bd=1,relief="raise")
topsleft6.pack(side=LEFT)

topsleft6=Frame(topsleft5,width=600,height=350,bd=1,relief="raise")
topsleft6.pack(side=RIGHT)

topsright2=Frame(root,width=1200,height=700,relief="raise",bd=20)
topsright2.pack(side=RIGHT)






#==========================================VARIABLES===================================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()

var23=StringVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var30 = IntVar()
varcvv = StringVar()


varSpicychickendoublepattyburger=StringVar()
varPannerdoublepattyburger=StringVar()
varVegburger=StringVar()
varPannerwrap=StringVar()
varaloowrap=StringVar()
varcheesecorndelightsandwich=StringVar()
varchickentandoorisandwich=StringVar()
varveggrilledsandwich=StringVar()
varExtracheesepannersandwich=StringVar()
varchocolava=StringVar()
varstrawberryicecream=StringVar()
varpancakessyrup=StringVar()
varchocolateicecream=StringVar()
varvanillamilkshake=StringVar()
varcoke=StringVar()
varsprite=StringVar()
varmiranda=StringVar()
var7up=StringVar()
varhashbrown=StringVar()
vargarlicbread=StringVar()
varfrenchfriesm=StringVar()
varfrenchfriesL=StringVar()

vartotal=StringVar()
varsubTotal=IntVar()
varsgst=StringVar()
varcgst=StringVar()


varSpicychickendoublepattyburger.set("0")
varPannerdoublepattyburger.set("0")
varVegburger.set("0")
varPannerwrap.set("0")
varaloowrap.set("0")
varcheesecorndelightsandwich.set("0")
varchickentandoorisandwich.set("0")
varveggrilledsandwich.set("0")
varExtracheesepannersandwich.set("0")
varchocolava.set("0")
varstrawberryicecream.set("0")
varpancakessyrup.set("0")
varchocolateicecream.set("0")
varvanillamilkshake.set("0")
varcoke.set("0")
varsprite.set("0")
varmiranda.set("0")
var7up.set("0")
varhashbrown.set("0")
vargarlicbread.set("0")
varfrenchfriesm.set("0")
varfrenchfriesL.set("0")

vartotal.set("0")
varsgst.set("0")
varcgst.set("0")
#====================================DEFINITIONS=============================================




def iExit():
    global root
    top = Toplevel()
    top.title("Confirm Logout")
    top.geometry("400x100")
    lbl2=Label(top,text="Are you sure you want to Logout?").pack()
    but1 = Button(top, text="Yes", command=exit,bg="orange",fg="white",width=10).place(x=100, y=50)
    but1 = Button(top, text="No", command=top.destroy,bg="orange",fg="white",width=10).place(x=200, y=50)
    root.mainloop()
    top.mainloop()


def Reset():
    varSpicychickendoublepattyburger.set("0")
    varPannerdoublepattyburger.set("0")
    varVegburger.set("0")
    varPannerwrap.set("0")
    varaloowrap.set("0")
    varcheesecorndelightsandwich.set("0")
    varchickentandoorisandwich.set("0")
    varveggrilledsandwich.set("0")
    varExtracheesepannersandwich.set("0")
    varchocolava.set("0")
    varstrawberryicecream.set("0")
    varpancakessyrup.set("0")
    varchocolateicecream.set("0")
    varvanillamilkshake.set("0")
    varcoke.set("0")
    varsprite.set("0")
    varmiranda.set("0")
    var7up.set("0")
    varhashbrown.set("0")
    vargarlicbread.set("0")
    varfrenchfriesm.set("0")
    varfrenchfriesL.set("0")
    vartotal.set("0")
    varsubTotal.set("0")
    varcgst.set("0")
    varsgst.set("0")
    txtSpicychickendoublepattyburger.configure(state=DISABLED)
    txtPannerdoublepattyburger.configure(state=DISABLED)
    txtVegburger.configure(state=DISABLED)
    txtaloowrap.configure(state=DISABLED)
    txtPannerwrap.configure(state=DISABLED)
    txtcheesecorndelightsandwich.configure(state=DISABLED)
    txtchickentandoorisandwich.configure(state=DISABLED)
    txtveggrilledsandwich.configure(state=DISABLED)
    txtExtracheesepannersandwich.configure(state=DISABLED)
    txtchocolava.configure(state=DISABLED)
    txtstrawberryicecream.configure(state=DISABLED)
    txtpancakessyrup.configure(state=DISABLED)
    txtchocolateicecream.configure(state=DISABLED)
    txtvanillamilkshake.configure(state=DISABLED)
    txtcoke.configure(state=DISABLED)
    txtsprite.configure(state=DISABLED)
    txtmiranda.configure(state=DISABLED)
    txt7up.configure(state=DISABLED)
    txthashbrown.configure(state=DISABLED)
    txtgarlicbread.configure(state=DISABLED)
    txtfrenchfriesm.configure(state=DISABLED)
    txtfrenchfriesL.configure(state=DISABLED)
    Spicychickendoublepattyburger.deselect()
    Pannerdoublepattyburger.deselect()
    Pannerwrap.deselect()
    Vegburger.deselect()
    aloowrap.deselect()
    cheesecorndelightsandwich.deselect()
    chickentandoorisandwich.deselect()
    veggrilledsandwich.deselect()
    Extracheesepannersandwich.deselect()
    chocolava.deselect()
    strawberryicecream.deselect()
    chocolateicecream.deselect()
    pancakessyrup.deselect()
    vanillamilkshake.deselect()
    coke.deselect()
    sprite.deselect()
    miranda.deselect()
    sevenup.deselect()
    hashbrown.deselect()
    garlicbread.deselect()
    frenchfriesm.deselect()
    frenchfriesL.deselect()




def chkSpicychicken():
    if var1.get() == 1:
        txtSpicychickendoublepattyburger.configure(state=NORMAL)
    elif var1.get() == 0:
        txtSpicychickendoublepattyburger.configure(state=DISABLED)

def chkPaneerDoublePatty():
    if var2.get() == 1:
        txtPannerdoublepattyburger.configure(state=NORMAL)
    elif var2.get()==0:
        txtPannerdoublepattyburger.configure(state=DISABLED)

def chkVegBurger():
    if var3.get() == 1:
        txtVegburger.configure(state=NORMAL)
    elif var3.get() == 0:
        txtVegburger.configure(state=DISABLED)

def chkPaneerwrap():
    if var4.get() == 1:
        txtPannerwrap.configure(state=NORMAL)
    elif var4.get() == 0:
        txtPannerwrap.configure(state=DISABLED)

def chkaloowrap():
    if var5.get() == 1:
        txtaloowrap.configure(state=NORMAL)
    elif var5.get() == 0:
        txtaloowrap.configure(state=DISABLED)

def chkcheesecorn():
    if var6.get() == 1:
        txtcheesecorndelightsandwich.configure(state=NORMAL)
    elif var6.get() == 0:
        txtcheesecorndelightsandwich.configure(state=DISABLED)

def chkchickentandoori():
    if var7.get() == 1:
        txtchickentandoorisandwich.configure(state=NORMAL)
    elif var7.get() == 0:
        txtchickentandoorisandwich.configure(state=DISABLED)

def chkveggrilled():
    if var8.get() == 1:
        txtveggrilledsandwich.configure(state=NORMAL)
    elif var8.get() == 0:
        txtveggrilledsandwich.configure(state=DISABLED)

def chkExtracheese():
    if var9.get() == 1:
        txtExtracheesepannersandwich.configure(state=NORMAL)
    elif var9.get() == 0:
        txtExtracheesepannersandwich.configure(state=DISABLED)

def chkchocolava():
    if var10.get() == 1:
        txtchocolava.configure(state=NORMAL)
    elif var10.get() == 0:
        txtchocolava.configure(state=DISABLED)

def chkstrawberry():
    if var11.get() == 1:
        txtstrawberryicecream.configure(state=NORMAL)
    elif var11.get() == 0:
        txtstrawberryicecream.configure(state=DISABLED)

def chkpancakes():
    if var12.get() == 1:
        txtpancakessyrup.configure(state=NORMAL)
    elif var12.get() == 0:
        txtpancakessyrup.configure(state=DISABLED)

def chkchocolate():
    if var13.get() == 1:
        txtchocolateicecream.configure(state=NORMAL)
    elif var13.get() == 0:
        txtchocolateicecream.configure(state=DISABLED)

def chkvanilla():
    if var14.get() == 1:
        txtvanillamilkshake.configure(state=NORMAL)
    elif var14.get() == 0:
        txtvanillamilkshake.configure(state=DISABLED)


def chkcoke():
    if var15.get() == 1:
        txtcoke.configure(state=NORMAL)
    elif var15.get() == 0:
        txtcoke.configure(state=DISABLED)

def chksprite():
    if var16.get() == 1:
        txtsprite.configure(state=NORMAL)
    elif var16.get() == 0:
        txtsprite.configure(state=DISABLED)

def chkmiranda():
    if var17.get() == 1:
        txtmiranda.configure(state=NORMAL)
    elif var17.get() == 0:
        txtmiranda.configure(state=DISABLED)

def chk7up():
    if var18.get() == 1:
        txt7up.configure(state=NORMAL)
    elif var18.get() == 0:
        txt7up.configure(state=DISABLED)

def chkhashbrown():
    if var19.get() == 1:
        txthashbrown.configure(state=NORMAL)
    elif var19.get() == 0:
        txt7up.configure(state=DISABLED)

def chkgarlicbread():
    if var20.get() == 1:
        txtgarlicbread.configure(state=NORMAL)
    elif var20.get() == 0:
        txt7up.configure(state=DISABLED)

def chkfriesm():
    if var21.get() == 1:
        txtfrenchfriesm.configure(state=NORMAL)
    elif var21.get() == 0:
        txt7up.configure(state=DISABLED)

def chkfriesl():
    if var22.get() == 1:
        txtfrenchfriesL.configure(state=NORMAL)
    elif var22.get() == 0:
        txtfrenchfriesL.configure(state=DISABLED)

def total():
    global meal1,meal2,meal3,meal4,meal5,meal6,meal7,meal8,meal9,meal10,meal11,meal12,meal13,meal14,meal15,meal16,meal17,meal18,meal19,meal20,meal21,meal22,total2
    meal1 = float(varSpicychickendoublepattyburger.get())
    meal2 = float(varPannerdoublepattyburger.get())
    meal3 = float(varVegburger.get())
    meal4 = float(varPannerwrap.get())
    meal5 = float(varaloowrap.get())
    meal6 = float(varcheesecorndelightsandwich.get())
    meal7= float(varchickentandoorisandwich.get())
    meal8 =  float(varveggrilledsandwich.get())
    meal9 =  float(varExtracheesepannersandwich.get())
    meal10 = float(varchocolava.get())
    meal11 = float(varstrawberryicecream.get())
    meal12 = float(varpancakessyrup.get())
    meal13 = float(varchocolateicecream.get())
    meal14 = float(varvanillamilkshake.get())
    meal15 = float(varcoke.get())
    meal16 = float(varsprite.get())
    meal17 = float(varmiranda.get())
    meal18 = float(var7up.get())
    meal19 = float(varhashbrown.get())
    meal20 = float(vargarlicbread.get())
    meal21 = float(varfrenchfriesm.get())
    meal22 = float(varfrenchfriesL.get())
    subTotal=((meal1*250)+(meal2*246)+(meal3*160)+(meal4*125)+(meal5*100)+(meal6*250)+(meal7*270)+(meal8*220)+(meal9*280)+(meal10*80)+(meal11*90)+(meal12*110)+(meal13*100)+(meal14*92)+(meal15*82)+(meal16*85)+(meal17*73)+(meal18*73)+(meal19*55)+(meal20*65)+(meal21*75)+(meal22*90))
    a=str(subTotal)
    varsubTotal.set(a)
    cgst = (subTotal * 9 / 100)
    sgst = (subTotal * 9 / 100)
    varcgst.set(cgst)
    varsgst.set(sgst)
    total2 = cgst + sgst + subTotal
    vartotal.set(total2)




def orderpage():
    top2 = Toplevel()
    top2.title("Place order")
    top2.geometry("800x700")
    #lblordersummary=Label(top2,text="Order Summary",font=('Trajan Pro', 18, 'bold'), relief="groove",
          #fg="white",
          #bg="orange").place(x=0,y=0)
    wrapper1 = LabelFrame(top2, text="Order Summary:", font=("arial", 11, 'italic'))
    wrapper2 = LabelFrame(top2, text="Select Payment Method:", font=("arial", 13, 'italic'))
    wrapper1.pack(fill="both", expand='yes', padx=20, pady=10)
    wrapper2.pack(fill="both", expand='yes', padx=20, pady=10)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("rockwell", 15, "bold"), fg="blue")

    trv = ttk.Treeview(wrapper1, columns=(1, 2, 3), show="headings", height=15)
    trv.pack()
    trv.heading(1, text="Item Name:")
    trv.heading(2, text="Price:")
    trv.heading(3, text="Quantity:")

    #Label(top2, text="ITEM NAME").place(x=0, y=40)
    #Label(top2,text="PRICE").place(x=260,y=40)
    #Label(top2, text="QTY").place(x=295, y=40)

    def ok():
        connectiondb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset='utf8',
                                               database="efooddelivery")
        cursordb = connectiondb.cursor(buffered=True)

        # fetch current login cid
        cid_sql = "select cid from login"
        cursordb.execute(cid_sql)
        cid_result = cursordb.fetchone()
        cid_fetched = cid_result[0]
        print('......fetch cid stored.....', cid_fetched)

        # fetch cvv stored in customer record
        # cvv_sql = "select cvv from customer where cid = 1"
        # cursordb.execute(cvv_sql)
        cvv_sql = "select cvv from customer where cid = %s"
        cursordb.execute(cvv_sql, [(cid_fetched)])
        cvv_result = cursordb.fetchone()
        cvv_stored = cvv_result[0]
        print('......fetch cvv stored.....', cvv_stored)

        global varcvv, var30
        print('.......entered cvv....', varcvv.get())
        if len(varcvv.get()) > 3:
            messagebox.showinfo('Information', 'CVV should be 3 digits')
            return
        elif len(varcvv.get()) == 3 and str(cvv_stored) != varcvv.get():
            print('inside not cvv comparison')
            messagebox.showinfo('Information', 'CVV entered is not correct. Please check and enter again !')
            return
        d = str(date.today())
        dt = d.split("-")
        a, b, c = dt
        e = c + "-" + b + "-" + a
        print(e)

        if var1.get() == 1:
            orderline1_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                            VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'Spicy chickendoublepatty burger', '250', str(meal1), str(250 * (meal1)), e,
                      datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline1_insert_query, record)
            connectiondb.commit()
            varSpicychickendoublepattyburger.set("0")
            txtSpicychickendoublepattyburger.configure(state=DISABLED)
            Spicychickendoublepattyburger.deselect()



        if var2.get() == 1:
            orderline2_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'Panner double patty burger', '246', str(meal2), str(246 * (meal2)), e,
                      datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline2_insert_query, record)
            connectiondb.commit()
            varPannerdoublepattyburger.set("0")
            txtPannerdoublepattyburger.configure(state=DISABLED)
            Pannerdoublepattyburger.deselect()

        if var3.get() == 1:
            orderline3_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'Veg burger', '160', str(meal3), str(160 * (meal3)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline3_insert_query, record)
            connectiondb.commit()
            varVegburger.set("0")
            txtVegburger.configure(state=DISABLED)
            Vegburger.deselect()

        if var4.get() == 1:
            orderline4_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'Panner wrap', '125', str(meal4), str(125 * (meal4)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline4_insert_query, record)
            connectiondb.commit()
            varPannerwrap.set("0")
            txtPannerwrap.configure(state=DISABLED)
            Pannerwrap.deselect()

        if var5.get() == 1:
            orderline5_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'aloo wrap', '100', str(meal5), str(100 * (meal5)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline5_insert_query, record)
            connectiondb.commit()
            varaloowrap.set("0")
            txtaloowrap.configure(state=DISABLED)
            aloowrap.deselect()

        if var6.get() == 1:
            orderline6_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'cheese corn delight sandwich', '250', str(meal6), str(250 * (meal6)), e,
                      datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline6_insert_query, record)
            connectiondb.commit()
            varcheesecorndelightsandwich.set("0")
            txtcheesecorndelightsandwich.configure(state=DISABLED)
            cheesecorndelightsandwich.deselect()

        if var7.get() == 1:
            orderline7_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'chicken tandoori sandwich', '270', str(meal7), str(270 * (meal7)), e,
                      datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline7_insert_query, record)
            connectiondb.commit()
            varchickentandoorisandwich.set("0")
            txtchickentandoorisandwich.configure(state=DISABLED)
            chickentandoorisandwich.deselect()
        if var8.get() == 1:
            orderline8_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'veg grilled sandwich ', '220', str(meal8), str(220 * (meal8)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline8_insert_query, record)
            connectiondb.commit()
            varveggrilledsandwich.set("0")
            txtveggrilledsandwich.configure(state=DISABLED)
            veggrilledsandwich.deselect()
        if var9.get() == 1:
            orderline9_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'Extra cheese panner sandwich', '280', str(meal9), str(280 * (meal9)), e,
                      datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline9_insert_query, record)
            connectiondb.commit()
            varExtracheesepannersandwich.set("0")
            txtExtracheesepannersandwich.configure(state=DISABLED)
            Extracheesepannersandwich.deselect()
        if var10.get() == 1:
            orderline10_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'choco lava', '250', str(meal10), str(80 * (meal10)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline10_insert_query, record)
            connectiondb.commit()
            varchocolava.set("0")
            txtchocolava.configure(state=DISABLED)
            chocolava.deselect()
        if var11.get() == 1:
            orderline11_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'strawberry icecream', '90', str(meal11), str(90 * (meal11)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline11_insert_query, record)
            connectiondb.commit()
            varstrawberryicecream.set("0")
            txtstrawberryicecream.configure(state=DISABLED)
            strawberryicecream.deselect()
        if var12.get() == 1:
            orderline12_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'pancakes &syrup', '110', str(meal12), str(110 * (meal12)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline12_insert_query, record)
            connectiondb.commit()
            varpancakessyrup.set("0")
            txtpancakessyrup.configure(state=DISABLED)
            pancakessyrup.deselect()
        if var13.get() == 1:
            orderline13_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'chocolate icecream', '100', str(meal13), str(100 * (meal13)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline13_insert_query, record)
            connectiondb.commit()
            varchocolateicecream.set("0")
            txtchocolateicecream.configure(state=DISABLED)
            chocolateicecream.deselect()
        if var14.get() == 1:
            orderline14_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'vanilla milkshake', '60', str(meal14), str(60 * (meal14)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline14_insert_query, record)
            connectiondb.commit()
            varvanillamilkshake.set("0")
            txtvanillamilkshake.configure(state=DISABLED)
            vanillamilkshake.deselect()

        if var15.get() == 1:
            orderline15_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'coke', '92', str(meal15), str(92 * (meal15)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline15_insert_query, record)
            connectiondb.commit()
            varcoke.set("0")
            txtcoke.configure(state=DISABLED)
            coke.deselect()

        if var16.get() == 1:
            orderline16_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'sprite', '82', str(meal16), str(82 * (meal16)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline16_insert_query, record)
            connectiondb.commit()
            varsprite.set("0")
            txtsprite.configure(state=DISABLED)
            sprite.deselect()
        if var17.get() == 1:
            orderline17_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'miranda', '85', str(meal17), str(85 * (meal17)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline17_insert_query, record)
            connectiondb.commit()
            varmiranda.set("0")
            txtmiranda.configure(state=DISABLED)
            miranda.deselect()
        if var18.get() == 1:
            orderline18_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, '7up', '73', str(meal18), str(73 * (meal18)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline18_insert_query, record)
            connectiondb.commit()
            var7up.set("0")
            txt7up.configure(state=DISABLED)
            sevenup.deselect()
        if var19.get() == 1:
            orderline19_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (cid, 'hash brown', '55', str(meal19), str(55 * (meal19)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline19_insert_query, record)
            connectiondb.commit()
            varhashbrown.set("0")
            txthashbrown.configure(state=DISABLED)
            hashbrown.deselect()
        if var20.get() == 1:
            orderline20_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'garlic bread', '65', str(meal20), str(65 * (meal20)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline20_insert_query, record)
            connectiondb.commit()
            vargarlicbread.set("0")
            txtgarlicbread.configure(state=DISABLED)
            garlicbread.deselect()

        if var21.get() == 1:
            orderline21_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'french fries(m)', '75', str(meal21), str(75 * (meal21)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline21_insert_query, record)
            connectiondb.commit()
            varfrenchfriesm.set("0")
            txtfrenchfriesm.configure(state=DISABLED)
            frenchfriesm.deselect()
        if var22.get() == 1:
            orderline22_insert_query = """INSERT INTO Order_History (cid, itemname, price, quantity, amount, date,time) 
                                                    VALUES (%s, %s, %s, %s, %s, %s,%s) """

            record = (
            cid, 'french fries(L)', '90', str(meal22), str(90 * (meal22)), e, datetime.now().strftime("%H:%M:%S"))
            cursordb.execute(orderline22_insert_query, record)
            connectiondb.commit()
            varfrenchfriesL.set("0")
            txtfrenchfriesL.configure(state=DISABLED)
            frenchfriesL.deselect()

        vartotal.set("0")
        varsubTotal.set("0")
        varcgst.set("0")
        varsgst.set("0")
        messagebox.showinfo("Ordered confirmed", "Thank you for ordering in Yummy corner! Visit us again! ")
        top2.destroy()


    def sel():
        if var30.get()== 2:
            Label(wrapper2, text="Enter your cvv:", fg="black", font=('Trajan Pro', 12, 'bold')).place(x=100,y=80)
            cvv = Entry(wrapper2, textvariable=varcvv, font=('arial', 12, 'bold'), width=6, justify='left')
            cvv.place(x=100, y=100)

        print(var30.get())

    R1 = Radiobutton(wrapper2, text="Cash", variable=var30, value=1, command=sel)
    R1.place(x=100, y=30)

    R2 = Radiobutton(wrapper2, text="Credit Card", variable=var30, value=2, command=sel)
    R2.place(x=100, y=60)

    order=[]
    a = 1

    if var1.get()== 1:
        order.append(["Spicy Chicken Double Patty Burger",250,txtSpicychickendoublepattyburger.get()])

    if var2.get() == 1:
        order.append(["Paneer Double patty burger", 246, txtPannerdoublepattyburger.get()])

    if var3.get() == 1:
        order.append(["Veg Burger", 160, txtVegburger.get()])

    if var4.get() == 1:
        order.append(["Paneer wrap", 125, txtPannerwrap.get()])

    if var5.get() == 1:
        order.append(["aloo wrap", 100, txtaloowrap.get()])

    if var6.get() == 1:
        order.append(["cheese corn delight sandwich", 250, txtcheesecorndelightsandwich.get()])

    if var7.get() == 1:
        order.append(["chicken tandoori sandwich", 270, txtchickentandoorisandwich.get()])

    if var8.get() == 1:
        order.append(["veg grilled sandwich", 220, txtveggrilledsandwich.get()])

    if var9.get() == 1:
        order.append(["Extra cheese paneer sandwich", 280, txtExtracheesepannersandwich.get()])

    if var10.get() == 1:
        order.append(["choco lava", 80, txtchocolava.get()])

    if var11.get()== 1:
        order.append(["strawberry icecream",90,txtstrawberryicecream.get()])

    if var12.get() == 1:
        order.append(["pancakes & syrup", 110, txtpancakessyrup.get()])

    if var13.get() == 1:
        order.append(["chocolate icecream", 100, txtchocolateicecream.get()])

    if var14.get() == 1:
        order.append(["vanilla milkshake", 60, txtvanillamilkshake.get()])

    if var15.get() == 1:
        order.append(["coke", 92, txtcoke.get()])

    if var16.get() == 1:
        order.append(["sprite", 82, txtsprite.get()])

    if var17.get() == 1:
        order.append(["miranda", 85, txtmiranda.get()])

    if var18.get() == 1:
        order.append(["7up", 73, txt7up.get()])

    if var19.get() == 1:
        order.append(["hash brown", 55, txthashbrown.get()])

    if var20.get() == 1:
        order.append(["garlic bread", 65, txtgarlicbread.get()])

    if var21.get() == 1:
        order.append(["french fries(m)", 75, txtfrenchfriesm.get()])

    if var22.get() == 1:
        order.append(["french fries(L)", 90, txtfrenchfriesL.get()])

    for i in range(len(order)):
        col1 = order[i][0]
        col2 = order[i][1]
        col3 = order[i][2]
        trv.insert("", "end", values=(col1, col2,col3))



    myButton10 = Button(wrapper2, text="Confirm Order", height=2, width=18, command=ok,font=('Trajan Pro',14,'bold'),bg="orange",fg="white")
    myButton10.place(x=450,y=40)


    top2.mainloop()


def only_numbers(char):
    if char.isdigit():
        return TRUE
    elif char == "":
        return TRUE
    else:
        messagebox.showinfo('Information', 'Only digits are allowed')
        return False








    #================================================FRAME 1===============================

lblBurgersWraps=Label(topsleft2,font=('Verdana',18,'bold'),text='Burgers & Wraps',fg="goldenrod")
lblBurgersWraps.place(x=180,y=9)

Spicychickendoublepattyburger=Checkbutton(topsleft2,text="Spicy chicken double patty burger\t₹250",variable=var1,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkSpicychicken)
Spicychickendoublepattyburger.place(x=1,y=60)

txtSpicychickendoublepattyburger=Entry(topsleft2,textvariable=varSpicychickendoublepattyburger,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtSpicychickendoublepattyburger.place(x=410,y=64)

valid_postalcode = root.register(only_numbers)
txtSpicychickendoublepattyburger.config(validate="key",validatecommand=(valid_postalcode, '%P'))


Pannerdoublepattyburger=Checkbutton(topsleft2,text="Paneer double patty burger\t\t₹246",variable=var2,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkPaneerDoublePatty)
Pannerdoublepattyburger.place(x=1,y=100)
txtPannerdoublepattyburger=Entry(topsleft2,textvariable=varPannerdoublepattyburger,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtPannerdoublepattyburger.place(x=410,y=104)

valid_postalcode = root.register(only_numbers)
txtPannerdoublepattyburger.config(validate="key",validatecommand=(valid_postalcode, '%P'))


Vegburger=Checkbutton(topsleft2,text="Veg burger\t\t\t₹160",variable=var3,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkVegBurger)
Vegburger.place(x=1,y=140)
txtVegburger=Entry(topsleft2,textvariable=varVegburger,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtVegburger.place(x=410,y=144)

valid_postalcode =root.register(only_numbers)
txtVegburger.config(validate="key",validatecommand=(valid_postalcode, '%P'))


Pannerwrap=Checkbutton(topsleft2,text="Panner wrap\t\t\t₹125",variable=var4,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkPaneerwrap)
Pannerwrap.place(x=1,y=180)
txtPannerwrap=Entry(topsleft2,textvariable=varPannerwrap,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtPannerwrap.place(x=410,y=184)

valid_postalcode = root.register(only_numbers)
txtPannerwrap.config(validate="key",validatecommand=(valid_postalcode, '%P'))


aloowrap=Checkbutton(topsleft2,text="aloo wrap\t\t\t₹100",variable=var5,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkaloowrap)
aloowrap.place(x=1,y=220)
txtaloowrap=Entry(topsleft2,textvariable=varaloowrap,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtaloowrap.place(x=410,y=224)

valid_postalcode = root.register(only_numbers)
txtaloowrap.config(validate="key",validatecommand=(valid_postalcode, '%P'))
#=========================================FRAME 2=====================================================================


lblSandwich=Label(root,font=('Verdana',18,'bold'),text='Sandwich',fg="goldenrod")
lblSandwich.place(x=200,y=410)

cheesecorndelightsandwich=Checkbutton(root,text="cheese corn delight sandwich\t₹250",variable=var6,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkcheesecorn)
cheesecorndelightsandwich.place(x=1,y=461)
txtcheesecorndelightsandwich=Entry(root,textvariable=varcheesecorndelightsandwich,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtcheesecorndelightsandwich.place(x=410,y=461)

valid_postalcode = root.register(only_numbers)
txtcheesecorndelightsandwich.config(validate="key",validatecommand=(valid_postalcode, '%P'))

chickentandoorisandwich=Checkbutton(root,text="chicken tandoori sandwich\t\t₹270",variable=var7,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkchickentandoori)
chickentandoorisandwich.place(x=1,y=511)
txtchickentandoorisandwich=Entry(root,textvariable=varchickentandoorisandwich,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtchickentandoorisandwich.place(x=410,y=511)

valid_postalcode = root.register(only_numbers)
txtchickentandoorisandwich.config(validate="key",validatecommand=(valid_postalcode, '%P'))

veggrilledsandwich=Checkbutton(root,text="veg grilled sandwich\t\t₹220",variable=var8,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkveggrilled)
veggrilledsandwich.place(x=1,y=561)
txtveggrilledsandwich=Entry(root,textvariable=varveggrilledsandwich,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtveggrilledsandwich.place(x=410,y=561)

valid_postalcode = root.register(only_numbers)
txtveggrilledsandwich.config(validate="key",validatecommand=(valid_postalcode, '%P'))




Extracheesepannersandwich=Checkbutton(root,text="Extra cheese paneer sandwich\t₹280",variable=var9,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkExtracheese)
Extracheesepannersandwich.place(x=1,y=611)
txtExtracheesepannersandwich=Entry(root,textvariable=varExtracheesepannersandwich,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtExtracheesepannersandwich.place(x=410,y=611)


valid_postalcode = root.register(only_numbers)
txtExtracheesepannersandwich.config(validate="key",validatecommand=(valid_postalcode, '%P'))


#=========================================FRAME 3=====================================================================

lblDesserts=Label(root,font=('Verdana',18,'bold'),text='Desserts',fg="goldenrod")
lblDesserts.place(x=200,y=710)

chocolava=Checkbutton(root,text="choco lava\t\t₹80",variable=var10,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkchocolava)
chocolava.place(x=1,y=770)
txtchocolava=Entry(root,textvariable=varchocolava,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtchocolava.place(x=410,y=770)

valid_postalcode = root.register(only_numbers)
txtchocolava.config(validate="key",validatecommand=(valid_postalcode, '%P'))

strawberryicecream=Checkbutton(root,text="strawberry icecream\t₹90",variable=var11,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkstrawberry)
strawberryicecream.place(x=1,y=820)
txtstrawberryicecream=Entry(root,textvariable=varstrawberryicecream,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtstrawberryicecream.place(x=410,y=820)

valid_postalcode = root.register(only_numbers)
txtstrawberryicecream.config(validate="key",validatecommand=(valid_postalcode, '%P'))


pancakessyrup=Checkbutton(root,text="pancakes & syrup\t\t₹110",variable=var12,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkpancakes)
pancakessyrup.place(x=1,y=870)
txtpancakessyrup=Entry(root,textvariable=varpancakessyrup,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtpancakessyrup.place(x=410,y=870)

valid_postalcode = root.register(only_numbers)
txtpancakessyrup.config(validate="key",validatecommand=(valid_postalcode, '%P'))



chocolateicecream=Checkbutton(root,text="chocolate icecream\t₹100",variable=var13,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkchocolate)
chocolateicecream.place(x=1,y=920)
txtchocolateicecream=Entry(root,textvariable=varchocolateicecream,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtchocolateicecream.place(x=410,y=920)

valid_postalcode = root.register(only_numbers)
txtchocolateicecream.config(validate="key",validatecommand=(valid_postalcode, '%P'))

vanillamilkshake=Checkbutton(root,text="vanilla milkshake\t\t₹60",variable=var14,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkvanilla)
vanillamilkshake.place(x=1,y=970)
txtvanillamilkshake=Entry(root,textvariable=varvanillamilkshake,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtvanillamilkshake.place(x=410,y=970)

valid_postalcode = root.register(only_numbers)
txtvanillamilkshake.config(validate="key",validatecommand=(valid_postalcode, '%P'))




#=========================================FRAME 4=====================================================================




lblDrinks=Label(root,font=('Verdana',18,'bold'),text='Drinks',fg="goldenrod")
lblDrinks.place(x=810,y=50)

coke=Checkbutton(root,text="coke\t\t₹92",variable=var15,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkcoke)
coke.place(x=611,y=120)
txtcoke=Entry(root,textvariable=varcoke,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtcoke.place(x=950,y=124)

valid_postalcode = root.register(only_numbers)
txtcoke.config(validate="key",validatecommand=(valid_postalcode, '%P'))

sprite=Checkbutton(root,text="sprite\t\t₹82",variable=var16,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chksprite)
sprite.place(x=611,y=170)
txtsprite=Entry(root,textvariable=varsprite,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtsprite.place(x=950,y=174)

valid_postalcode = root.register(only_numbers)
txtsprite.config(validate="key",validatecommand=(valid_postalcode, '%P'))

miranda=Checkbutton(root,text="miranda\t\t₹85",variable=var17,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkmiranda)
miranda.place(x=611,y=220)
txtmiranda=Entry(root,textvariable=varmiranda,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtmiranda.place(x=950,y=224)

valid_postalcode = root.register(only_numbers)
txtmiranda.config(validate="key",validatecommand=(valid_postalcode, '%P'))


sevenup=Checkbutton(root,text="7 up\t\t₹73",variable=var18,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chk7up)
sevenup.place(x=611,y=270)
txt7up=Entry(root,textvariable=var7up,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txt7up.place(x=950,y=274)

valid_postalcode = root.register(only_numbers)
txt7up.config(validate="key",validatecommand=(valid_postalcode, '%P'))





#=========================================FRAME 5=====================================================================




lblSides=Label(root,font=('Verdana',18,'bold'),text='Sides',fg="goldenrod")
lblSides.place(x=1420,y=50)

hashbrown=Checkbutton(root,text="hash brown\t\t₹55",variable=var19,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkhashbrown)
hashbrown.place(x=1221,y=120)
txthashbrown=Entry(root,textvariable=varhashbrown,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txthashbrown.place(x=1580,y=124)

valid_postalcode = root.register(only_numbers)
txthashbrown.config(validate="key",validatecommand=(valid_postalcode, '%P'))

garlicbread=Checkbutton(root,text="garlic bread\t\t₹65",variable=var20,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkgarlicbread)
garlicbread.place(x=1221,y=170)
txtgarlicbread=Entry(root,textvariable=vargarlicbread,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtgarlicbread.place(x=1580,y=174)

valid_postalcode = root.register(only_numbers)
txtgarlicbread.config(validate="key",validatecommand=(valid_postalcode, '%P'))


frenchfriesm=Checkbutton(root,text="french fries(m)\t\t₹75",variable=var21,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkfriesm)
frenchfriesm.place(x=1221,y=220)
txtfrenchfriesm=Entry(root,textvariable=varfrenchfriesm,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtfrenchfriesm.place(x=1580,y=224)

valid_postalcode = root.register(only_numbers)
txtfrenchfriesm.config(validate="key",validatecommand=(valid_postalcode, '%P'))


frenchfriesL=Checkbutton(root,text="french fries(L)\t\t₹90",variable=var22,onvalue=1,offvalue=0,font=('arial',12,'bold'),command=chkfriesl)
frenchfriesL.place(x=1221,y=270)
txtfrenchfriesL=Entry(root,textvariable=varfrenchfriesL,font=('arial',12,'bold'),width=6,justify='left',state=DISABLED)
txtfrenchfriesL.place(x=1580,y=274)

valid_postalcode = root.register(only_numbers)
txtfrenchfriesL.config(validate="key",validatecommand=(valid_postalcode, '%P'))

#=========================================FRAME 6=====================================================================


lblSubTotal=Label(root,text="Sub Total:",font=('trajan pro ',30,'bold')).place(x=1210,y=500)
txtsubTotal=Entry(root,state=DISABLED,width=8,textvariable=varsubTotal,font=('trajan pro ',20,'bold'))
txtsubTotal.place(x=1450,y=510)

lblcgst=Label(root,text="CGST:",font=('trajan pro ',30,'bold')).place(x=1210,y=600)
txtcgst = Entry(root, state=DISABLED,width=8,textvariable=varcgst,font=('trajan pro ',20,'bold'))
txtcgst.place(x=1450, y=610)

lblsgst=Label(root,text="SGST:",font=('trajan pro ',30,'bold')).place(x=1210,y=700)
txtsgst = Entry(root, state=DISABLED,width=8,textvariable=varsgst,font=('trajan pro ',20,'bold'))
txtsgst.place(x=1450, y=710)


lbltotal=Label(root,text="Total:",font=('trajan pro ',30,'bold')).place(x=1210,y=800)
txttotal = Entry(root, state=DISABLED,width=8,textvariable=vartotal,font=('trajan pro ',20,'bold'))
txttotal.place(x=1450, y=810)





















#===========================BUTTONS============================
myButton=Button(root,text="Place Order",height=2,width=20,command=orderpage,font=('Trajan Pro',15,'bold'),bg="orange",fg="white")
myButton.place(x=1200,y=870)

myButton2=Button(root,text="Order History",height=2,width=20,command=lambda:os.system('order_history.py'),font=('Trajan Pro',15,'bold'),bg="orange",fg="white")
myButton2.place(x=610,y=750)

myButton4=Button(root,text="Reset",height=2,width=20,font=('Trajan Pro',15,'bold'),bg="orange",fg="white",command=Reset)
myButton4.place(x=610,y=620)



myButton3=Button(root,text="Logout",height=2,width=20,font=('Trajan Pro',15,'bold'),bg="orange",fg="white",command=iExit)
myButton3.place(x=610,y=880)

myButton3=Button(root,text="Check Total",height=2,width=20,font=('Trajan Pro',15,'bold'),bg="orange",fg="white",command=total)
myButton3.place(x=610,y=490)

root.mainloop()
