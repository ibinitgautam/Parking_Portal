from email import message
import tkinter as root
from tkinter.font import BOLD
import mysql.connector as sq
import time
import turtle as tr
import random
from twilio.rest import Client
import keys
import keysII


def exit():
    root.Tk().quit()


def graphics():
    t = tr.Turtle()

    tr.title("Parking Plot")
    tr.bgcolor("red")


    t.penup()
    t.goto(350, 100)
    t.pendown()

    #parking 1-5
    for i in range(6):
        t.rt(90)
        t.fd(100)
        t.lt(-90)
        t.bk(-100)

        t.bk(-100)
        t.lt(-90)
        t.fd(100)
        t.rt(90)

        t.stamp()
        t.fd(100)

    t.fd(500)
    t.stamp()
    t.fd(100)

    t.penup()
    t.goto(350, -150)
    t.pendown()
    t.bk(70)
    t.lt(90)
    t.fd(90)


    time.sleep(6)

    #parking 1-5
    for i in range(5):
        t.rt(90)
        t.fd(100)
        t.lt(-90)
        t.bk(-100)

        t.bk(-100)
        t.lt(-90)
        t.fd(100)
        t.rt(90)

        t.stamp()
        t.fd(100)

    t.fd(400)
    t.stamp()
    t.fd(100)


    t.penup()
    t.goto(300, -150)
    t.pendown()
    t.bk(70)
    t.lt(90)
    t.fd(90)

    time.sleep(6)


def details():
    global vehicle_number, vehicle_type, owner_name, phone
    vehicle_number = vehicle_number.get()
    vehicle_type = vehicle_type.get()
    owner_name = owner_name.get()
    phone = phone.get()
    
    if(len(phone) != 10):
        phone_mismatch()        
    else:
        otp()

def login_check():
    global veh, login_phone

    veh = veh.get()
    login_phone = login_phone.get()

    mydb = sq.connect(
        host = "localhost",
        user = "root",
        passwd = "root"
    )
    cur = mydb.cursor()
    cur.execute("use park;")
    cur.execute("select * from parking;")

    #check
    for vehicle in cur:
        if (veh == vehicle[0]):
            repay()
            break;
    else:
        error()
    
def repay():
    window_repay = root.Tk()
    window_repay.geometry("380x300")
    window_repay.title("Payment")

    root.Label(window_repay, text = "Extending Your Parking, Choose Your Payment Option.", font = ("AgencyFB", 12), fg = "grey").pack()
    root.Label(window_repay, text = "NOTE --> Charges: 3000/- per day.", font = ("AgencyFB", 8), fg = "red").pack()
    
    button_upi = root.Button(window_repay, text="   UPI   ", relief="groove", command=reupi)
    button_upi.place(x = 70, y = 100)

    button_card = root.Button(window_repay, text="  Debit Card  ", relief="groove", command=redebit)
    button_card.place(x = 150, y = 100)

    cancel = root.Button(window_repay, text = "  Cancel  ", relief="groove", command = window_repay.destroy)
    cancel.place(x = 200, y = 200)

def update_entry():
    global p, login_phone
    #print(login_phone)
    
    mydb = sq.connect(
        host = "localhost",
        user = "root",
        passwd = "root"
    )
    cur = mydb.cursor()
    cur.execute("use park;")
    cur.execute("select Payment from payment;")

    for pay in cur:
        p = pay[0] + 3000
        break;
    #print(p)
    
    q = "update payment set Time = %s, Payment = %s where Phone = %s;"
    val = (time.strftime("%H:%M:%S"), p, login_phone)
    cur.execute(q, val)
    mydb.commit()
    
    confirmationII()


def reupi():
    window_reupi = root.Tk()
    window_reupi.geometry("300x200")
    window_reupi.title("Payment Through UPI")
    root.Label(window_reupi, text="  UPI  ", fg = "grey", font = ("Myriad", 18, "bold", "italic")).place(x = 100, y = 30)
    id_upi = root.Entry(window_reupi, width = 24)
    id_upi.place(x = 50, y = 80)

    button_upi = root.Button(window_reupi, text = "    PAY    ", relief = "groove", command = update_entry)
    button_upi.place(x = 100, y = 120)  


