#prefijo toledo 45
tabla = [['Maria ','25001', '34'],['Zihara ','35210', '45'],['Aruca ','45120', '56'],['Yurima ','28205', '47'],['Yeneva ','28150', '49'],['Eduin ','45260', '20'],['Diosnel ','35166', '78'],['Rolindes ','58962', '82'],['Yandira ','45896', '34'],['Juan ','12365', '67'],['Daniel ','48965', '67'],['Jose ','45120', '19'],['Yania ','28205', '90'],['Jean ','28150', '39'],['Enetz ','45260', '45'],['Arnaitz ','35166', '49']]
persona = []
def toledo (t, n, c):
      
    if 0 <= n < len(t):
        if t[n][1].startswith(c):
            persona.append (t[n][0]) 
            toledo(t,n+1,c)
        else:
            toledo(t,n+1,c)
                

def Madrid (t, n, c,e,f):
          
    if 0 <= n < len(t):
        if t[n][1].startswith(c):
            if e <= t[n][2] <= f:
                persona.append (t[n][0]) 
                Madrid(t,n+1,c, e, f)
        else:
            Madrid(t,n+1,c, e, f)
                
toledo(tabla, 0, '45')
print (persona)
persona=[]
Madrid(tabla, 0, '28','40','50')
print (persona)
