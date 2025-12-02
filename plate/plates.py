def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    mitad=len(s)/2 - 1
    numeros=[]

    if len(s)<=6 and len(s)>=2:
        if s.isalnum():
            if s[0:2].isalpha():
                for letra in s:
                    if letra.isdigit():
                        numeros.append(letra)
                    else: 
                        pass
                if not numeros:
                    return True
                elif numeros[0]=='0':
                    return False
                elif s[2:len(s)-2].isdigit():
                    return False
                else:
                    return True
                
    else:
        return False
                



main()
'''
implementar:
empiece con 2 letras
maximmo 6 caracteres
numeros al final
el primer numero no puede ser 0
ningun signo de puntuacion
'''