def debit():
    window_debit = root.Tk()
    window_debit.geometry("340x250")
    window_debit.title("Payment Through Debit Card")

    debit_label = root.Label(window_debit, text="Enter Your Details Here", fg = "blue", font = ("AgencyFB", 12, "bold"))
    debit_label.place(x = 100, y = 20)
    
    debit_cardNum = root.Label(window_debit, text = "Card Number ", font = ("Arial", 8, "bold"))
    debit_cardNum.place(x = 20, y = 50)
    cardNum = root.Entry(window_debit, width=18)
    cardNum.place(x = 130, y = 50)
    
    debit_cardCVV = root.Label(window_debit, text = "CVV", font = ("Arial", 8, "bold"))
    debit_cardCVV.place(x = 20, y = 80)
    CVV = root.Entry(window_debit, width=18)
    CVV.place(x = 130, y = 80)
    
    debit_card_owner = root.Label(window_debit, text = "Card Owner ", font = ("Arial", 8, "bold"))
    debit_card_owner.place(x = 20, y = 110)
    card_name = root.Entry(window_debit, width=18)
    card_name.place(x = 130, y = 110)
    
    owner_phone = root.Label(window_debit, text = "Phone number", font = ("Arial", 8, "bold"))
    owner_phone.place(x = 20, y = 140)
    card_phone = root.Entry(window_debit, width=18)
    card_phone.place(x = 130, y = 140)
    
    button_pay = root.Button(window_debit,text="  PAY  ",relief="groove" , command = pay_entry)
    button_pay.place(x = 170 , y= 170)

def redebit():
    window_debit = root.Tk()
    window_debit.geometry("340x250")
    window_debit.title("Payment Through Debit Card")

    debit_label = root.Label(window_debit, text="Enter Your Details Here", fg = "blue", font = ("AgencyFB", 12, "bold"))
    debit_label.place(x = 100, y = 20)
    
    debit_cardNum = root.Label(window_debit, text = "Card Number ", font = ("Arial", 8, "bold"))
    debit_cardNum.place(x = 20, y = 50)
    cardNum = root.Entry(window_debit, width=18)
    cardNum.place(x = 130, y = 50)
    
    debit_cardCVV = root.Label(window_debit, text = "CVV", font = ("Arial", 8, "bold"))
    debit_cardCVV.place(x = 20, y = 80)
    CVV = root.Entry(window_debit, width=18)
    CVV.place(x = 130, y = 80)
    
    debit_card_owner = root.Label(window_debit, text = "Card Owner ", font = ("Arial", 8, "bold"))
    debit_card_owner.place(x = 20, y = 110)
    card_name = root.Entry(window_debit, width=18)
    card_name.place(x = 130, y = 110)
    
    owner_phone = root.Label(window_debit, text = "Phone number", font = ("Arial", 8, "bold"))
    owner_phone.place(x = 20, y = 140)
    card_phone = root.Entry(window_debit, width=18)
    card_phone.place(x = 130, y = 140)
    
    button_pay = root.Button(window_debit,text="  PAY  ",relief="groove" , command = update_entry) 
    button_pay.place(x = 170 , y= 170)

def phone_mismatch():
    window_book = root.Tk()
    window_book.geometry("247x100")
    window_book.title("Alert!")
    Lb1 = root.Label(window_book, text="Invalid Phone Number !",
                  font=("arial", 16, "bold"), fg="red").pack()
    lb = root.Label(window_book, text="Please enter a valid phone number",
                 fg="grey", font=("calibri", 8,)).pack()
    but = root.Button(window_book, text="   OK   ", relief="groove",
                   command=window_book.destroy).pack()


