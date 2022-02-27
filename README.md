# Ejercicios-recursividad

La dirección de mi repositorio de GitHub es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios-recursividad.git)

https://github.com/andmansim/Ejercicios-recursividad.git

He realizado tres ejercicios distintos, los cuales son: La bandera de Dijkstra, Paíndromo y busqueda por dicotomía en una tabla ordenada. Empleando recursividad y clases.
También a cada ejercicio le corresponde un diagrama UML, representando las distintas variables y funciones de nuestro programa.
El diagrama UML del Palindromo es el siguiente:


![El diagrama UML del Palindromo](/Palindromo.jpg)
```
# Variables
frase = "Hola soy Andreá"
#frase = "Hooh"
f=""
   
class Palindromo:
    def espacios():
        h = frase.replace(" ", "")
        return h    


    def alfanumerico():
        # va a verificar que frase se compone de letras o números
          
        if f.isnumeric(): #función para saber si es un número o no, también vale con f.isdigit()
            print ("Solo números")
        elif f.isalpha(): #para comprobar que contiene letras
            print ("Solo letras")
        elif f.isalnum():
            print ("tiene letras y números")
        
             
    
    #transformar toda letra mayúscula en minúscula
    def minuscula():
        k = f.lower()
        return k
    
    # quitar toda parte acentuada
    def acentuacion():
        f2 = n.replace("á", "a")
        f2 = f2.replace("é", "a")
        f2 = f2.replace("í", "a")
        f2 = f2.replace("ó", "a")
        f2 = f2.replace("ú", "a")
        return f2
    
    def invertir():
        a2=""
        for i in range(0,len(m)):
            a2 = m[i] + a2 # pasa la primera letra al final y se llama otra vez así misma para hacerlo con todas
        return a2

l = Palindromo()
f = Palindromo.espacios()
Palindromo.alfanumerico()
n = Palindromo.minuscula()
m = Palindromo.acentuacion()
b = Palindromo.invertir()

print (b)
print (m)

#Comparamos la frase inicial con el resultado y decimos si es o no
if b == m:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
```


El diagrama UML de la bandera de Dijkstra es el siguiente:

![El diagrama UML de la bandera de Dijkstra](/Dijkstra.jpg)

```
 #Variables
fichas = "RVVARVVARVARAVR"
l_rojas = []
l_verdes = []
l_azul = []

fichas = list(fichas)
print(fichas)

class Dijkstra:
     
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
        
    def ordenar_fichas(f):    

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
                l_verdes.sort()
                l_azul.sort()    
                       
            elif (k + j ) > q >= j   :  #en este hueco van las verdes
        
                if q in l_azul: #si lo tiene las azules, los intercambiamos
                    p = l_azul.index(q) #hay una verde donde las azules, las intercambio 
                    fichas[l_verdes[q - j ]], fichas[q] = fichas[q], fichas[l_verdes[q - j ]]
                    l_azul[p] = l_verdes[q - j ]
        
        print (fichas)
    
posicion_fichas = Dijkstra()
posicion_fichas.leer_fichas()
posicion_fichas.ordenar_fichas()
```


El diagrama UML de la busqueda por dicotomía en una tabla ordenada es el siguiente:

![El diagrama UML de la busqueda por dicotomía en una tabla ordenada](/Dicotomia.jpg)
