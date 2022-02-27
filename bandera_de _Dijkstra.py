#Variables

fichas = "RVVARVVARVARAVR"
l_rojas = []
l_verdes = []
l_azul = []

fichas = list(fichas)
print(fichas)

#Función para leer fichas
def leer_fichas(f):
    for i in range(0, len(fichas)):
        if fichas[i] == "R": # me guarda en una lista las posiciones de dicha fichas
            l_rojas.append(i) 
        
        if fichas[i] == "V":
            l_verdes.append(i) 
        
        if fichas[i] == "A":
            l_azul.append(i) 
    
    print("Posiciones fichas rojas")
    print(l_rojas)
    print("Posiciones fichas verdes")
    print(l_verdes)  
    print("Posiciones fichas azules")
    print(l_azul)
    
leer_fichas(fichas)

# Número de fichas de cada color 
j = len(l_rojas)
k = len(l_verdes)
w = len(l_azul)

for q in range(0, len(fichas)):
    if q <= j - 1: #en este hueco van las rojas
                 
        if q in l_verdes: #si lo tiene las verdes, los intercambiamos
            p = l_verdes.index(q) #hay una roja donde las verdes, las intercambio
           
            fichas[l_rojas[q]], fichas[q] = fichas[q], fichas[l_rojas[q]]
           
            l_verdes[p] = l_rojas[q]
        elif q in l_azul:
            p = l_azul.index(q) #hay una roja donde las verdes, las intercambio
            
            fichas[l_rojas[q]], fichas[q] = fichas[q], fichas[l_rojas[q]]
            
            l_azul[p] = l_rojas[q]
        print(fichas)
        
        l_verdes.sort()
        l_azul.sort()    
        print(l_verdes)
        print(l_azul)        
    elif (k + j ) > q >= j   :  #en este hueco van las verdes
        
        if q in l_azul: #si lo tiene las azules, los intercambiamos
            p = l_azul.index(q) #hay una verde donde las azules, las intercambio
            
            fichas[l_verdes[q - j ]], fichas[q] = fichas[q], fichas[l_verdes[q - j ]]
            
            l_azul[p] = l_verdes[q - j ]
        
print (fichas)