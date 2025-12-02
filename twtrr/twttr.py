nuevo_texto=''
vocales={'a','e','i','o','u','A','E','I','O','U'}
texto=input("Input: ")

for letra in texto:
    if letra not in vocales:
      nuevo_texto+=letra  
        

print(nuevo_texto)


'''
another form to do this exercice more eficient:

vocales = {'a','e','i','o','u','A','E','I','O','U'}

texto = input("Input: ")
nuevo_texto = ''.join(letra for letra in texto if letra not in vocales)

print(nuevo_texto)
'''