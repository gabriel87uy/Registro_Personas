from Tkinter import *
import string, pickle

registro=[]

class gui:
	def __init__(self, marco):
		self.marco=marco
		frame=Frame(marco)
		frame.pack()

		marco.geometry('280x200')
		marco.title('registro 0.1c')
		nombre_etiqueta=Label(frame, text='Nombre:').grid(row=0)
		direc_etiqueta=Label(frame, text='Direccion:').grid(row=1)
		tel_etiqueta=Label(frame, text='Telefono:').grid(row=2)
		cedula_etiqueta=Label(frame, text='Cedula:').grid(row=3)

		empty_line=Label(frame).grid(row=4)

		self.nombre_var=StringVar()
		nombre=Entry(frame, textvariable=self.nombre_var, width=32).grid(row=0, column=1)

		self.direc_var=StringVar()
		direc=Entry(frame, textvariable=self.direc_var, width=32).grid(row=1, column=1)
	
		self.tel_var=StringVar()
		tel=Entry(frame, textvariable=self.tel_var, width=32).grid(row=2, column=1)

		self.cedula_var=StringVar()
		cedula=Entry(frame, textvariable=self.cedula_var, width=32).grid(row=3, column=1)

		boton_1=Button(frame, text='Guardar', command=registrar, width=16, fg='blue').grid(row=5, column=1)
		boton_2=Button(frame, text='Buscador', command=self.buscador, width=16, fg='green').grid(row=6, column=1)
	
	def buscador(self): #revisar, no toma entrada
		def pasos():
			archivo=open('registro.pck', 'r')
			lista=pickle.load(archivo)
			archivo.close()
#			lista=registro_temporal
			a=filtrar(self.cedula_buscar)
			encontrado=False
			for n in range(len(lista)):
				if lista[n]['Cedula']==a.get():
					encontrado=True
					lugar=n
					break
			if encontrado:
				print lista[lugar]['Nombre']
				self.datos.set(lista[lugar]['Nombre'])
				print self.etiqueta.get() + '2'
			
			else:
				print 'no existe'
			print a.get()
		
		ventana_buscar=Tk()
#		frame_2=Frame(ventana_buscar)
#		frame_2.pack()
		ventana_buscar.title('buscando')
		self.etiqueta=StringVar()
#		self.etiqueta.set('hola')
		self.datos=Label(ventana_buscar, textvariable=self.etiqueta , height=4)
		self.datos.grid(row=0)
		
		self.cedula_buscar=Entry(ventana_buscar, width=32)
		self.cedula_buscar.grid(row=1, column=1)
		boton=Button(ventana_buscar, text='Buscar', command=pasos)
		boton.grid(row=2, column=1)
		
		ventana_buscar.mainloop()

archivo_creado=False

while not archivo_creado:
	try:
		archivo=open('registro.pck', 'r')
		lista_temporal=pickle.load(archivo)
		registro=lista_temporal
		archivo.close()
		archivo_creado=True
	except:
		lista_temporal=[]
		archivo=open('registro.pck', 'w')
		pickle.dump(lista_temporal, archivo)
		archivo.close()
		archivo_creado=False
                
def registrar():
	datos_persona={}
	cedula=filtrar(ventana.cedula_var)
	items=('Nombre', 'Direccion', 'Telefono', 'Cedula')
	values=(ventana.nombre_var, ventana.direc_var, ventana.tel_var, cedula)
	for n in range(len(items)):
		datos_persona[items[n]]=values[n].get()
	registro.append(datos_persona)
	archivo=open('registro.pck', 'w')
	pickle.dump(registro, archivo)
	archivo.close()
	
	print datos_persona #auxiliar
	archivo=open('registro.pck', 'r')
	lista=pickle.load(archivo)
	archivo.close()
	print lista
	
def filtrar(documento):
	c=StringVar()
	a=documento.get()
	lista=list(a)
	b=0
	for n in lista:
		if n<chr(48) or n>chr(57):
			lista.remove(lista[b])
		b+=1
	salida=string.join(lista,'')
	c.set(salida)
	return c

def buscar(documento):
	cedula=documento.get()
	for i in range(len(registro)):
		if registro[i]['Cedula']==cedula:
			ventana.nombre.set(registro[i]['Nombre'])
			break
#	return 'no encontrado'

root=Tk()
ventana=gui(root)
root.mainloop()
