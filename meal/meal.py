def main():
    hours,minutes=convert(input("What time is it?: ")).split('.')
    hours=int(hours)
     
    if hours>=7 and hours<=8:
        print("breakfast time")
    elif hours>=12 and hours<=13:
        print("lunch time")
    elif hours>= 18 and hours<=19:
        print("dinner time")

    
def convert(hora):
    hours,minutes=hora.split(':')
    hours,minutes=int(hours),int(minutes)
    minutes=minutes/60
    hora=str(hours+minutes)
    return hora

      
        

if __name__=='__main__':
    main()
    