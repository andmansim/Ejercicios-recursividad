# Variables
frase = "cuero"

print(frase)

#función para comprobar que la frase contiene letras, números o ambos
def alfanumerico(f):
    # va a verificar que frase se compone de letras o números
    for i in f:
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
'''
def acentuacion(r):
   '''
        
#Función para transformar toda letra mayúscula en minúscula
def minuscula(a):
    k = a.lower()
    return k
print(minuscula(frase))

#Función invertir 
def invertir(b):
    if len(b) == 0:
        return b
    else: 
        b = invertir(b[1:]) + b[0] # pasa la primera letra al final y se llama otra vez así misma para hacerlo con todas
        return b
    
print(invertir(frase))