print("Hola")

#arreglo
nombres = ["Fernando", "Ana", "Maria", "Jose"]

print('Soy un arreglo: ',nombres)

cursos = ["octavo", "noveno", "decimo"]

#diccinarios
#diccionario con mismo tipo de dato
diccionario = {'clave':'valor', 'triangulo':'figura geometrica de 3 lados'}

print('Soy un diccionario: ', diccionario)

#get obtenemos el valor dentro del diccionario pasando como parametro su clave
print(diccionario.get('triangulo'))


#diccionario con diferentes tipos de datos
diccionario1 = {'clave':'valor', 'nombre':'Fernando', 'apellido':'Cusco', 'edad':23, 'peso':110.2, 'estado':False}
print(diccionario1.keys())
print(diccionario1.values())



#sentencias de control

#if
edad = 45
peso = 10
nivelMedicina = "Cantidad sugerida 50%"

if edad > 18 and peso < 100:
	nivelMedicina = "Cantidad sugerida 25%"

else:
	if edad < 18 and peso < 65:
		nivelMedicina = "Cantidad sugerida 10-15%"

print(nivelMedicina)


#ciclos

contador = 0
tm = 0
while(contador < 11):
	tm = 5 * contador
	print('5 * ',contador, '=',tm)
	contador+=1









