def main():
    while True:
        
        try:
            num,den=input("Fraction: ").split('/')
            num=int(num)
            den=int(den)
            result=obtner_resul(num,den)
        except NameError:
            pass
        except ValueError:
            pass
        except UnboundLocalError:
            pass
        except TypeError:
            pass
        else:
            if (0<=result<=1):
                break
            else:
                pass
    if 0<=result<=0.1:
        print('E')
    elif .99<=result<=1:
        print('F')
    else:
        print(f'{result*100:.0f}%')
           

def obtner_resul(num,den):
        try:
            result=num/den
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        return result
main()