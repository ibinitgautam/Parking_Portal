import tkinter as root
from tracemalloc import Frame

def pay():
    window_pay = root.Tk()
    window_pay.geometry("280x250")
    window_pay.title("Payment")

    root.Label(window_pay, text = "Choose Your Payment Option.", font = ("AgencyFB", 10)).pack()

    button_upi = root.Button(window_pay, text="UPI", relief="groove", command="blank")
    button_upi.place(x = 70, y = 100)

    button_card = root.Button(window_pay, text="Debit Card", relief="groove", command="blank")
    button_card.place(x = 150, y = 100)

    cancel = root.Button(window_pay, text = "Cancel", relief="groove", command="blank")
    window_pay.mainloop()

    

    window_pay.mainloop()


def blank():
    print()


pay()