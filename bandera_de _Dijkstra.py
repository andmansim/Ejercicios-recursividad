#Variables
fichas = "RVAARV"
l_rojas = []
l_verdes = []
l_azul = []
l_sin_color = []
fichas = list(fichas)
print(fichas)
def leer_fichas(f):
 
    for i in f:
        if "R" in f:
            c = f.index("R")
            
        if "V" in f:
            a = f.index("V")
            
        if "A" in f:
            b = f.index("A")
        
            #d = f.index("?")
            #return l_sin_color.append(d)
            
    return (c, a, b)
c_l, a_l, b_l = leer_fichas(fichas)

print(c_l)
print(a_l)
print(b_l)