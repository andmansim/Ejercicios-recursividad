 #Variables
fichas = "RVVARVVARVARAVRA"
l_rojas = []
l_verdes = []
l_azul = []

q = 0
colocadas = False

fichas = list(fichas)
print(fichas)

     
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



def ordenar_fichas(q):    
    # Número de fichas de cada color 
    j = len(l_rojas)
    k = len(l_verdes)
    w = len(l_azul)
    
    if q <= j - 1: #en este hueco van las rojas
        
        if q in l_verdes: #si lo tiene las verdes, los intercambiamos
            p = l_verdes.index(q) #hay una roja donde las verdes, las intercambio
        
            fichas[l_rojas[q]], fichas[q] = fichas[q], fichas[l_rojas[q]]
        
            l_verdes[p] = l_rojas[q]
        elif q in l_azul:
            p = l_azul.index(q) #hay una roja donde las verdes, las intercambio
        
            fichas[l_rojas[q]], fichas[q] = fichas[q], fichas[l_rojas[q]]
        
            l_azul[p] = l_rojas[q]        
        l_verdes.sort()
        l_azul.sort()    
                    
    elif (k + j ) > q >= j   :  #en este hueco van las verdes
        
        if q in l_azul: #si lo tiene las azules, los intercambiamos
            p = l_azul.index(q) #hay una verde donde las azules, las intercambio 
            fichas[l_verdes[q - j]], fichas[q] = fichas[q], fichas[l_verdes[q - j ]]
            l_azul[p] = l_verdes[q - j]
        
    
    while q < j + k :
        q += 1
        ordenar_fichas(q)    
    
       
        
leer_fichas(fichas)
ordenar_fichas(0)
        
print (fichas)
    

