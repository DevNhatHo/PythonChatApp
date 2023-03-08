import tkinter
import socket
from tkinter import *
from threading import Thread

def receive():
    while True:
        try:
            msg = s.recv(1024).decode('utf8')
            msg_list.insert(tkinter.END,msg)
        except:
            print("There is an error recieving the message")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg,'utf8'))
    if msg=='#quit':
        s.close()
        window.close()

def on_closing():
    my_msg.set('#quit')
    send()
window = Tk()
window.title("Chatroom")
window.configure(bg="gray")


message_frame =Frame(window, height=100, width=100, bg='white')
message_frame.pack()

my_msg=StringVar()
my_msg.set=("")

scroll_bar= Scrollbar(message_frame)

msg_list = Listbox(message_frame, height=15,width=100,bg="white",yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT,fill=Y)
msg_list.pack(side=LEFT,fill=BOTH)
msg_list.pack()
label = Label(window,text="Enter the message", fg='white', font='Aerial',bg='green')
label.pack()
entry_field= Entry(window, textvariable=my_msg,fg='black',width=50)
entry_field.pack()

send_Button = Button(window,text="SEND",font='Aerial',fg='white',command=send)
send_Button.pack()

quite_Button = Button(window,text='QUIT',font='Aerial',fg='white',command=on_closing)

Host='127.0.0.1'
Port=8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))

receive_Thread =Thread(target=receive)
receive_Thread.start()
mainloop()