#Variables

fichas = "RVAARV"
l_rojas = []
l_verdes = []
l_azul = []
l_sin_color = []
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

def mover_fichas():
    for j in l_rojas:
        if l_rojas[j] in range(0, len(l_rojas)):
            