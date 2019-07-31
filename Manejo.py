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
