# Variables
frase = "ui"

print(frase)


def alfanumerico(f):
    # va a verificar que frase se compone de letras o números
    for i in f:
        if f.isnumeric(): #función para saber si es un número o no, también vale con f.isdigit()
            return("Solo números")
        elif type(f) == str:
            return("Solo letras")
        elif type(f) == str and f.isnumeric():
            return("tiene letras y números")
        else:
            return("Frase no es válida")
        
a = alfanumerico(frase)
print(a)