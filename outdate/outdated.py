
meses=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def es_fecha_valida(fecha):
    if 0<fecha[1]<=31:
        if 0<fecha[0]<=12:         
            return True     
    else:
        return False


def main():
    while True:
        try:
            date=input("Date: ")
            if '/' in date:
                date=date.split('/')                
                date=list(map(int,date))
                if es_fecha_valida(date):
                    print(f'{date[2]}-{date[0]:02d}-{date[1]:02d}')
                    break
            elif ',' in date:
                date=date.replace(',','')
                date=date.split()
                if date[0] in meses:
                    date[0]=int(meses.index(date[0]))+1
                    date=list(map(int,date))
                    if es_fecha_valida(date):
                        print(f'{date[2]}-{date[0]:02}-{date[1]:02}')
                        break
        except EOFError:
            break
        except ValueError:
            pass
        #print(date)
   
main()