def pay():
    window_pay = root.Tk()
    window_pay.geometry("280x250")
    window_pay.title("Payment")

    root.Label(window_pay, text = "Choose Your Payment Option.", font = ("AgencyFB", 12), fg = "grey").pack()
    root.Label(window_pay, text = "NOTE --> Charges: 3000/- per day.", font = ("AgencyFB", 8), fg = "red").pack()
    button_upi = root.Button(window_pay, text="   UPI   ", relief="groove", command=upi)
    button_upi.place(x = 70, y = 100)

    button_card = root.Button(window_pay, text="  Debit Card  ", relief="groove", command=debit)
    button_card.place(x = 150, y = 100)

    cancel = root.Button(window_pay, text = "  Cancel  ", relief="groove", command = window_pay.destroy)
    cancel.place(x = 200, y = 200)


def pay_entry():
    mydb = sq.connect(
    host = "localhost",
    user = "root",
    passwd = "root"
    )
    curr = mydb.cursor()

    curr.execute("use park")
    q = "insert into payment values(%s, %s, %s, %s)"
    val = (owner_name, "3000", phone, time.strftime("%H:%M:%S"))
    curr.execute(q, val)
    mydb.commit()

    entry()
    confirmation()
    #graphics()


def upi():
    window_upi = root.Tk()
    window_upi.geometry("300x200")
    window_upi.title("Payment Through UPI")
    root.Label(window_upi, text="  UPI  ", fg = "grey", font = ("Myriad", 18, "bold", "italic")).place(x = 100, y = 30)
    id_upi = root.Entry(window_upi, width = 24)
    id_upi.place(x = 50, y = 80)

    button_upi = root.Button(window_upi, text = "    PAY    ", relief = "groove", command = pay_entry)
    button_upi.place(x = 100, y = 120)


def book():
    global vehicle_number, vehicle_type, owner_name, phone
    window_book = root.Tk()
    window_book.title("Parking Portal")
    window_book.geometry("280x250")
    root.Label(window_book, text = "Please Enter Details", fg = "blue").pack()

    label_vehicle = root.Label(window_book, text = "Vehicle Number ", font = ("Arial", 8, "bold"))
    label_vehicle.place(x = 20, y = 30)
    vehicle_number = root.Entry(window_book, width=18)
    vehicle_number.place(x = 130, y = 30)
    
    label_vehicle_type = root.Label(window_book, text = "Vehicle Type", font = ("Arial", 8, "bold"))
    label_vehicle_type.place(x = 20, y = 60)
    vehicle_type = root.Entry(window_book, width=18)
    vehicle_type.place(x = 130, y = 60)
    
    label_owner = root.Label(window_book, text = "Owner Name ", font = ("Arial", 8, "bold"))
    label_owner.place(x = 20, y = 90)
    owner_name = root.Entry(window_book, width=18)
    owner_name.place(x = 130, y = 90)
    
    label_phone = root.Label(window_book, text = "Phone number", font = ("Arial", 8, "bold"))
    label_phone.place(x = 20, y = 120)
    phone = root.Entry(window_book, width=18)
    phone.place(x = 130, y = 120)

    button_detail = root.Button(window_book,text="  Submit  ",relief="groove" , command = details) 
    button_detail.place(x = 160 , y= 160)
   

def otp():
    global otp
    otp = random.randint(1000, 9999)
    if(str(phone) == "9015117813"):
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body = "Here is Your OTP: " + str(otp),
            from_ = keys.twilio_number,
            to = "+91" + str(phone)
        )
    elif(str(phone) == "8091161927"):
        client = Client(keys.account_sid, keys.auth_token)
        message = client.messages.create(
            body = "Here is Your OTP: " + str(otp),
            from_ = keys.twilio_number,
            to = "+91" + str(phone)
        )
    print(otp)
    input_otp()
    

def input_otp():
    #Check
    global user_otp    
    window_otp = root.Tk()
    window_otp.geometry("650x130")
    window_otp.title("Parking Portal")
    label_otp = root.Label(window_otp, text = "Please Enter OTP!", font=("Ariel", 16, "bold")).pack()
    label_otp_note = root.Label(window_otp, text = "An OTP has been sent to your number entered. If you have not got OTP then please renter your details! click on 'Go Back' button", font=("calibri", 8))
    label_otp_note.place(x=30, y=30)
    user_otp = root.Entry(window_otp, width=18)
    user_otp.place(x = 120, y = 75)
    
    otp_submit = root.Button(window_otp, text="  Submit  ", relief="groove", font=("Ariel", 10), command= check)
    otp_submit.place(x=300, y=65)
    
    back = root.Button(window_otp, text="  Go Back  ", relief="groove", font=("Ariel", 10), command= blank)
    back.place(x = 400, y = 65)


