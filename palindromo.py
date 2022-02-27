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

