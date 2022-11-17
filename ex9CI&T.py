def menor_string_maior(name):
    cont = 2
    copia = list(name)
    lista = []
    comprimento = len(copia)
    if len(name) <= 1 or name == "".join(sorted(name,reverse=True)):
        resposta = "sem resposta"
    elif name == "".join(sorted(name)):
            contador = copia.count(max(copia))+1
            copia.remove(max(name))
            copia.insert(len(name)-contador,max(name))
            resposta = "".join(copia)
    else:
        for i in range (len(copia),0,-1):
            if copia[i-1]>copia[(i-1)-1] and copia[i-1] == copia[-1]:
                copia[i-1],copia[(i-1)-1] = copia[(i-1)-1],copia[i-1]
                resposta = "".join(copia)
                break  
            elif copia[i-1]>copia[(i-1)-1] and copia[i-1] != copia[-1]:
                copia[i-1],copia[(i-1)-1] = copia[(i-1)-1],copia[i-1]
                lista = copia[6:]
                copia = copia[0:6]
                lista = sorted(lista)
                for i in lista:
                    copia.append(i)
                resposta = "".join(copia)
                
                break
    return resposta
    








        









print(menor_string_maior("nextgen"))