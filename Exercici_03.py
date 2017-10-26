print "Dime un numero"
prime=input()
print "Dime un numero mas mayor que" , prime
secu=input()
o=0
for i in range(prime,secu+1):
    o=o+i
print "la suma desde" , prime , "hasta" , secu , "es" , o 
