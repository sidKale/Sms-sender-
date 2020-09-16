import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'Q7q5GjOkd2Ae1RK9uY8rWbZlNfLaoESPgpUc0Ch3BwimMT4nsDucFVRU14d6jy8Ho9SLDvYthOGiICbl',
        'sender_id': 'FastWP',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

#Developed by "SIDDHESH KALE"
def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
lb1 = Label(root, text = "Enter Number Below to Send Sms", bg = "BLUE", fg = "WHITE")
lb1.pack()
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
lb2 = Label(root, text="Your Message", bg = "BLUE", fg = "WHITE")
lb2.pack()
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()
