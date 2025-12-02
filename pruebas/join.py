

''' 
En la sintaxis join, el primer argumetno es lo que retorna la funcion
'''

vocales={'a','e','i','o','u','A','E','I','O','U'}
texto=input("Ingrese su texto: ")
textonuevo=''.join(letra for letra in texto if letra not in vocales)
print(textonuevo)