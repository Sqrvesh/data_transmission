import customtkinter
import socket
import pyglet
pyglet.font.add_file("Satoshi-Variable.ttf")


def send_msg_func():
    data = send_msg.get()
    if data == "":
        pass


    else:
        s.send(data.encode())
        send_msg.delete(0, customtkinter.END)

def get_msg_func():
    data = s.recv(1024).decode()
    if data:
        client_msg.configure(text=data)
    else:
        pass


app = customtkinter.CTk()
app.title("Client Screen")
app.geometry("1200x450")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

main_frame = customtkinter.CTkFrame(app, fg_color = "#222426")
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.columnconfigure(0, weight=4)
main_frame.columnconfigure(1, weight=1)
#main_frame.rowconfigure((0,1,2,3,4), weight=1)

main_title = customtkinter.CTkLabel(main_frame, text="Client Screen", font = ("Satoshi-Variable.ttf", 40))
main_title.grid(row=0, column=0, padx=20, pady=20, sticky = "nsew", columnspan = 2)

client_msg_title = customtkinter.CTkLabel(main_frame, text="Text from Server:", font = ("Satoshi-Variable.ttf", 30))
client_msg_title.grid(row=1, column=0, padx=20, sticky = "w")

client_msg = customtkinter.CTkLabel(main_frame, text="", font = ("Satoshi-Variable.ttf", 25))
client_msg.grid(row=2, column=0, padx=20, pady=(10,20), sticky="nsew")

get_data_button = customtkinter.CTkButton(main_frame, text="Get", height= 36, width= 200, font = ("Satoshi-Variable.ttf", 18), command=get_msg_func)
get_data_button.grid(row=2, column=1, padx=(0, 20), pady=10, sticky="ns")

send_msg_title = customtkinter.CTkLabel(main_frame, text="Reply to Server:", font = ("Satoshi-Variable.ttf", 30))
send_msg_title.grid(row=3, column=0, padx=20, pady=(70,0), sticky = "w")

send_msg = customtkinter.CTkEntry(main_frame, width= 500 , height= 30, font = ("Satoshi-Variable.ttf", 15))
send_msg.grid(row=4, column=0, padx=(20,5), pady=10, sticky="ew")

send_button = customtkinter.CTkButton(main_frame, text="Send", height= 36, width= 200, font = ("Satoshi-Variable.ttf", 18), command=send_msg_func)
send_button.grid(row=4, column=1, padx=(0, 20), pady=10)


#socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.44.216", 1234))

app.mainloop()



