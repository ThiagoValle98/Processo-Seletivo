def calcula_top_ocorrencias_de_queries(texto,queries,k):
    texto = str(texto).lower().strip()
    contador=[]
    conter = 0
    final = []
    k = int(k)
    primeiros = []
    last = []
    for i in range(len(queries)):
        if texto.count(queries[i]) != 0:
            contador.append(texto.count(queries[i]))
            contador.append(queries[i])
            final.append(contador[:])
            contador.clear()

    while conter < k:
        primeiros.append(max(final))
        final.remove(max(final))
        conter+=1
    for i in primeiros:
        last.append(i[1])
    return last

        




        
            
        






calcula_top_ocorrencias_de_queries("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",["a","em","i","el","ore"],4)