name=input("Whats ur name? ")

file=open("namex.txt",'a')
file.write(name)
file.close()