import random
n=0
numero_rand=0


while True: 
    n=input('Level: ')
    if (n.isdigit() ):
        n=int(n)
        numero_rand=random.randint(1,n)
        break

while True:
    resp=input("Guess: ")
    if resp.isdigit():
        resp=int(resp)
        if ((resp<numero_rand) and (resp>0)):
            print('Too small!')
        elif resp>numero_rand:
            print('Too large!')
        elif resp==numero_rand:
            print('Just right!')
            break
        else:
            pass