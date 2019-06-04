from tkinter import *
import MySQLdb
import login
from  tkinter import messagebox

def salir():
    salir=messagebox.askyesno("Cerrar Sesión", "¿Deseas Salir?")
    if salir==True:
        quit()

def opciones():
    ventana2 = Tk()
    ventana2.geometry("310x280")
    ventana2.title("Company Phone Telecomications")
    ventana2.configure(bg="cyan")
    #centrando la ventana
    ventana2.update_idletasks()
    w = ventana2.winfo_width()
    h = ventana2.winfo_height()
    extraW = ventana2.winfo_screenwidth() - w
    extraH = ventana2.winfo_screenheight() - h
    ventana2.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
    #etiqueta de bienvenida y botones de opciones
    id=Label(ventana2,text="ID: "+login.usuario.get(),fg="black",bg="cyan")
    id.place(x=215,y=5)
    benvenue=Label(ventana2,text="Bienvenido ",fg="black",bg="cyan",font=("Arial",11))
    benvenue.place(x=3,y=2)
    opc=Label(ventana2,text="Menú", fg="black",bg="orange",font=("calibri",12))
    opc.place(x=127,y=60)
    boton1=Button(ventana2,text="Inventario de telofonos moviles y tabletas",fg="red",bg="white",command=lambda:
    inventarioMoviles())
    boton1.place(x=40,y=105)
    boton2=Button(ventana2,text="Inventario de accesorios telefonicos",fg="red",bg="white",command=lambda: inventario_Articulos() )
    boton2.place(x=40,y=145)
    boton3=Button(ventana2,text="Buscar Producto ",fg="red",bg="white",command=lambda:
    buscar())
    boton3.place(x=97,y=185)
    boton4=Button(ventana2,text="Salir",fg="blue",bg="white",font=("Arial",10),command=lambda:
    salir())
    boton4.place(x=250,y=240)
    def buscar():
        def Consulta():
            if opcion1.get()==1:
                tabla="inventario_móviles"
                campo=str(opcion2.get())
                cadena = "SELECT * FROM `inventario_móviles` WHERE %s=%s"

            else:
                if opcion1.get()==2:
                    tabla="inventario_articulos"
                    campo=str(opcion3.get())
                    cadena = "SELECT * FROM `inventario_articulos` WHERE %s=%s"
                else:
                    print("Error")
            conexion = MySQLdb.connect(host='localhost', user='root', passwd='', db="tienda_moviles")
            consulta = conexion.cursor()
            def llamar():
                cadena = "SELECT * FROM `inventario_móviles` WHERE %s=%s"
                campo="MARCA"
                hol="Samsung"
                #EL PROGRAMA SE TUVO QUE HACER HASTA AQUI DEBIDO A QUE NO TENGO CONOCIMIENTOS DE COMO HACER LA CONSULTA SIN QUE ME SALGA EL EEROR DE NO SE CONVIRTIERON TODOS A BYTES
                if consulta.execute('SELECT * FROM `inventario_móviles` WHERE MARCA="Samsung"'):
                    conexion.commit()
                    datos=consulta.fetchall()
                    for dato in datos:
                        print(dato)
                    resultado.set(datos)
                else:
                    conexion.commit()
                    resultado.set("NO SE ENCONTRÓ NINGUNA COINCIDENCIA")
                conexion.close()
            llamar()

        ventana4 = Toplevel(ventana2)
        ventana4.geometry("550x450")
        ventana4.title("Company Phone Telecomications")
        ventana4.configure(bg="cyan")
        # centrando la ventana
        ventana4.update_idletasks()
        w = ventana4.winfo_width()
        h = ventana4.winfo_height()
        extraW = ventana4.winfo_screenwidth() - w
        extraH = ventana4.winfo_screenheight() - h
        ventana4.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
        # variable para buscar
        etiqueta2=Label(ventana4,text="Busqueda Por: ",bg="cyan")
        etiqueta2.place(x=10,y=38)
        #variables
        buscar = StringVar()
        opcion1 = IntVar()
        opcion2 = StringVar()
        opcion3 = StringVar()
        resultado=StringVar()

        caja_buscar=Entry(ventana4,textvariable=buscar)
        caja_buscar.place(height=28,width=250,x=10,y=128)
        boton=Button(ventana4,text="Buscar",command=lambda:Consulta())
        boton.place(x=270,y=128)
        etiqueta1=Label(ventana4,text="Buscar Registros Guardados", bg="cyan",fg="black")
        etiqueta1.place(x=250,y=10)
        moviles=Radiobutton(ventana4,text="Inventario de Moviles",value=1, variable=opcion1)
        moviles.place(x=10,y=58)
        movil_Opciones = Spinbox(ventana4, values=("FECHA", "MARCA", "MODELO", "VALOR(UNIDAD)"),textvariable=opcion2)
        movil_Opciones.place(x=10, y=88)
        articulos = Radiobutton(ventana4, text="Inventario de Articulos ", value=2, variable=opcion1)
        articulos.place(x=200,y=58)
        articulos_Opciones=Spinbox(ventana4,values=("FECHA","PRODUCTO","VALOR(UNIDAD)"),textvariable=opcion3)
        articulos_Opciones.place(x=200,y=88)
        campo_Resultado=Entry(ventana4,textvariable=resultado)
        campo_Resultado.place(height=260,width=500,x=10,y=180)

    def inventarioMoviles():
        ventana2.state(newstate='iconic')
        ventana3=Toplevel(ventana2);
        ventana3.geometry("520x380")
        ventana3.title("Company Phone Telecomications")
        ventana3.configure(bg="cyan")
        # centrando la ventana
        ventana3.update_idletasks()
        w = ventana3.winfo_width()
        h = ventana3.winfo_height()
        extraW = ventana3.winfo_screenwidth() - w
        extraH = ventana3.winfo_screenheight() - h
        ventana3.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
        #   VARIABLES QUE GUARDARAN EL INVENTARIO
        #esto limpiara la caja cuando se presione guardar registro
        """def guardar_registro():
            date = f.get()
            marca = M.get()
            modelo = m.get()
            cantidad =c.get()
            valor = v.get()"""
        def guardar_registro():
                def limpiar_Campo1():
                    f.delete(0,END)
                def limpiar_Campo2():
                    M.delete(0,END)
                def limpiar_Campo3():
                    m.delete(0,END)
                def limpiar_Campo4():
                    c.delete(0,END)
                def limpiar_Campo5():
                    v.delete(0,END)
                #conexion a base de datos
                conexion = MySQLdb.connect(host='localhost', user='root', passwd='', db="tienda_moviles")
                consulta = conexion.cursor()  # sirve para hacer las consultas
                precio=v.get()
                unidades=c.get()
                cadena = "INSERT INTO `inventario_móviles` (`FECHA`, `MARCA`, `MODELO`, `VALOR(UNIDAD)`, `CANTIDAD`) VALUES (%s,%s,%s,%s,%s)";
                consulta.execute(cadena,(f.get(),M.get(),m.get(),precio,unidades))
                conexion.commit()
                conexion.close()
                #metodos para limpiar los campos NOTA: LO HICE ASI PORQUE NO ME FUNCIONABAN JUNTOS
                messagebox.showinfo("File Save","Registro guardado con éxito")
                limpiar_Campo1()
                limpiar_Campo2()
                limpiar_Campo3()
                limpiar_Campo4()
                limpiar_Campo5()

        #creando los campos para el invenatrio con dos botones el retroceder y el de añadir un nuevo elemento
        text1=Label(ventana3,text="Inventario De Telefonos Moviles y Tabletas",fg="black",bg="cyan")
        text1.place(x=190,y=15)

        botonBack=Button(ventana3,text="Crear Nuevo Inventario")
        botonBack.place(x=20,y=330)
        botonShow=Button(ventana3,text=" Mostrar Inventario ")
        botonShow.place(x=360,y=330)
        botonSAVE=Button(ventana3,text="Guardar Registro",command=lambda:guardar_registro())
        botonSAVE.place(x=185,y=250)
        fecha=Label(ventana3,text="Fecha: ",bg="cyan")
        fecha.place(x=49,y=70)
        f=Entry(ventana3,textvar=login.fecha)
        f.place(x=93,y=70)
        Mark= Label(ventana3, text="Marca: ",bg="cyan")
        Mark.place(x=49, y=100)
        M= Entry(ventana3,textvar=login.mark)
        M.place(x=93, y=100)
        model= Label(ventana3, text="Modelo: ",bg="cyan")
        model.place(x=45, y=130)
        m= Entry(ventana3,textvar=login.modelo)
        m.place(x=93, y=130)
        Cantidad=Label(ventana3,text="Cantidad: ",bg="cyan")
        Cantidad.place(x=36,y=160)
        c= Entry(ventana3,textvar=login.cantidad)
        c.place(x=93, y=160)
        Valor_UNIDAD = Label(ventana3, text="Valor x Unidad: ",bg="cyan")
        Valor_UNIDAD.place(x=10, y=190)
        v= Entry(ventana3,textvar=login.valor)
        v.place(x=93, y=190)
        #obteniendo valores de las cajas

    def inventario_Articulos():
        ventana5 = Toplevel(ventana2)
        ventana5.geometry("500x350")
        ventana5.title("Company Phone Telecomications")
        ventana5.configure(bg="cyan")
        # centrando la ventana
        ventana5.update_idletasks()
        w = ventana5.winfo_width()
        h = ventana5.winfo_height()
        extraW = ventana5.winfo_screenwidth() - w
        extraH = ventana5.winfo_screenheight() - h
        ventana5.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))

        def guardar_registro():
            def limpiar_Campo1():
                f.delete(0, END)
            def limpiar_Campo3():
                p.delete(0, END)
            def limpiar_Campo4():
                c.delete(0, END)
            def limpiar_Campo5():
                v.delete(0, END)
            # conexion a base de datos
            conexion = MySQLdb.connect(host='localhost', user='root', passwd='', db="tienda_moviles")
            consulta = conexion.cursor()  # sirve para hacer las consultas
            precio = v.get()
            unidades = c.get()
            cadena = "INSERT INTO `inventario_articulos` ( `FECHA`, `PRODUCTO`,`CANTIDAD`, `VALOR(UNIDAD)`) VALUES (%s,%s,%s,%s)";
            consulta.execute(cadena, (f.get(),p.get(),unidades,precio))
            conexion.commit()
            conexion.close()
            # metodos para limpiar los campos NOTA: LO HICE ASI PORQUE NO ME FUNCIONABAN JUNTOS
            messagebox.showinfo("File Save", "Registro guardado con éxito")
            limpiar_Campo1()
            limpiar_Campo3()
            limpiar_Campo4()
            limpiar_Campo5()
            # creando los campos para el invenatrio con dos botones el retroceder y el de añadir un nuevo elemento

        text1 = Label(ventana5, text="Inventario De Accesorios Telefonicos", fg="black", bg="cyan")
        text1.place(x=160, y=15)

        botonBack = Button(ventana5, text="Crear Nuevo Inventario")
        botonBack.place(x=20, y=300)
        botonShow = Button(ventana5, text=" Mostrar Inventario ")
        botonShow.place(x=360, y=300)
        botonSAVE = Button(ventana5, text="Guardar Registro", command=lambda: guardar_registro())
        botonSAVE.place(x=185, y=250)
        fecha = Label(ventana5, text="Fecha: ", bg="cyan")
        fecha.place(x=55, y=70)
        f = Entry(ventana5, textvar=login.fecha)
        f.place(x=93, y=70)
        product= Label(ventana5, text="Producto: ", bg="cyan")
        product.place(x=38, y=100)
        p= Entry(ventana5, textvar=login.mark)
        p.place(x=93, y=100)
        Cantidad = Label(ventana5, text="Cantidad: ", bg="cyan")
        Cantidad.place(x=36, y=130)
        c = Entry(ventana5, textvar=login.cantidad)
        c.place(x=93, y=130)
        Valor_UNIDAD = Label(ventana5, text="Valor x Unidad: ", bg="cyan")
        Valor_UNIDAD.place(x=10, y=160)
        v = Entry(ventana5, textvar=login.valor)
        v.place(x=93, y=160)








