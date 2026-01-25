def main():
    fraction=input('Fraction: ')
    percentaje=convert(fraction)
    print(gauge(percentaje))

def convert(fraction):
    try:
        numerador,denominador=fraction.split('/')
        numerador=int(numerador)
        denominador=int(denominador)
        resultado=numerador/denominador
        if resultado<0:
            raise ValueError
       
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    if numerador>denominador:
            raise ValueError
    return resultado*100
def gauge(percentage):
    if 0<=percentage<=10:
        return('E')
    elif 99<=percentage<=100:
        return('F')
    else:
        return(f'{percentage:.0f}%')
           

if __name__=="__main__":
    main()
