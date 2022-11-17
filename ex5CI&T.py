def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    horas =[]
    horas_batizadas =[]
    porcentagem = []
    for i in minutos_assistidos:
        hora= i//60
        if i%60 >= 1:
            hora+=1
        horas.append(hora)
    for z in range(len(assinante)):
        if assinante[z] == True:
            horas_batizadas.append(horas[z]*2)
        else:
            horas_batizadas.append(horas[z])
    for i in horas_batizadas:
        percentual = (i*100)/sum(horas_batizadas)

        porcentagem.append(round(percentual))
    return porcentagem

    
    
    
    
    
    
    
    
    
calcula_porcentagem_sorteio([True,False],[80,1050])   