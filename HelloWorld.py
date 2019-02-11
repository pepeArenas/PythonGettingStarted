print("Hello World")

nombre = "jose de jesus arenas mondragon"
# Pone la primer letra de toda la str como mayuscula
print(nombre.capitalize())
# remplaza todas las A's con X's
print(nombre.replace("a", "x"))
# Verifica que todos los caracteres sean digitos
print(nombre.isalpha())
# Verifica que todos los caracteres sean digitos
print(nombre.isdigit())
# Va a generar un array con los elementos de una cadena dada separados por espacio
print(nombre.split(" "))

trueValueEx = True
falseValueEx = False
"""Imprimimos True o False"""
print(trueValueEx)
print(falseValueEx)

"""Si casteamos un true a int nos da un 1, si casteamos un false nos da un 0"""
print(int(trueValueEx))
print(int(falseValueEx))

"""Si casteamos un True a un str nos dara el string 'True', 
al igual que si casteamos un False nos dara string 'false'"""
print(str(trueValueEx))
print(str(falseValueEx))
