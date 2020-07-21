import platform,socket,psutil
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title('INFO-PC')
window.iconbitmap('computer_icon.ico')

window.geometry('215x205')

hostname = socket.gethostname()
os = platform.system() #Sistema operacional
machine = platform.machine() #Arquitetura
user = platform.node() #Nome de Usuário
IP = socket.gethostbyname(hostname) #Internet Protocol
ram = (round(psutil.virtual_memory().total / (1024.0 **3))) #Memória RAM
so = os + machine

lbltitle = tk.Label(window, text='Informações', font=('Times New Roman', 15), padx=10, pady=10)
lbluser = tk.Label(window, text='Usuário: %s' %user, font=('Montserrat', 10), padx=5, pady=5) 
lblso = tk.Label(window, text='Sistema operacional: %s' %so, font=('Montserrat', 10), padx=5, pady=5)
lblip = tk.Label(window, text='IP: %s' %IP, font=('Montserrat', 10), padx=5, pady=5)  
lblram = tk.Label(window, text='Memória RAM: %sGB' %ram, font=('Montserrat', 10), padx=5, pady=5) 

def creditos():
	messagebox.showinfo('Creditos', 'Discord: LucasSilvaDev#6058\n\nGitHub: LucasSilvaD')

btncreditos = tk.Button(window, text='Créditos', font=('Arial', 10), command=creditos, padx=3, pady=3)

lbltitle.grid(column=0, row=0)
lbluser.grid(column=0, row=1)
lblso.grid(column=0, row=2)
lblip.grid(column=0, row=3)
lblram.grid(column=0, row=4)
btncreditos.grid(column=0, row=5)

window.mainloop()