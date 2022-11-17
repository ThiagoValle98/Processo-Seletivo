def checa_numero_escondido(numero,numero_oculto):
    numero = str(numero)
    numero_oculto = str(numero_oculto)
    lista = []
    for x in range (len(numero)):
        for i in numero_oculto:
            if i == numero[x]:
                lista.insert(x,i)
                break
                
    if "".join(lista) == numero_oculto or "".join(lista).count(numero_oculto)!= 0:
        return True
    else: 
        return False

                
    



print(checa_numero_escondido(321123,123))