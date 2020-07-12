
"""En este modulo se construye la interfaz grafica"""

from Funcionalidad import *

class Main_Window(Functionality):

	def __init__(self,Window):
		self.WindowMain=Window
		#Definir los atributos para la creacion de cuadros de texto
		self.AN,self.IP,self.Direc,self.Telef,self.Monto,self.Megas,self.FI=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

		self.ContraActual,self.ContraNueva,self.MostrarContra=StringVar(),StringVar(),BooleanVar()
		self.Age,self.Mes,self.Fecha,self.Pago=StringVar(),StringVar(),StringVar(),StringVar()
		self.Accion,self.FH,self.PH=StringVar(),StringVar(),StringVar()
		self.ValorOrden,self.ValorVista=IntVar(),IntVar()

		now = datetime.now() #Inicializar algunos cuadros de texto con datos por defecto
		self.FI.set(now.strftime('%d-%m-%Y')),self.IP.set('192.168.'),self.Megas.set('Mbps')

		#Definir estilos
		self.PCF,self.PCFS,self.PCL,self.PCLS='#466183','white','white','black'
		style,self.ST=ttk.Style(),('Arial',12)
		style.configure('my.TButton', font=('Arial', 12))
		style.layout('TNotebook.Tab', [])
		style.configure("Treeview.Heading", font=('Arial', 13))
		style.configure('Treeview', font=('Arial',12),rowheight=30)

		self.Datos=Data()
		#Guardar imagenes
		self.ImagenAjustes=PhotoImage(file='Imagenes/Ajustes.png')
		self.ImagenHistorial=PhotoImage(file='Imagenes/Historial.png')
		self.ImagenLista=PhotoImage(file='Imagenes/Lista.png')
		self.ImagenVerde = PhotoImage(file="Imagenes/Verde.png")
		self.ImagenAmarillo = PhotoImage(file="Imagenes/Amarillo.png")
		self.ImagenRojo = PhotoImage(file="Imagenes/Rojo.png")
		self.ImagenNegro = PhotoImage(file="Imagenes/Negro.png")
		self.ImagenAgregar = PhotoImage(file='Imagenes/Agregar.png')
		self.MainWindow(),self.Tab_Client_Table(),self.Tab_New_Client(),self.Tab_Change_Login(),self.Tab_Detall()
		self.CargarAgeMes()

	def Create_Window_Login(self,Window): #Ventana Login
		self.WindowLogin,ST,style=Window,('Arial',12),ttk.Style()
		style.configure('my.TButton', font=('Arial', 12))
		self.WindowLogin.title("Entrar a Gestion de Internet")
		self.WindowLogin.geometry("340x190+450+200")
		self.WindowLogin.iconbitmap("Imagenes/My_icon.ico")
		self.WindowLogin.resizable(0,0)
		Frame1=Frame(self.WindowLogin,width="450",height="50",bg='#466183')
		Frame1.pack()
		Label(Frame1,text="Internet Papuchin",bg='#466183',fg="white",font=ST).place(x=190,y=10)
		Frame2=Frame(self.WindowLogin,width="450",height="150")
		Frame2.pack()
		Label(Frame2,text="Usuario:",font=ST).place(x=50,y=20)
		Label(Frame2,text="Contraseña:",font=ST).place(x=25,y=50)
		self.CuadroUser=ttk.Entry(Frame2,font=ST,textvariable=self.User)
		self.CuadroUser.place(x=125,y=20)
		self.CuadroUser.focus()
		self.CuadroPass=ttk.Entry(Frame2,font=ST,show="•",textvariable=self.Password)
		self.CuadroPass.place(x=125,y=50)

		self.User.set("admin")

		Imagen2=PhotoImage(file="Imagenes/My_ico_User.png")
		Label(Frame2,image=Imagen2).place(x=70,y=75)
		
		self.WindowLogin.bind('<Return>',self.Access)
		BotonEntrar=ttk.Button(Frame2,text="Iniciar",width="20",style='my.TButton',command=self.Access)
		BotonEntrar.bind('<Button-1>', self.Access)
		BotonEntrar.place(x=123,y=85)

	def Tab_Change_Login(self): #Pestaña para cambio de contraseña
		Top=self.Pes4
		Label(Top,text="Contraseña Actual:",font=self.ST).place(x=25,y=25)
		Label(Top,text="Contraseña Nueva:",font=self.ST).place(x=25,y=65)

		self.CuadroActual=ttk.Entry(Top,font=self.ST,show="•",textvariable=self.ContraActual)
		self.CuadroActual.place(x=170,y=25)
		self.CuadroActual.focus()
		self.CajaContra=ttk.Entry(Top,font=self.ST,show="•",textvariable=self.ContraNueva)
		self.CajaContra.place(x=170,y=65)
		Top.bind('<Return>',self.CambiarContra)
		Label(Top,text="Mostrar Contraseña",font=self.ST).place(x=25,y=105)
		ttk.Checkbutton(Top,variable=self.MostrarContra,command=self.MostrarContrasena).place(x=170,y=107)
		BotonCambiar=ttk.Button(Top,text="Guardar",style='my.TButton',width=9,command=self.CambiarContra)
		BotonCambiar.place(x=170,y=145)
		BotonCancelar=ttk.Button(Top,text="Cancelar",style='my.TButton',width=9,command=lambda:(self.ContraActual.set(""),self.ContraNueva.set(""),self.MostrarContra.set(0)))
		BotonCancelar.place(x=265,y=145)


	def TopDatos(self,N): #Pestaña para mostrar datos de un cliente

		Top,Lista=Toplevel(),self.Datos.CargarCliente(N)
		Top.geometry('450x350+500+150')
		Top.resizable(0,0)
		for i in Lista:
			Label(Top,text='Apellidos y Nombres:  {}'.format(i[1]),font=self.ST).place(x=25,y=25)
			Label(Top,text='Dirección IP:\t   {}'.format(i[2]),font=self.ST).place(x=25,y=65)
			Label(Top,text='Dirección:\t\t   {}'.format(i[3]),font=self.ST).place(x=25,y=105)
			Label(Top,text='Telefono - Celular:\t   {}'.format(i[4]),font=self.ST).place(x=25,y=145)
			Label(Top,text='Monto mensual:\t   {}'.format(i[5]),font=self.ST).place(x=25,y=185)
			Label(Top,text='Megas disponibles:\t   {}'.format(i[6]),font=self.ST).place(x=25,y=225)
			Label(Top,text='Fecha de instalación:  {}'.format(i[7]),font=self.ST).place(x=25,y=265)
			Label(Top,text='Estado:\t\t   {}'.format(i[8]),font=self.ST).place(x=25,y=305)

	def EscribirFecha(self): #Mini Ventana para escribir la fecha de corte o reinstalacion del cliente
		Top,now=Toplevel(),datetime.today()
		Top.geometry('151x49+625+275')
		Top.resizable(0,0)
		Cajon=ttk.Entry(Top,font=self.ST,justify='center',width=16)
		Cajon.place(x=0,y=0)
		Cajon.insert(0,now.strftime('%d/%m/%Y'))

		ttk.Button(Top,text='Aceptar',command=lambda: self.ActualizarEstado(Top,Cajon.get())).place(x=0,y=24)
		ttk.Button(Top,text='Cancelar',command=lambda:Top.destroy()).place(x=75,y=24)

	def TopHistorial(self): #Pestaña para modificar el Historial de cliente
		NValorH=str(self.TablaHistorial.item(self.TablaHistorial.selection())['values'][0])
		if NValorH=='1':
			messagebox.showwarning('Mensaje','No se puede modificar este registro desde esta sección')
		else:
			Top,Lista=Toplevel(),self.Datos.CargarHistorial(self.NValorH)
			Top.geometry('225x165+615+260')
			Label(Top,text='Acción:').place(x=20,y=20)
			Label(Top,text='Fecha:').place(x=20,y=50)
			Label(Top,text='Monto:').place(x=20,y=80)
			ttk.Entry(Top,textvariable=self.Accion).place(x=70,y=20)
			ttk.Entry(Top,textvariable=self.FH).place(x=70,y=50)
			ttk.Entry(Top,textvariable=self.PH).place(x=70,y=80)
			ttk.Button(Top,text='Modificar',width=19,command=lambda: self.ActualizarHistorial(Top)).place(x=70,y=115)
			
			for k in Lista:
				self.Accion.set(k[1])
				self.FH.set(k[2])
				self.PH.set(k[3])

	def MainWindow(self): #Ventana principal
		self.WindowMain.title("Internet Papuchin")
		self.WindowMain.geometry("887x370+200+120")
		self.WindowMain.iconbitmap("Imagenes/My_icon.ico")
		self.WindowMain.resizable(0,0)

		self.Pestana=ttk.Notebook(self.WindowMain)
		self.Pestana.place(x=175,y=0)
		
		FramePes=Frame(self.WindowMain,bg=self.PCF,width=175,height=367)
		FramePes.place(x=0,y=3)

		#Creacion de pestañas		
		self.Pes1,self.Pes2,self.Pes3,self.Pes4=ttk.Frame(self.Pestana),ttk.Frame(self.Pestana),ttk.Frame(self.Pestana),ttk.Frame(self.Pestana)
		self.Pestana.add(self.Pes1),self.Pestana.add(self.Pes2),self.Pestana.add(self.Pes3),self.Pestana.add(self.Pes4)

		self.PesVerCli=Button(FramePes,text="   Clientes        ",font=self.ST,bg=self.PCFS,fg=self.PCLS,activebackground=self.PCFS,activeforeground=self.PCLS,relief='sunken',width=171,height=40,bd=0,image=self.ImagenLista,compound=LEFT)
		self.PesVerCli.place(x=0,y=50)
		self.PesNewCli=Button(FramePes,text="   Nuevo Cliente",font=self.ST,bg=self.PCF,fg=self.PCL,activebackground=self.PCFS,activeforeground=self.PCLS,relief='sunken',width=171,height=40,bd=0,image=self.ImagenAgregar,compound=LEFT)
		self.PesNewCli.place(x=0,y=95)
		self.PesDetall=Button(FramePes,text=" Detalles de pago",font=self.ST,bg=self.PCF,fg=self.PCL,activebackground=self.PCFS,activeforeground=self.PCLS,relief='sunken',width=171,height=40,bd=0,image=self.ImagenHistorial,compound=LEFT)
		self.PesDetall.place(x=0,y=140)
		self.PesAjust=Button(FramePes,text="    Ajustes         ",font=self.ST,bg=self.PCF,fg=self.PCL,activebackground=self.PCFS,activeforeground=self.PCLS,relief='sunken',width=171,height=40,bd=0,image=self.ImagenAjustes,compound=LEFT)
		self.PesAjust.place(x=0,y=185)

		#Eventos para implementar dinamismo en la seleccion de pestañas
		self.PesVerCli.bind('<Enter>',lambda event: self.PesVerCli.config(bg=self.PCFS,fg=self.PCLS))
		self.PesVerCli.bind('<Button-1>',self.SelecPesVerCli)
		self.PesNewCli.bind('<Enter>',lambda event: self.PesNewCli.config(bg=self.PCFS,fg=self.PCLS))
		self.PesNewCli.bind('<Leave>',lambda event: self.PesNewCli.config(bg=self.PCF,fg=self.PCL))
		self.PesNewCli.bind('<Button-1>',self.SelecPesNewCli)
		self.PesDetall.bind('<Enter>',lambda event: self.PesDetall.config(bg=self.PCFS,fg=self.PCLS))
		self.PesDetall.bind('<Leave>',lambda event: self.PesDetall.config(bg=self.PCF,fg=self.PCL))
		self.PesDetall.bind('<Button-1>',self.SelecPesDetall)
		self.PesAjust.bind('<Enter>',lambda event: self.PesAjust.config(bg=self.PCFS,fg=self.PCLS))
		self.PesAjust.bind('<Leave>',lambda event: self.PesAjust.config(bg=self.PCF,fg=self.PCL))
		self.PesAjust.bind('<Button-1>',self.SelecPesAjust)

		Label(FramePes,text='Pulsa F1 para obtener',bg=self.PCF,fg='#B8B8B8').place(x=10,y=345)
		LinkAyuda=Label(FramePes,text="ayuda",fg='#B8B8B8',bg=self.PCF,cursor="hand2")
		LinkAyuda.place(x=126,y=345)
		LinkAyuda.bind("<Button-1>",lambda url:(webbrowser.open_new("http://www.google.com")))

	def Tab_Client_Table(self): #Pestaña para mostrar lista de clientes
		BloqueA1=Frame(self.Pes1,width='712',height='363')
		BloqueA1.pack()

		BloqueA2=Frame(self.Pes1,height='41',width='711')
		BloqueA2.place(x=0,y=327)

		self.CuadroBuscar=ttk.Entry(BloqueA2,foreground='Gray',width=25)
		self.CuadroBuscar.insert(0,'Buscar')
		self.CuadroBuscar.bind("<KeyRelease>",self.BuscarCliente)
		self.CuadroBuscar.bind('<FocusIn>', self.GrisBuscar)
		self.CuadroBuscar.bind('<FocusOut>', self.GrisBuscar)
		self.CuadroBuscar.place(x=20,y=6,height=25)

		ttk.Button(BloqueA2,text='Modificar',style='my.TButton',command=self.CargarCliente).place(x=462,y=6)
		ttk.Button(BloqueA2,text='Eliminar',style='my.TButton',command=self.EliminarCliente).place(x=575,y=6)

		#------------------------Tabla-del-Cliente-------------------------#
		self.TablaCliente =ttk.Treeview(BloqueA1,height=10,columns=("#1","#2","#3","#4"))
		self.TablaCliente.place(x=-5,y=0,width=692)
		self.TablaCliente.heading("#0")
		self.TablaCliente.column("#0",width=35,stretch=0,anchor=W)
		self.TablaCliente.heading("#1", text="N°") 
		self.TablaCliente.column("#1",width=60,stretch=0,anchor=CENTER)
		self.TablaCliente.heading("#2", text="Apellidos y Nombres")
		self.TablaCliente.column("#2",width=300,stretch=0)
		self.TablaCliente.heading("#3", text="Dirección IP")
		self.TablaCliente.column("#3",width=150,stretch=0,anchor=CENTER)
		self.TablaCliente.heading("#4", text="Estado") 
		self.TablaCliente.column("#4",width=145,stretch=0,anchor=CENTER)
		ScrollVertical=ttk.Scrollbar(BloqueA1,command=self.TablaCliente.yview,orient=VERTICAL)
		self.TablaCliente.configure(yscrollcommand=ScrollVertical.set)
		ScrollVertical.place(x=687,y=0,height=327)

		
		self.TablaCliente.tag_configure("LineaBlanca",background='white')
		self.TablaCliente.tag_configure("LineaColor",background='#C9D8F0')
		self.TablaCliente.bind('<Button-1>', self.Click)
		self.TablaCliente.bind('<Button-3>', self.PopupC)
		self.TablaCliente.bind('<Double-Button-1>', self.Cargar2Click)
		self.Orden,self.Vista='OA','Activo'
		self.ConsultarCliente()
		

	def Tab_New_Client(self): #Pestaña para agregar nuevos clientes
		BloqueB1=Frame(self.Pes2,width="712",height="363")
		BloqueB1.pack(fill="both",side=LEFT,expand="yes",ipadx=5,ipady=5)

		Frame(BloqueB1,width=15,height=15).grid(row=0,column=0)
		Label(BloqueB1,text="Registre los datos del nuevo cliente",font=self.ST).grid(row=1,column=1,columnspan=2,pady=10)
		Label(BloqueB1,text="Apellidos y Nombres:",font=self.ST).grid(row=2,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Dirección IP:",font=self.ST).grid(row=3,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Dirección:",font=self.ST).grid(row=4,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Telefono/Celular:",font=self.ST).grid(row=5,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Monto:",font=self.ST).grid(row=6,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Megas:",font=self.ST).grid(row=7,column=1,pady=5,padx=10,sticky="w")
		Label(BloqueB1,text="Fecha de Instalacion:",font=self.ST).grid(row=8,column=1,pady=5,padx=10,sticky="w")

		ttk.Entry(BloqueB1,width=25,font=self.ST,textvariable=self.AN).grid(row=2,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,justify='center',textvariable=self.IP).grid(row=3,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,textvariable=self.Direc).grid(row=4,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,justify='right',textvariable=self.Telef).grid(row=5,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,justify='right',textvariable=self.Monto).grid(row=6,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,justify='right',textvariable=self.Megas).grid(row=7,column=2)
		ttk.Entry(BloqueB1,width=25,font=self.ST,justify='center',textvariable=self.FI).grid(row=8,column=2)
                            
		self.BotRegistrar=ttk.Button(BloqueB1,text='Registrar',style='my.TButton',command=self.RegistrarCliente)
		self.BotRegistrar.place(x=305,y=305,width=115)
		self.BotDeshacer=ttk.Button(BloqueB1,text='Deshacer',style='my.TButton',command=self.Deshacer)
		self.BotDeshacer.place(x=188,y=305,width=115)

		self.BotModificar=ttk.Button(BloqueB1,text="Modificar",style='my.TButton',command=self.ActualizarCliente)
		self.BotCancelar=ttk.Button(BloqueB1,text='Cancelar',style='my.TButton',command=self.Cancelar)
		
	def Tab_Detall(self): #Pestaña para gestionar y mostrar el historial del cliente

		ArregloAge,self.ArregloMes=[],['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
		for i in range(2020,int(date.today().year)+1):
			ArregloAge.append(i)

		self.ComboCliente=ttk.Combobox(self.Pes3,width=20,state='readonly',font=self.ST)
		self.ComboCliente.place(x=25,y=25)
		self.ComboCliente.bind("<<ComboboxSelected>>", self.DesPagoMes)
		self.ComboCliente.set('Seleccione cliente')

		Label(self.Pes3,text="Año",font=self.ST).place(x=25,y=65)
		self.ComboAge=ttk.Combobox(self.Pes3,width=10,values=ArregloAge,state='readonly',font=self.ST)
		self.ComboAge.place(x=80,y=65)
		self.ComboAge.bind("<<ComboboxSelected>>", lambda event: (self.Pago.set(''),self.Fecha.set('')))
		
		self.CargarCombo()

		Label(self.Pes3,text="Mes",font=self.ST).place(x=25,y=105)

		self.ComboMes=ttk.Combobox(self.Pes3,width=10,values=self.ArregloMes,state='readonly',font=self.ST)
		self.ComboMes.place(x=80,y=105)
		self.ComboMes.bind("<<ComboboxSelected>>", lambda event: (self.Pago.set(''),self.Fecha.set('')))

		ttk.Button(self.Pes3,text='Generar',style='my.TButton',command=self.CargarPagoMes).place(x=79,y=143,width=116)

		Label(self.Pes3,text="Pago",font=self.ST).place(x=25,y=185)
		Label(self.Pes3,text="Fecha",font=self.ST).place(x=25,y=225)
		ttk.Entry(self.Pes3,justify='right',font=self.ST,width=12,textvariable=self.Pago).place(x=80,y=185)
		ttk.Entry(self.Pes3,justify='center',font=self.ST,width=12,textvariable=self.Fecha).place(x=80,y=225)

		ttk.Button(self.Pes3,text='Actualizar',style='my.TButton',command=self.ActualizarPagoMes).place(x=79,y=265,width=116)

		self.TablaHistorial =ttk.Treeview(self.Pes3,height=9,columns=("#1","#2","#3","#4"))
		self.TablaHistorial.place(x=250,y=25,width=375)
		self.TablaHistorial.heading("#0", text='')
		self.TablaHistorial.column("#0",width=0,stretch=0)
		self.TablaHistorial.heading("#1", text='N°')
		self.TablaHistorial.column("#1",width=50,stretch=0,anchor=CENTER)
		self.TablaHistorial.heading("#2", text="Acción")
		self.TablaHistorial.column("#2",width=153,stretch=0)
		self.TablaHistorial.heading("#3", text="Fecha")
		self.TablaHistorial.column("#3",width=100,stretch=0,anchor=CENTER)
		self.TablaHistorial.heading("#4", text="Monto") 
		self.TablaHistorial.column("#4",width=70,stretch=0,anchor=CENTER)
		ScrollVertical=ttk.Scrollbar(self.Pes3,command=self.TablaHistorial.yview,orient=VERTICAL)
		self.TablaHistorial.configure(yscrollcommand=ScrollVertical.set)
		ScrollVertical.place(x=665,y=25,height=150)

		self.TablaHistorial.bind('<Button-3>', self.PopupH)
		self.TablaHistorial.bind('<Button-1>', self.Click)
		self.TablaHistorial.tag_configure("LineaBlanca",background='white')
		self.TablaHistorial.tag_configure("LineaColor",background='#C9D8F0')
	

		##------------------------------Pestaña 4------------------------------------------#
		self.Pestana.bind("<<NotebookTabChanged>>",self.Desseleccionar)
