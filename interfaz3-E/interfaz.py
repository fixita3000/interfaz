import tkinter
from tkinter import ttk
import json

with open('errores.json',"r") as archivo:
    datos =json.load(archivo)

def obtenerdesc():
    dato_ingresado = entrada_texto.get()
    print(dato_ingresado)
    for error in datos["errores"]:
        if error["codigo"] == dato_ingresado:
            desc_error.config(text=error["desc"])
            break
        else:
            print("dato erroneo")


ventana = tkinter.Tk()
ventana.title("Codigos de error")

#titulo 
titulo = ttk.Label(ventana,text="Ingresa el codigo", font="Calibri 24 bold")
titulo.pack(pady= 10, padx=10)

entrada_texto = ttk.Entry(ventana)
entrada_texto.pack(pady=10,padx=10)

btn_buscar = ttk.Button(ventana, text="Buscar codigo",command=obtenerdesc)
btn_buscar.pack(pady=10, padx=10)

desc_error = ttk.Label(ventana, text="")
desc_error.pack(pady=10)
ventana.mainloop()