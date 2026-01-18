from pyfiglet import Figlet
import random
import sys

figlet=Figlet()
available=figlet.getFonts()

if len(sys.argv) == 1:
    txt=input('Input: ')
    rand_font=random.choice(available)

    figlet=Figlet(font=rand_font)
    print('Output:',figlet.renderText(txt))
elif len(sys.argv) ==3:
    if ((sys.argv[1]!='-f') and  (sys.argv[1]!='--font')):
        sys.exit(1)

    if sys.argv[2] not in  available:
        print('Invalid usage')
        sys.exit(1)

    txt=input('Input: ')
    figlet=Figlet(font=sys.argv[2])
    print('Output:',figlet.renderText(txt))
else:
    print('Invalid usage')
    sys.exit(1)