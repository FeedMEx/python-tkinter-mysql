
"""Modulo para gestionar consultas a la base de datos"""

from Conection import *

class Data(Connection):

	def RegistrarCliente(self,AN,IP,Direc,Telef,Monto,Megas,FI):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL registrar_cliente (null,'{}','{}','{}','{}','{}','{}','{}')".format(AN,IP,Direc,Telef,Monto,Megas,FI))
		cnx.commit()
		self.CloseConnection(cnx)

	def ActualizarCliente(self,N,AN,IP,Direc,Telef,Monto,Megas,FI):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL actualizar_cliente ('{}','{}','{}','{}','{}','{}','{}','{}')".format(N,AN,IP,Direc,Telef,Monto,Megas,FI))
		cnx.commit()
		self.CloseConnection(cnx)

	def ActualizarEstado(self,N,Estado):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL actualizar_estado ('{}','{}')".format(N,Estado))
		cnx.commit()
		self.CloseConnection(cnx)

	def RegistrarPagoMes(self,Age,ID):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL registrar_pagomes ('{}','{}')".format(Age,ID))
		cnx.commit()
		self.CloseConnection(cnx)

	def ActualizarPagoMes(self,ID,Age,Mes,Pago,Fecha):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL actualizar_pagomes ('{}','{}','{}','{}','{}')".format(ID,Age,Mes,Pago,Fecha))
		cnx.commit()
		self.CloseConnection(cnx)

	def RegistrarHistorial(self,Accion,Fecha,Monto,ID):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL registrar_historial ('{}','{}','{}','{}')".format(Accion,Fecha,Monto,ID))
		cnx.commit()
		self.CloseConnection(cnx)

	def ActualizarHistorial(self,N,Accion,Fecha,Monto):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL actualizar_historial ('{}','{}','{}','{}')".format(N,Accion,Fecha,Monto))
		cnx.commit()
		self.CloseConnection(cnx)

	def ActualizarFIH(self,ID,Accion,Fecha):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL actualizar_fih ('{}','{}','{}')".format(ID,Accion,Fecha))
		cnx.commit()
		self.CloseConnection(cnx)

	def ConsultarHistorial(self,ID):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL consultar_historial('{}')".format(ID))
		Lista=Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def CargarHistorial(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL cargar_historial ('{}')".format(N))
		Lista=Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def EliminarHistorial(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL eliminar_historial ('{}')".format(N))
		cnx.commit()
		self.CloseConnection(cnx)

	def EliminarPagoMes(self,ID):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL eliminar_pagomes ('{}')".format(ID))
		cnx.commit()
		self.CloseConnection(cnx)

	def CargarPagoMes(self,ID,Age,Mes):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL cargar_pagomes ('{}','{}','{}')".format(ID,Age,Mes))
		Lista=Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def CargarXAN(self,AN):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL cargar_xan ('{}')".format(AN))
		Lista=Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def EliminarCliente(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL eliminar_cliente ('{}')".format(N))
		cnx.commit()
		self.CloseConnection(cnx)

	def CargarCliente(self,N):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL cargar_cliente ('{}')".format(N))
		Lista = Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def ConsultarCliente(self,Orden,Vista):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL consultar_cliente ('{}','{}')".format(Orden,Vista))
		Lista = Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def BuscarCliente(self,Cadena,Orden,Vista):
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL buscar_cliente ('{}%','{}','{}')".format(Cadena,Orden,Vista))
		Lista=Cursor.fetchall()
		self.CloseConnection(cnx)
		return Lista

	def RelacionarCliente(self): #Obtener el numero de clientes registrados en la base de datos
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("CALL relacionar_cliente ()")
		Lista=Cursor.fetchall()
		Arreglo=[]
		for dato in Lista:
			Arreglo=dato[0]
		self.CloseConnection(cnx)
		return Arreglo

class Usuario(Connection):

	def Consultar(self,User,Pass): #Consultar Usuario y contraseña de la base de datos
		try:
			cnx=self.Connect()
			Cursor=cnx.cursor()
			Cursor.execute("SELECT * FROM login WHERE Usuario='{}' AND Contra='{}'".format(User,Pass))
			for login in Cursor:
				if login[1]==User and login[2]==Pass:
					self.CloseConnection(cnx)
					return True
			self.CloseConnection(cnx)
			return False

		except AttributeError:
			return str(self.MensajeError)

	def CambiarLogin(self,Pass): #Cambiar contraseña de usuario
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("UPDATE login SET Contra='{}' WHERE Usuario='admin'".format(Pass))
		cnx.commit()
		self.CloseConnection(cnx)

	def ValidarContra(self,Pass): #Validar contraseña actual para el cambio de contraseña nueva
		cnx=self.Connect()
		Cursor=cnx.cursor()
		Cursor.execute("SELECT * FROM login WHERE Usuario='admin' AND Contra='{}'".format(Pass))
		for login in Cursor:
			if login[2]==Pass:
				self.CloseConnection(cnx)
				return True
		self.CloseConnection(cnx)
		return False
