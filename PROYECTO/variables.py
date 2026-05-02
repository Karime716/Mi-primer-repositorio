#Esto es un comentario de una sola linea
"""Esto es un comentario 
de varias lienes"""

#inicializando variables
nombre="Karime Diaz Lopez"
edad=13
estado=True
nota=5.0

#mostrar el contenido de las variables print ()
print(nombre)
print(edad)
print(estado)
print(nota)

#Que tipo de dato contiene cada variable
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#Vamos a utilizar la funcion input para recojer datos por medio del teclado
nombre=input("¿como te llamas?")
edad=input("¿cuantos años tienes?")
estado=input("¿en que estado te encuentras?")
nota=input("¿que nota sacaste?")

#Para visualisar que guardamos en las variables anteriores
print("hola,",nombre,"un gusto conocerte")
print("tu edad es:",edad)
print("tu estado es:",estado)
print("tu nota es:",nota)