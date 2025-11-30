variable=input("camelCase: ")
resultado=""

for letra in variable:
    if letra.isupper():
        resultado+="_"+letra.lower()
    else:
        resultado+=letra
     
print(resultado)