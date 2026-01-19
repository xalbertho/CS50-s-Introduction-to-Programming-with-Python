import random

def main():
    contador=0
    score=0
    level=get_level()
    while contador<=9:
        x=generate_integer(level)
        y= generate_integer(level)
        result=x+y
        contador_errores=0
        while True:
            user_result=input(f'{x} + {y} = ')
            try:
                user_result=int(user_result)
            except ValueError:
                pass

            if user_result==result:
                score+=1
                break
            else:
                print('EEE')
                contador_errores+=1
                if contador_errores==3:
                    print(f'{x} + {y} = {x+y}')
                    break
    
        contador+=1
    print(f'Score: {score}')
    
def get_level():
    while True:
        level=input('Level: ')
        try:
            level=int(level)
            if 1<=level<=3:
                return level
        except ValueError:
            pass 

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)

if __name__=="__main__":
    main()