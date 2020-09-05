
"""Modulo para Conectarse a la base de datos"""

import mysql.connector
from mysql.connector import errorcode
import mysql.connector.locales.eng.client_error

class Connection:

	def Connect(self):
		try:
			connection=mysql.connector.connect(
				user='root', #nombre de usuario
				host='127.0.0.1',
				password='', #Contraseña de acceso a mysql
				database='internet') #Nombre de la base de datos
			return connection
	
		except mysql.connector.Error as err:

			if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
				self.MensajeError='Error_User'

			elif err.errno==errorcode.ER_BAD_DB_ERROR:
				self.MensajeError='Error_DB'

			else:
				self.MensajeError='Error_unknown'

	def CloseConnection(self,connection):
		connection.close()



