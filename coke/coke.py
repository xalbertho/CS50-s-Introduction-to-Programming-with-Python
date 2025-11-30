saldo=0
cuenta=50
while (saldo<50):
    print(f'Amount Due: {cuenta-saldo}')
    moneda=int(input('Insert Coin: '))
    
    match (moneda):
        case 10 :
            saldo+=moneda
        case (25):
            saldo+=moneda
            # comment: 
        case 5:
            saldo+=moneda
        case _:
            pass
    if saldo>=50:
        print(f'Change Owed: {saldo-cuenta}')
        
    
'''
secunday form of program this problem more efficient
saldo = 0
cuenta = 50
monedas_validas = {5, 10, 25}

while saldo < cuenta:
    print(f"Amount Due: {cuenta - saldo}")
    moneda = int(input("Insert Coin: "))

    if moneda in monedas_validas:
        saldo += moneda

print(f"Change Owed: {saldo - cuenta}")
'''


            
