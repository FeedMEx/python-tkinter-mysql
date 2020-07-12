
"""En este modulo se implementa metodos de validación de datos"""

class Autenticar():	

	def ValidarCliente(self): #validar datos del cliente
		return len(self.AN.get())!=0 and len(self.IP.get())!=0 and len(self.Direc.get())!=0 and len(self.Monto.get())!=0 and len(self.FI.get())!=0

	def ValidarDigitos(self,A): #valivar montos, pagos, etc
		Valor=A
		Punto=0
		ParteDecimal=0
		ParteEntera=0
		for i in Valor:
			if i==".":
				Punto=1
			else:
				if Punto==0:
					ParteEntera=ParteEntera+1
				else:
					ParteDecimal=ParteDecimal+1
		if ParteEntera<=4 and ParteDecimal<=2 and self.ValidarMulta(A):
			return True
		else:
			return False

	def ValidarMulta(self,A): 
		try:
			float(A)
			return True
		except:
			return False
	
#Hace falta crear mas metodos de validación de datos para minimizar bugs


