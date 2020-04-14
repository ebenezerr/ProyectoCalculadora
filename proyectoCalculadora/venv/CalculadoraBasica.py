'''
Calculadora simple con interfaz grafica
'''
import tkinter as tk

root = tk.Tk()
numero_agregadox = tk.StringVar()
numero_agregadoy = tk.StringVar()
resultado = tk.StringVar()

sw = True
menu = '''
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
'''
#Logica del programa
def sumar():
    a = int(numero_agregadox.get())
    b = int(numero_agregadoy.get())
    res = a + b
    resultado.set(str(res))
    print(res)

def restar():
    a = int(numero_agregadox.get())
    b = int(numero_agregadoy.get())
    res = a - b
    resultado.set(str(res))
    print(res)

def multiplicar():
    a = int(numero_agregadox.get())
    b = int(numero_agregadoy.get())
    res = a * b
    resultado.set(str(res))
    print(res)

def dividir():
    a = int(numero_agregadox.get())
    b = int(numero_agregadoy.get())
    res = a / b
    resultado.set(str("{:.4f}".format(res)))
    print(res)

def limpiar():
    numero_agregadoy.set('')
    numero_agregadox.set('')
    resultado.set('')

#Interfaz de  usuario
root.geometry('500x500')
root.title('CALCULADORA')

root.configure(bg="#2F4858")

tk.Label(root, text='CALCULADORA BASICA', bg="#F79824", fg='white', font=('', 28)).place(x=30, y=30)

tk.Label(root, text='Valor 1: ', bg="#2F4858", fg='white', font=('', 15)).place(x=120, y=100)
tk.Entry(root, justify='center', textvariable=numero_agregadox).place(x=240, y=105)

tk.Label(root, text='Valor 2: ', bg="#2F4858", fg='white', font=('', 15)).place(x=120, y=135)
tk.Entry(root, justify='center', textvariable=numero_agregadoy).place(x=240, y=140)

tk.Button(root, text='Sumar', bd=0, command= sumar,font=('helv36', 18), background="#FDCA40").place(x=220, y=190)
tk.Button(root, text='Restar', bd=0, command= restar,font=('helv36', 18), background="#FDCA40").place(x=220, y=240)
tk.Button(root, text='Multiplicar', bd=0, command= multiplicar,font=('helv36', 18), background="#FDCA40").place(x=200, y=290)
tk.Button(root, text='Dividir', bd=0, command= dividir,font=('helv36', 18), background="#FDCA40").place(x=220, y=340)
tk.Button(root, text='Limpiar', bd=0, command= limpiar,font=('helv36', 18), background="#FDCA40").place(x=216, y=390)

tk.Label(root, text='RESULTADO:', bg="#2F4858", fg='white', font=('', 15)).place(x=30, y=450)
tk.Label(root, textvariable=resultado, bg="#2F4858", fg='white', font=('', 24)).place(x=180, y=445)

root.mainloop()

#Consola


print(menu)

while sw:
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        print('Programa finalizado')
        sw = False
    else:
        print('Intente de nuevo')
