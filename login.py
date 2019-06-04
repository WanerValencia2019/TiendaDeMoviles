from opciones import *
import MySQLdb

PYTHON_VERSION=sys.version_info.major

if PYTHON_VERSION<3:
    try:
        from tkinter import *
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Se requiere el modulo 'tkinter' ")
    else:
        try:
            from tkinter import *
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Se requiere el modulo 'tkinter' ")

#creando ventana principal
ventana=Tk()
ventana.geometry("300x270")
ventana.title("Company Phone Telecomunications")
ventana.configure(bg="cyan")
#centrar ventana en la pantalla del  ordenador
ventana.update_idletasks()
w=ventana.winfo_width()
h=ventana.winfo_height()
extraW=ventana.winfo_screenwidth()-w
extraH=ventana.winfo_screenheight()-h
ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))


#etiqueta en python
etiqueta1=Label(ventana,text="Bienvenido Al Futuro, Tú eres el cambio.",fg="black",bg="cyan",font=("arial",7))
etiqueta1.place(x=5,y=2)
etiqueta_login=Label(ventana,text="Login",fg="red",bg="cyan",font=("Arial",12)).place(x=125,y=30)

#ogin de prueba nada mas
"""def verifica():
    false="Usuario o/y Contraseña incorrectos"
    if (usuario.get() == "20030308" and password.get() == "wnaesvlamro"):
        opciones()
        ventana.destroy()

    else:
        mensaje = Label(ventana, text=false,fg="red")
        mensaje.place(x=65, y=168)"""
#CONSULTA PARA EL LOGIN
def verifica():
    false = "Usuario o/y Contraseña incorrectos"
    conexion = MySQLdb.connect(host='localhost', user='root', passwd='', db="tienda_moviles")
    consulta=conexion.cursor()
    cadenaCONSULTA = "SELECT USUARIO,CONTRASEÑA FROM `usuarios` WHERE `USUARIO`=%s AND `CONTRASEÑA`=%s"
    if consulta.execute(cadenaCONSULTA,(usuario.get(),password.get())):
        conexion.commit()
        ventana.destroy()
        opciones()
    else:
        conexion.commit()
        mensaje = Label(ventana, text=false, fg="red")
        mensaje.place(x=65, y=168)


usuario=StringVar()
password=StringVar()
#etiquetas del login
etiqueta2=Label(ventana,text="Usuario: ",fg="blue",bg="cyan",font=("Arial",9)).place(x=10,y=80)
caja_text1=Entry(ventana,textvariable=usuario)
caja_text1.place(height=25,width=150,x=65,y=75)
etiqueta3=Label(ventana,text="Contraseña: ",fg="blue",bg="cyan",font=("Arial",9)).place(x=10,y=130)
caja_text2=Entry(ventana,textvariable=password,show='*')
caja_text2.place(height=25,width=150,x=85,y=130)
#Boton en python
bton1=Button(ventana,text="Iniciar Sesión",bg="white",command=lambda:
verifica())
bton1.place(x=110,y=200)

#TENGO QUE INICIALZAR LAS VARIABLES EN LA VENTANA PRINCIPAL PARA QUE PUEDA FUNCIONAR
#variables del inventario de moviles
fecha=StringVar()
mark=StringVar()
modelo=StringVar()
cantidad=StringVar()
valor=StringVar()
#Inicializa la ventana, es decir la ejecuta
ventana.mainloop()