def check():
    user = user_otp.get()
    if(user == otp):
        window_error = root.Tk()
        window_error.geometry("450x100")
        window_error.title("Alert!")
        label_error = root.Label(window_error, text="OTP you entered is INCORRECT! Try Again.", font=("Courrier", 10), fg = "red")
        label_error.pack()
    else:
        pay()


def confirmation():
    client = Client(keys.account_sid, keys.auth_token)
    message = client.messages.create(
        body = "Hi " + owner_name + ", Parking for " + str(vehicle_number) +" is CONFIRMED ! Your parking will expires after alloted time.",
        from_ = keys.twilio_number,
        to = "+91" + str(phone)
    )


def confirmationII():
    client = Client(keys.account_sid, keys.auth_token)
    message = client.messages.create(
        body = "Hi " + owner_name + ", Parking for " + str(vehicle_number) +" is successfully extended ! Your parking will expires after alloted time.",
        from_ = keys.twilio_number,
        to = "+91" + str(phone)
    )    


def entry():
    mydb = sq.connect(
    host = "localhost",
    user = "root",
    passwd = "root"
    )
    curr = mydb.cursor()
    curr.execute("use park;")
    q = "insert into parking values( %s, %s, %s, %s);"
    val = (vehicle_number, owner_name, vehicle_type, phone);
    curr.execute(q, val)
    mydb.commit()
    #print(q)


def blank():
    #just test
    print()


def error():
    window_error = root.Tk()
    window_error.geometry("300x100")
    window_error.title("Error")
    title = root.Label(window_error, text = "Error ! Vehicle Number is Not Regitered.", fg = "red", font=("AgencyFB", 10, "bold"))
    title.place(x = 20, y = 10)

    button = root.Button(window_error, text = "    OK    ", font = ("Arial", 8), relief = "groove", command = window_error.destroy)
    button.place(x = 130, y = 50)


def login():
    global veh, login_phone
    window_login = root.Tk()
    window_login.geometry("380x220")
    window_login.title("Login")

    Vehicle_Number = root.Label(window_login, text = "Enter Your Vehicle Number", font = ("Arial", 8, "bold"))
    Vehicle_Number.place(x = 20, y = 20)
    veh = root.Entry(window_login, width=18)
    veh.place(x = 220, y = 20)

    contact_number = root.Label(window_login, text = "Contact Number", font = ("Arial", 8, "bold"))
    contact_number.place(x = 20, y = 90)
    login_phone = root.Entry(window_login, width = 18)
    login_phone.place(x = 220, y = 90)

    button = root.Button(window_login, text = "     login     ", font = ("Arial", 10), relief = "groove", command = login_check)
    button.place(x = 180, y = 130)


def main():
    window_main = root.Tk()
    window_main.geometry("550x350")
    window_main.title("PARKING SLOT PORTAL")
    
    #labels
    label_1 = root.Label(text = "Hello There! Welcome To Parking Portal",
                         font = ("Agency FB", 18, "bold"), fg="blue").pack()
    label_2 = root.Label(text = "How we can help you",
                         font = ("ariel", 12)).place(x = 200, y = 120)
    
    #buttons
    button_book = root.Button(window_main, text = "  Book Parking Slot  ", relief="groove", command = book)
    button_book.place(x = 90, y = 180)
    
    button_tutorial = root.Button(window_main, text = "  Extend Parking Time  ", relief="groove", command = login)
    button_tutorial.place(x = 320, y = 180)
    
    button_quite = root.Button(window_main, text="  Quite  ",fg="red", relief="groove", command = exit)
    button_quite.place(x = 250, y = 260)
    
    window_main.mainloop()
    
    
# MAIN
main()