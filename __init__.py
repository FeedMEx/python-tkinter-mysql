#!/usr/bin/env python

"""Modulo principal para ejecutar el programa"""

from Interfaz import *

class MainApp(Frame,Main_Window,Functionality):

	def __init__(self, Window , *args , **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.User=StringVar() #Variable string para el cuadro de texto usuario
		self.Password=StringVar() #Variable string para el cuadro de texto contraseña
		self.Create_Window_Login(Window) #Ejecutar la creacion de la ventana login
			
	def Create_Main_Window(self):
		Privilege_Value=self.Privilege_Value #Almacenar el valor de privilegio del usuario
		Default=self.Default #Almacenar el nombre de usuario
		window=Tk() #Ventana principal
		Main_Window(window)
		window.mainloop()

if __name__=="__main__":
	window=Tk() #Ventana login
	MainApp(window)
	window.mainloop()