# Variables
import string
from numpy import integer


frase = "Oso"
#frase = list(frase)
print(frase)

def alfanumerico(f):
    # va a verificar que frase se compone de letras o números
    for i in f:
        if f == integer:
            return("Solo números")
        elif f == string:
            return("Solo letras")
        elif f == string and f == integer:
            return("tiene letras y números")
        else:
            return("Frase no es válida")
        
a = alfanumerico(frase)
print(a)