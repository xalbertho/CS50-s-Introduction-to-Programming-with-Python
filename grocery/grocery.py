grocery={}
while True:
    try:
        item=input()
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1
    except EOFError:
        break

grocery=dict(sorted(grocery.items()))

for element,cantidad in grocery.items():
    element=element.upper()
    print(f'{cantidad} {element}')