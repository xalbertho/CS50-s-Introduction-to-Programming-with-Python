import inflect
nombres=[]

p=inflect.engine()

def imprimir():
    text='Adieu, adieu, to '
   
    text=text+p.join((nombres), conj="and")

    print(text)



while True:
    try: 
        nombres.append(input('Name: '))
    except EOFError:
        print('\n')
        imprimir()
        break


    
