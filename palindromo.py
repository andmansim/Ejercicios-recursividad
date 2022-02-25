# Variables
frase = "Hola soy Andrea"
print(frase)
c = frase

#función para quitar espacios
def espacios(e):
    if " " in e:
        e = e.replace(" ", "")
        return e
    
frase = espacios(frase) 
 
#función para comprobar que la frase contiene letras, números o ambos
def alfanumerico(f):
    # va a verificar que frase se compone de letras o números
          
        if f.isnumeric(): #función para saber si es un número o no, también vale con f.isdigit()
            return("Solo números")
        elif f.isalpha(): #para comprobar que contiene letras
            return("Solo letras")
        elif f.isalpha() and f.isnumeric():
            return("tiene letras y números")
        else:
            return("Frase no es válida")
             
print(alfanumerico(frase))    
         
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
  
frase = acentuacion(frase)

#Función para transformar toda letra mayúscula en minúscula
def minuscula(a):
    k = a.lower()
    return k
frase = minuscula(frase)

#Función invertir 
def invertir(b):
    if len(b) == 0:
        return b
    else: 
        b = invertir(b[1:]) + b[0] # pasa la primera letra al final y se llama otra vez así misma para hacerlo con todas
        return b
    
frase = invertir(frase)
print(frase)

#Comparamos la frase inicial con el resultado y decimos si es o no
if frase == c:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")