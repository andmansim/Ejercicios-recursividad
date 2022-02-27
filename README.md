# Ejercicios-recursividad

La dirección de mi repositorio de GitHub es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios-recursividad.git)

https://github.com/andmansim/Ejercicios-recursividad.git

He realizado tres ejercicios distintos, los cuales son: La bandera de Dijkstra, Paíndromo y busqueda por dicotomía en una tabla ordenada. Empleando recursividad y clases.
También a cada ejercicio le corresponde un diagrama UML, representando las distintas variables y funciones de nuestro programa.
El diagrama UML del Palindromo es el siguiente:


![El diagrama UML del Palindromo](/Palindromo.jpg)
```
# Variables
frase = "Hola 3 soy Andreá"
frase = "Hooh"

print(frase)
#función para quitar espacios
def espacios(e):
    if " " in e:
        e = e.replace(" ", "")
        return e


#función para comprobar que la frase contiene letras, números o ambos

def alfanumerico(f):
    if f.digit():
    # va a verificar que frase se compone de letras o números
        return ("Solo números")
    elif f.isalpha(): #para comprobar que contiene letras
        return("Solo letras")
    elif f.isalnum():
        return("tiene letras y números")
    else:
        return("Frase no es válida")
  

#Función para quitar toda parte acentuada

def acentuacion(r):
    if "á" in r:    
        r = r.replace("á", "a")
        
    if "é" in r:
        r = r.replace('é', 'e')

    if "í" in r:
        r = r.replace('í', 'i')

    if "ó" in r:
        r = r.replace('ó', 'o')
           
    if "ú" in r:
        r = r.replace('ú', 'u')
        
    return r



#Función para transformar toda letra mayúscula en minúscula
def minuscula(a):
    k = a.lower()
    return k


#Función invertir 
def invertir(b):
    if len(b) == 0:
        return b
    else: 
        b = invertir(b[1:]) + b[0] # pasa la primera letra al final y se llama otra vez así misma para hacerlo con todas
        return b

frase = espacios(frase) 
print (alfanumerico(frase)) 
frase = minuscula(frase)
frase = acentuacion(frase)
c =frase
frase = invertir(frase)
print(frase)


#Comparamos la frase inicial con el resultado y decimos si es o no
if frase == c:
  print("Es un palíndromo")
else:
    print("No es un palíndromo")
```


El diagrama UML de la bandera de Dijkstra es el siguiente:

![El diagrama UML de la bandera de Dijkstra](/Dijkstra.jpg)

```
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
```


El diagrama UML de la busqueda por dicotomía en una tabla ordenada es el siguiente:

![El diagrama UML de la busqueda por dicotomía en una tabla ordenada](/Dicotomia.jpg)

```
#prefijo toledo 45
tabla = [['Maria ','25001', '34'],['Zihara ','35210', '45'],['Aruca ','45120', '56'],['Yurima ','28205', '47'],['Yeneva ','28150', '49'],['Eduin ','45260', '20'],['Diosnel ','35166', '78'],['Rolindes ','58962', '82'],['Yandira ','45896', '34'],['Juan ','12365', '67'],['Daniel ','48965', '67'],['Jose ','45120', '19'],['Yania ','28205', '90'],['Jean ','28150', '39'],['Enetz ','45260', '45'],['Arnaitz ','35166', '49']]
persona = []
def toledo (t, n, c):
      
    if 0 <= n < len(t):
        if t[n][1].startswith(c): #Buscamos el inicio de su código postal
            persona.append (t[n][0]) 
            toledo(t,n+1,c) # Parte recursiva, se llama así misma 
        else:
            toledo(t,n+1,c)
                
#Segunda parte del ejercicio
def Madrid (t, n, c,e,f):
          
    if 0 <= n < len(t):
        if t[n][1].startswith(c):
            if e <= t[n][2] <= f: #filtro para encontrar a las personas comprendidas entre estas edades
                persona.append (t[n][0]) 
                Madrid(t,n+1,c, e, f)
        else:
            Madrid(t,n+1,c, e, f)
                
toledo(tabla, 0, '45')
print (persona)
persona=[]
Madrid(tabla, 0, '28','40','50')
print (persona)
```
