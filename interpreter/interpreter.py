x,y,z=input("Expression: ").split()
x,z=int(x),int(z) 
match y:
    case ("+"):
        print(f'{x+z:.1f}')
    case ("-"):
        print(f'{x-z:.1f}')
    case ("/"):
        print(f'{x/z:.1f}')
        # comment:
    case ("*"):
        print(f'{x*z:.1f}')
        # comment:  
         