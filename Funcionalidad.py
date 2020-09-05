
"""En este modulo se implementa las diferentes funcionalidades del programa"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from BaseDatos import *
from tkinter import filedialog
from datetime import date,datetime
from Autenticador import *
import webbrowser
from PIL import Image, ImageTk

class Functionality(Autenticar):

	def Access(self,event): #Metodo para validar usuario y contraseña
		Obj=Usuario()
		Validar=Obj.Consultar(self.User.get(),self.Password.get())

		if Validar:
			self.Default=self.User.get()
			self.WindowLogin.destroy()
			self.Create_Main_Window()

		elif Validar=='Error_User':
			messagebox.showwarning('Mensaje','Error de contraseña de la base de datos')

		elif Validar=='Error_DB':
			messagebox.showwarning('Mensaje','La base de datos no existe')

		elif Validar=='Error_unknown':
			messagebox.showwarning('Mensaje','Se negó la conexion con la base de datos, consulte con el administrador')

		else:
			messagebox.showinfo("Mensaje","Login Incorrecto")
			self.CuadroUser.delete(0,END)
			self.CuadroPass.delete(0,END)
			self.CuadroUser.focus()

	def MostrarContrasena(self):
		if self.MostrarContra.get()==1:
			self.CajaContra.config(show="")
		else:
			self.CajaContra.config(show="•")

	def CambiarContra(self):
		Datos=Usuario()
		Validar=Datos.ValidarContra(self.ContraActual.get())

		if Validar:
			if len(self.ContraNueva.get())>=8:
				Cambiar=Datos.CambiarLogin(self.ContraNueva.get())
				messagebox.showinfo("Mensaje","La contraseña ha sido modificada con éxito")
				self.ContraActual.set("")
				self.ContraNueva.set("")
				self.MostrarContra.set(0)
			else:
				messagebox.showwarning("Mensaje",'La contraseña nueva debe contener como mímino 8 carácteres')
				self.CajaContra.focus()
				self.ContraNueva.set("")
		else:
			messagebox.showinfo("Mensaje","La contraseña actual es incorrecta")
			self.ContraActual.set("")
			self.ContraNueva.set("")
			self.CuadroActual.focus()

	def SelecPesVerCli(self,event): #Seleccionar la pestaña ver cliente
		self.Pestana.select(self.Pes1)
		self.PesVerCli.config(bg=self.PCFS,fg=self.PCLS)
		self.PesNewCli.config(bg=self.PCF,fg=self.PCL)
		self.PesDetall.config(bg=self.PCF,fg=self.PCL)
		self.PesAjust.config(bg=self.PCF,fg=self.PCL)
		self.PesVerCli.bind('<Leave>',lambda event: self.PesVerCli.config(bg=self.PCFS,fg=self.PCLS))
		self.PesNewCli.bind('<Leave>',lambda event: self.PesNewCli.config(bg=self.PCF,fg=self.PCL))
		self.PesDetall.bind('<Leave>',lambda event: self.PesDetall.config(bg=self.PCF,fg=self.PCL))
		self.PesAjust.bind('<Leave>',lambda event: self.PesAjust.config(bg=self.PCF,fg=self.PCL))

	def SelecPesNewCli(self,event):  #Seleccionar la pestaña nuevo clienete
		self.Pestana.select(self.Pes2)
		self.PesVerCli.config(bg=self.PCF,fg=self.PCL)
		self.PesNewCli.config(bg=self.PCFS,fg=self.PCLS)
		self.PesDetall.config(bg=self.PCF,fg=self.PCL)
		self.PesAjust.config(bg=self.PCF,fg=self.PCL)
		self.PesVerCli.bind('<Leave>',lambda event: self.PesVerCli.config(bg=self.PCF,fg=self.PCL))
		self.PesNewCli.bind('<Leave>',lambda event: self.PesNewCli.config(bg=self.PCFS,fg=self.PCLS))
		self.PesDetall.bind('<Leave>',lambda event: self.PesDetall.config(bg=self.PCF,fg=self.PCL))
		self.PesAjust.bind('<Leave>',lambda event: self.PesAjust.config(bg=self.PCF,fg=self.PCL))

	def SelecPesDetall(self,event):  #Seleccionar la pestaña Detalles
		self.Pestana.select(self.Pes3)
		self.PesVerCli.config(bg=self.PCF,fg=self.PCL)
		self.PesNewCli.config(bg=self.PCF,fg=self.PCL)
		self.PesDetall.config(bg=self.PCFS,fg=self.PCLS)
		self.PesAjust.config(bg=self.PCF,fg=self.PCL)
		self.PesVerCli.bind('<Leave>',lambda event: self.PesVerCli.config(bg=self.PCF,fg=self.PCL))
		self.PesNewCli.bind('<Leave>',lambda event: self.PesNewCli.config(bg=self.PCF,fg=self.PCL))
		self.PesDetall.bind('<Leave>',lambda event: self.PesDetall.config(bg=self.PCFS,fg=self.PCLS))
		self.PesAjust.bind('<Leave>',lambda event: self.PesAjust.config(bg=self.PCF,fg=self.PCL))

	def SelecPesAjust(self,event):  #Seleccionar la pestaña Ajustes
		self.Pestana.select(self.Pes4)
		self.PesVerCli.config(bg=self.PCF,fg=self.PCL)
		self.PesNewCli.config(bg=self.PCF,fg=self.PCL)
		self.PesDetall.config(bg=self.PCF,fg=self.PCL)
		self.PesAjust.config(bg=self.PCFS,fg=self.PCLS)
		self.PesVerCli.bind('<Leave>',lambda event: self.PesVerCli.config(bg=self.PCF,fg=self.PCL))
		self.PesNewCli.bind('<Leave>',lambda event: self.PesNewCli.config(bg=self.PCF,fg=self.PCL))
		self.PesDetall.bind('<Leave>',lambda event: self.PesDetall.config(bg=self.PCF,fg=self.PCL))
		self.PesAjust.bind('<Leave>',lambda event: self.PesAjust.config(bg=self.PCFS,fg=self.PCLS))

	def GrisBuscar(self,event):  #Implementar dinamismo al cuadro de buscar
		if self.CuadroBuscar.get()=="Buscar":
			self.CuadroBuscar.delete(0, END)
			self.CuadroBuscar.config(foreground = 'black')
		
		elif self.CuadroBuscar.get() == "":
			self.CuadroBuscar.insert(0,"Buscar")
			self.CuadroBuscar.config(foreground = 'gray')


	def RegistrarCliente(self):
		self.Datos.RegistrarCliente(self.AN.get().upper(),self.IP.get(),self.Direc.get().upper(),self.Telef.get(),self.Monto.get(),self.Megas.get(),self.FI.get())
		self.ConsultarCliente()
		ID,Age=str(self.Datos.RelacionarCliente()),str(date.today().year)
		self.CargarCombo(),self.Datos.RegistrarPagoMes(Age,ID),self.Datos.RegistrarHistorial('Instalación',self.FI.get(),'',ID),self.ConsultarHistorial()
		messagebox.showinfo("Mensaje","El cliente ah sido registrado con éxito")
		self.Deshacer()

	def CargarCombo(self): #Cargar registros al Combobox
		Arreglo=self.Datos.ConsultarCliente('OA','Activo')
		Lista=[]
		for i in Arreglo:
			Lista.append(i[1])
		self.ComboCliente.config(values=Lista)
		

	def EliminarCliente(self):
		try:
			if self.TablaCliente.item(self.TablaCliente.selection())["values"]:
				Valor=messagebox.askquestion("Eliminar","¿Desea eliminar este registro?")
				if Valor=="yes":
					self.Datos.EliminarCliente(self.NValor)
					self.Datos.EliminarPagoMes(self.NValor)
					self.ConsultarCliente()
					messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')
					self.CargarCombo()
			else:
				messagebox.showinfo('Mensaje','Ningún registro seleccionado')
		except TclError:
			messagebox.showwarning('Mensaje','Seleccione un solo registro')

	def CargarCliente(self):
		try:
			if self.TablaCliente.item(self.TablaCliente.selection())["values"]:
				self.SelecPesNewCli(self.PesNewCli)

				self.BotRegistrar.place(x=2000,y=350)
				self.BotDeshacer.place(x=2000,y=350)
				self.BotModificar.place(x=305,y=305,width=115)
				self.BotCancelar.place(x=188,y=305,width=115)
				
				self.NValor=str(self.TablaCliente.item(self.TablaCliente.selection())["text"])
				Lista=self.Datos.CargarCliente(self.NValor)

				for i in Lista:
					self.AN.set(i[1])
					self.IP.set(i[2])
					self.Direc.set(i[3])
					self.Telef.set(i[4])
					self.Monto.set(i[5])
					self.Megas.set(i[6])
					self.FI.set(i[7])

			else:
				messagebox.showinfo('Mensaje','Ningún registro seleccionado')

		except TclError:
			messagebox.showwarning('Mensaje','Seleccione un solo registro')

	def BuscarCliente(self,Key):
		if self.CuadroBuscar.get()=='':
			self.ConsultarCliente()
		else:
			Tabla,Arreglo,cont=self.TablaCliente.get_children(),self.Datos.BuscarCliente(self.CuadroBuscar.get(),self.Orden,self.Vista),1
			for elemento in Tabla:
				self.TablaCliente.delete(elemento)		
			for row in Arreglo:
				if cont % 2 != 0:
					if row[8]=='Activo':
						self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenVerde,values=(cont,row[1],row[2], row[8]), tags=('LineaBlanco'))
					else:
						self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenNegro,values=(cont,row[1],row[2], row[8]), tags=('LineaBlanco'))
				elif cont % 2 == 0:
					if row[8]=='Activo':
						self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenVerde,values=(cont,row[1],row[2], row[8]), tags=('LineaColor'))
					else:
						self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenNegro,values=(cont,row[1],row[2], row[8]), tags=('LineaColor'))
				cont=cont+1


	def ActualizarCliente(self):

		self.Datos.ActualizarCliente(self.NValor,self.AN.get().upper(),self.IP.get(),self.Direc.get().upper(),self.Telef.get(),self.Monto.get(),self.Megas.get(),self.FI.get())
		messagebox.showinfo('Mensaje','El registro ha sido actualizado con éxito')
		self.ConsultarCliente(),self.SelecPesVerCli(self.PesVerCli),self.Datos.ActualizarFIH(self.NValor,'Instalación',self.FI.get())
		
		self.BotModificar.place(x=2000,y=350)
		self.BotCancelar.place(x=2000,y=350)
		self.BotRegistrar.place(x=305,y=305)
		self.BotDeshacer.place(x=188,y=305)
		self.CargarCombo(),self.Deshacer()

	def ActualizarEstado(self,Top,Fecha):
		self.Datos.ActualizarEstado(self.NValor,self.Estado)
		self.ConsultarCliente()
		Top.destroy()
		datos=self.Datos.CargarCliente(self.NValor)
		for e in datos:
			self.Estado=e[8]
		accion='Corte'
		if self.Estado=='Activo':
			accion='ReInstalado'
		self.Datos.RegistrarHistorial(accion,Fecha,'',self.NValor),self.ConsultarHistorial()

	def Deshacer(self): #Limpiar los cuadros de texto en la pestaña de nuevo cliente
		now = datetime.now()
		self.AN.set(''),self.Direc.set(''),self.IP.set(''),self.Telef.set(''),self.Monto.set(''),self.Megas.set('Mbps'),self.FI.set(now.strftime('%d-%m-%Y')),self.IP.set('192.168.')

	def DesPagoMes(self,event): #Limpiar los cuadros de texto en la pestaña detalles
		month = self.ArregloMes[date.today().month - 2]
		self.Pago.set(''),self.Fecha.set(''),self.ComboAge.set(date.today().year),self.ComboMes.set(month)
		Lista=self.Datos.CargarXAN(self.ComboCliente.get())
		for i in Lista:
			self.NValor=str(i[0])
		self.ConsultarHistorial()

	def Cancelar(self): #cancelar cambios en la actualizacion de datos
		Valor=messagebox.askquestion("Cancelar","¿Desea cancelar la operación?")
		if Valor=="yes":
			self.SelecPesVerCli(self.PesVerCli)
			self.Deshacer()
			self.BotModificar.place(x=2000,y=6,height=25)
			self.BotCancelar.place(x=2000,y=6,height=25)
			self.BotRegistrar.place(x=305,y=305,height=25)
			self.BotDeshacer.place(x=188,y=305,height=25)

	def Click(self,event): #Restringir el redimensionamiento de las columnas de la tabla
		if self.TablaCliente.identify_region(event.x, event.y) == "separator":
			return "break"

		elif self.TablaHistorial.identify_region(event.x, event.y) == "separator":
			return "break"

	def CambiarOrden(self): #Cambiar el orden en el que se muestra los clientes
		if self.ValorOrden.get()==0:
			self.Orden='OA'
		elif self.ValorOrden.get()==1:
			self.Orden='IP'
		self.ConsultarCliente()

	def CambiarVista(self): 
		if self.ValorVista.get()==0:
			self.Vista='Activo'
		elif self.ValorVista.get()==1:
			self.Vista='All'
		elif self.ValorVista.get()==2:
			self.Vista='Inactivo'
		elif self.ValorVista.get()==2:
			self.Vista='Deuda'
		self.ConsultarCliente()
    
	def ConsultarCliente(self): #Mostrar los clientes en la tabla
		Tabla,Arreglo,cont=self.TablaCliente.get_children(),self.Datos.ConsultarCliente(self.Orden,self.Vista),1
		for elemento in Tabla:
			self.TablaCliente.delete(elemento)		
		for row in Arreglo:
			if cont % 2 != 0:
				if row[8]=='Activo':
					self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenVerde,values=(cont,row[1],row[2], row[8]), tags=('LineaBlanco'))
				else:
					self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenNegro,values=(cont,row[1],row[2], row[8]), tags=('LineaBlanco'))
			elif cont % 2 == 0:
				if row[8]=='Activo':
					self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenVerde,values=(cont,row[1],row[2], row[8]), tags=('LineaColor'))
				else:
					self.TablaCliente.insert("",index="end",text=row[0],image=self.ImagenNegro,values=(cont,row[1],row[2], row[8]), tags=('LineaColor'))
			cont=cont+1

	def CargarAgeMes(self): #Mostrar el año y mes actual
		month = self.ArregloMes[date.today().month - 2]
		self.ComboAge.set(date.today().year)
		self.ComboMes.set(month)

	def Cargar2Click(self,event): #Realizar dos click en el cliente para ver los detalles
		self.SelecPesDetall(self.PesDetall)
		self.NValor=str(self.TablaCliente.item(self.TablaCliente.selection())["text"])
		for e in self.Datos.CargarCliente(self.NValor):
			Name=e[1]
		self.ComboCliente.set(Name),self.ConsultarHistorial()
		

	def CargarPagoMes(self): #Mostrar el monto a pagar o pagado por el cliente
		if self.ComboCliente.get()!='Seleccione cliente':
			now = datetime.now()
			Lista=self.Datos.CargarXAN(self.ComboCliente.get())
			for i in Lista:
				self.NValor=str(i[0])

			Lista1,Lista2=self.Datos.CargarPagoMes(self.NValor,self.ComboAge.get(),self.ComboMes.get()),self.Datos.CargarCliente(self.NValor)
			for i in Lista1:
				Pago=i[3]
				Fecha=i[4]
			
			if Pago=='0':
				for i in Lista2:
					self.Pago.set(i[5])
				self.Fecha.set(now.strftime('%d-%m-%Y'))
			else:
				self.Pago.set(Pago)
				self.Fecha.set(Fecha)
		else:
			messagebox.showwarning('Mensaje','Seleccione cliente')

	def ActualizarPagoMes(self): #Registrar nuevo pago del cliente
		if self.ComboCliente.get()!='Seleccione cliente':
			if self.ValidarDigitos(self.Pago.get()):
				self.Datos.ActualizarPagoMes(self.NValor,self.ComboAge.get(),self.ComboMes.get(),self.Pago.get(),self.Fecha.get())
				messagebox.showinfo('Mensaje','El pago ah sido actualizado con éxito')
				self.Datos.RegistrarHistorial('Pago {}'.format(self.ComboMes.get()),self.Fecha.get(),self.Pago.get(),self.NValor)
				self.ConsultarHistorial()
			else:
				messagebox.showwarning('Mensaje','Error en el cuadro "pago"')
		else:
			messagebox.showwarning('Mensaje','Seleccione cliente')

	def ActualizarHistorial(self,Top):	
		self.Datos.ActualizarHistorial(self.NValorH,self.Accion.get(),self.FH.get(),self.PH.get())
		messagebox.showinfo('Mensaje','El registro ah sido modificado con éxito')
		self.ConsultarHistorial(),Top.destroy()
		
	def EliminarHistorial(self):
		NValorH=str(self.TablaHistorial.item(self.TablaHistorial.selection())['values'][0])
		if NValorH=='1':
			messagebox.showwarning('Mensaje','No se puede eliminar este registro desde esta sección')
		else:
			Valor=messagebox.askquestion('Mensaje','¿Desea eliminar este registro?')
			if Valor=='yes':
				self.Datos.EliminarHistorial(self.NValorH)
				messagebox.showinfo('Mensaje','El registro ha sido eliminado con éxito')
			self.ConsultarHistorial()

	def ConsultarHistorial(self): #Mostrar el historial de cada cliente en la tabla de historial
		try:
			Tabla,Arreglo,cont=self.TablaHistorial.get_children(),self.Datos.ConsultarHistorial(self.NValor),1
			for elemento in Tabla:
				self.TablaHistorial.delete(elemento)		
			for row in Arreglo:
				if cont % 2 != 0:				
					self.TablaHistorial.insert("",index="end",text=row[0],values=(cont,row[1],row[2], row[3]), tags=('LineaBlanco'))
				elif cont % 2 == 0:
					self.TablaHistorial.insert("",index="end",text=row[0],values=(cont,row[1],row[2], row[3]), tags=('LineaColor'))
				cont=cont+1
		except AttributeError:
			pass

	def PopupC(self, event): #Realizar click derecho en el cliente para mas opciones
		try:
			if  self.TablaCliente.item(self.TablaCliente.selection())["values"]:
				self.NValor=str(self.TablaCliente.item(self.TablaCliente.selection())["text"])
				self.MenuRightClick(self.WindowMain)
				self.ClickMenu.post(event.x_root, event.y_root)
			else:
				self.MenuClickNull(self.WindowMain)
				self.MenuNull.post(event.x_root, event.y_root)
		
		except TclError:
			messagebox.showwarning('Mensaje','Seleccione solo un registro')

	def PopupH(self, event): #Realizar click derecho en la tabla de clientes para mas opciones
		if  self.TablaHistorial.item(self.TablaHistorial.selection())["values"]:
			self.NValorH=str(self.TablaHistorial.item(self.TablaHistorial.selection())["text"])
			self.MenuHistorial(self.WindowMain)
			self.ClickMenu2.post(event.x_root, event.y_root)

	def MenuClickNull(self, window): #Mostrarme mas opciones al presionar click derecho en la tabla de clientes
		
		self.MenuNull = Menu(window, tearoff=0)
		self.MenuOrdenar=Menu(self.WindowMain)
		self.MenuVer=Menu(self.WindowMain)
		
		self.MenuVer=Menu(self.MenuNull,tearoff=0)
		self.MenuOrdenar=Menu(self.MenuNull,tearoff=0)

		self.MenuVer.add_radiobutton(label='Solo clientes activos',variable=self.ValorVista,value=0,command=self.CambiarVista)
		self.MenuVer.add_radiobutton(label='Todos los clientes',variable=self.ValorVista,value=1,command=self.CambiarVista)
		self.MenuVer.add_radiobutton(label='Solo clientes inactivos',variable=self.ValorVista,value=2,command=self.CambiarVista)
		self.MenuVer.add_radiobutton(label='Clientes deudores',variable=self.ValorVista,value=3,command=self.CambiarVista)

		self.MenuOrdenar.add_radiobutton(label='Orden Alfabético',variable=self.ValorOrden,value=0,command=self.CambiarOrden)
		self.MenuOrdenar.add_radiobutton(label='Dirección IP',variable=self.ValorOrden,value=1,command=self.CambiarOrden)

		self.MenuNull.add_cascade(label='Ver', menu=self.MenuVer)
		self.MenuNull.add_cascade(label='Ordenar por   ',menu=self.MenuOrdenar)

	def MenuRightClick(self, window): #Mostrarme mas opciones al presionar click derecho en el cliente
		datos=self.Datos.CargarCliente(self.NValor)
		for e in datos:
			self.Estado=e[8]
		estado='Activar'
		if self.Estado=='Activo':
			estado='Cortar'

		self.ClickMenu = Menu(window, tearoff=0)
		self.ClickMenu.add_command(label='Ver datos          ',command=lambda: self.TopDatos(self.NValor))
		self.ClickMenu.add_command(label='Ver Historial de pago',command=lambda: self.Cargar2Click(self.TablaCliente))
		self.ClickMenu.add_command(label='Modificar registro',command=self.CargarCliente)
		self.ClickMenu.add_command(label='Eliminar registro', command=self.EliminarCliente)
		self.ClickMenu.add_command(label=estado,command=self.EscribirFecha)

	def MenuHistorial(self,window): #Mostrarme mas opciones al presionar click derecho en un registro de la tabla historial
		self.ClickMenu2 = Menu(window, tearoff=0)
		self.ClickMenu2.add_command(label='Modificar          ',command=self.TopHistorial)
		self.ClickMenu2.add_command(label='Eliminar',command=self.EliminarHistorial)

	def Desseleccionar(self,event): #Anulacion de alguna seleccion de registro automatico al cambiar de pestaña
		if len(self.TablaCliente.selection()) > 0:
   		    self.TablaCliente.selection_remove(self.TablaCliente.selection()[0])
		
		elif len(self.TablaHistorial.selection()) > 0:
		    self.TablaHistorial.selection_remove(self.TablaHistorial.selection()[0])

