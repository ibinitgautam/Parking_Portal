import tkinter as root

window_error = root.Tk()
window_error.geometry("300x100")
window_error.title("Error")
title = root.Label(window_error, text = "Error ! Vehicle Number is Not Regitered.", fg = "red", font=("AgencyFB", 10, "bold"))
title.place(x = 20, y = 10)

button = root.Button(window_error, text = "    OK    ", font = ("Arial", 8), relief = "groove", command = window_error.destroy)
button.place(x = 130, y = 50)

window_error.mainloop()