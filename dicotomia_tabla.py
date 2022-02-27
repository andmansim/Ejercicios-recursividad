#prefijo toledo 45
tabla = [['Maria ','25001'],['Zihara ','35210'],['Aruca ','45120'],['Yurima ','28205'],['Yeneva ','28150'],['Eduin ','45260'],['Diosnel ','35166'],['Rolindes ','58962'],['Yandira ','45896'],['Juan ','12365'],['Daniel ','48965'],['Jose ','45120'],['Yania ','28205'],['Jean ','28150'],['Enetz ','45260'],['Arnaitz ','35166']]
persona = []
def toledo (t, n, c):
    i = 0
   
    
    if 0 <= n < len(t):
                   
        if t[n][1].startswith('45'):
            persona.append (t[n][0]) 
            toledo(t,n+1,c)
        else:
            toledo(t,n+1,c)
            



    
toledo(tabla, 0, '45')
print (persona)
