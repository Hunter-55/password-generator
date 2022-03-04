import tkinter as tk
from tkinter import messagebox
import random

arrUser = []
# ---- configuarcion de algunos widget ---
color_bg = 'skyblue'
colorbg_pass = 'steelblue'
color_text = 'black'
font_text = 'Arial 13'
widthtitle = 70
heighttitle = 3

# ======== [ Genera contraseñas random ] ========
def GenerarContraseña(nameBox,nameUser,buttonaux,arrUser,window2):
    letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros=['1','2','3','4','5','6','7','8','9','0']
    simbolo=['!','#','$','%','&','/',
    ',','.',';',':','-','_','¿','?','¡','+','*','@']
    password=[]
    num2 = int(nameBox.get())
    # --- recorre la cantidad de usuario ---
    # --- y se les asigna caracteres aleatorios ---
    for j in range(len(arrUser)):
        password.append([])
        for i in range(num2):
            definirdigito = random.randint(0, 2)
            if definirdigito == 0:
                num = random.randint(0, 9)
                password[j].append(numeros[num])
            elif definirdigito == 1:
                sim = random.randint(0, 17)
                password[j].append(simbolo[sim])
            else:
                aux = random.randint(0, 1)
                mayuscula_minuscula = random.randint(0, 26)
                if aux == 0:
                    password[j].append(letras[mayuscula_minuscula])
                else:
                    password[j].append(letras[mayuscula_minuscula].upper())
    userpass=''
    # --- ordenamos a los usuarios por el tamañao de su nombre ---
    # --- para identificar el nombre mas largo y asi modificar adecuadamente la caja de texto ---
    arrUser2 = sorted(arrUser,key=len)
    for i in range(len(arrUser)):
        pass1 = ""
        for j in range(len(password[i])):
            pass1 += password[i][j]
        userpass += str(arrUser[i])+":  "+pass1+'\n' # agregamos un string con los usuarios y el password
    
    # ----- eliminando widget
    nameBox.destroy()
    nameUser.destroy()
    buttonaux.destroy()
    
    passfinish = tk.Label(window2,
        text="Contraseñas de los usuarios",fg=color_text,bg=color_bg,font = font_text)
    passfinish.pack()
    # --- caja de texto ---
    text_box = tk.Text(window2,width=len(arrUser2[len(arrUser2)-1])+len(password[0])+4,height=len(arrUser))
    text_box.insert("1.0", userpass)
    text_box.pack()

    vacio = tk.Label(window2,bg=color_bg,text="")
    vacio.pack()
    print(password)
    return password


# ======== [ contador crea una nueva ventana donde se guardara los usuarios en un arreglo ] ========
def contador(nameBox,nameUser,buttonaux,window2):
    
    if nameBox.get() != '':

        if len(arrUser) <= int(entry.get())-1:
            arrUser.append(nameBox.get())
            nameBox.delete(0, tk.END)
            
            if len(arrUser) == (int(entry.get())):
                window.destroy()
                nameBox.delete(0, tk.END)
                nameBox.destroy()
                nameUser.destroy()
                buttonaux.destroy()

                nameBox= tk.Entry(window2,text="Placeholder text")
                nameBox.insert(50, "")

                nameUser = tk.Label(window2,
                text="Cuantos Caracteres tendra la contraseña",fg=color_text,bg=color_bg,font = font_text)

                vacio = tk.Label(window2,bg=color_bg,text="")

                buttonaux =tk.Button(window2, text='Generar Contraseña',fg=color_text,bg=colorbg_pass,font='Arial 11',
                command=lambda:GenerarContraseña(nameBox,nameUser,buttonaux,arrUser,window2))

                nameUser.pack()
                nameBox.pack()
                buttonaux.pack()
                vacio.pack()

    else:   
        print("campo vacio")
        messagebox.showinfo('Alerta', 'Campo vacío') # mensaje de alerta


# # ======== [ crea la primera ventana donde pedira un numero para la cantidad de usuario ] ========
def show_entry_fields():
    num = str(entry.get())

    if num.isnumeric() and int(num) > 0:
        window2 = tk.Tk()
        window2.title("Generador de Contraseñas")
        window2.configure(bg=color_bg)
        title = tk.Label(window2,text="Generar Contraseñas\n",
        fg="whitesmoke",bg=colorbg_pass,font=font_text,width=widthtitle,height=heighttitle)

        nameBox= tk.Entry(window2,text="Placeholder text")
        nameBox.insert(50, "")

        nameUser = tk.Label(window2,
        text="Nombre de Usuarios",fg=color_text,bg=color_bg,font = font_text)

        vacio = tk.Label(window2,bg=color_bg,text="")

        buttonaux =tk.Button(window2, text='Agregar',fg=color_text,bg=colorbg_pass,font='Arial 11',
        command=lambda:contador(nameBox,nameUser,buttonaux,window2))
    
        title.pack()
        nameUser.pack()
        nameBox.pack()
        buttonaux.pack()
        vacio.pack()
        window2.mainloop()

    else:
        print("no es numero")
        messagebox.showinfo('Alerta', 'Campo vacío')

def init():
     #Una ventana es una instancia de la Tkclase de Tkinter. 
    global window
    window = tk.Tk()
    window.configure(bg=color_bg)
    window.title("Generador de Contraseñas")

    greeting = tk.Label(text="Generar Contraseñas",
        fg="whitesmoke",bg=colorbg_pass,font=font_text,width=widthtitle,height=heighttitle)

    textUser = tk.Label(text="¿Cuantos Usuarios Cambiaran su contraseña?\n",
        fg=color_text,bg=color_bg,font = font_text)
    global entry
    entry = tk.Entry(window,text="Placeholder text")
    entry.insert(50, "")

    button =tk.Button(window, text='Ingresar',fg=color_text,bg=colorbg_pass,font='Arial 11' ,command=show_entry_fields)

    Empty = tk.Label(text="",bg=color_bg)

    greeting.pack()
    textUser.pack()
    entry.pack()
    button.pack()
    Empty.pack()
    window.mainloop()

if __name__ == "__main__":
    init()









