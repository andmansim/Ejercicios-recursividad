# Variables
frase = "Casa"

print(frase)

#función para comprobar que la frase contiene letras, números o ambos
def alfanumerico(f):
    # va a verificar que frase se compone de letras o números
    for i in f:
        if f.isnumeric(): #función para saber si es un número o no, también vale con f.isdigit()
            return("Solo números")
        elif type(f) == str: #para comprobar que contiene letras
            return("Solo letras")
        elif type(f) == str and f.isnumeric():
            return("tiene letras y números")
        else:
            return("Frase no es válida")
        
print(alfanumerico(frase))

'''from unidecode import unidecode
unidecode(frase)'''
 # instalar pip install unidecode 
 # unidecode, biblioteca que nos transforma los caracteres específicos en unos que no
    
#Función para quitar toda parte acentuada
'''
def acentuacion(r):
    unidecode(f)'''
        
#Función para transformar toda letra mayúscula en minúscula
def minuscula(a):
    k = a.lower()
    return k
print(minuscula(frase))