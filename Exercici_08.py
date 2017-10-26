print "Altura de un triangulo"
altu=input()
for c in range(altu-1,-1,-1):
    for d in range(c,altu,1):
             print "*",
    print ""
for c in range(1,altu):
    for d in range(c,altu,1):
             print "*",
    print ""
