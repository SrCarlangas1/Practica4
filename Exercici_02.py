print "Dime un número"
prime=input()
print "Dime un número mas mayor que" , prime
secu=input()

for p in range(prime,secu+1):
    if p%2==0:
        print "El número" , p , "es par"
    else:
        print "El número" , p , "es impar"
    
    
    



