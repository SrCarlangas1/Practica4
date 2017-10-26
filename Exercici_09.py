print "dame la altura del rectangulo"
a=input()
print "dame la anchura del rectangulo"
b=input()
for i in range (a):
    for j in range (b):
        if i==0 or i==a-1:
            print "*",
        else:
            if j==0 or j==b-1:
                print"*",
            else:
                print" ",
    print ""
        
