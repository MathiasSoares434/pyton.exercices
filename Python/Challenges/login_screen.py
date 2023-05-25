from tkinter import Tk, Label, Entry, Button

def cheking_credencials():
    user= entry_user.get()
    password= entry_password.get()
    if user == "adm" and password == "12345":
        message["text"] = "Bem-vindo, " + user + "!"
    else:
        message["text"] = "Credenciais inválidas"

window= Tk()
window.title("Tela de login")
window.geometry("320x200")

label_user= Label(window, text="Usuário")
label_user.pack()
entry_user= Entry(window)
entry_user.pack()

label_password= Label(window, text="Senha:")
label_password.pack()
entry_password= Entry(window, show="*")
entry_password.pack()

button_login= Button(window, text="Login", command=cheking_credencials)
button_login.pack()

message= Label(window, text="")
message.pack()

window.mainloop()