print "Dime un n�mero"
prime=input()
print "Dime un n�mero mas mayor que" , prime
secu=input()

for p in range(prime,secu+1):
    if p%2==0:
        print "El n�mero" , p , "es par"
    else:
        print "El n�mero" , p , "es impar"
    
    
    



