def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    taxa1 = float(tf1)
    vkm1= float(vqr1)
    taxa2=float(tf2)
    vkm2 = float(vqr2)
    x = 0
    listapreço1 =[]
    listapreço2=[]
    igualdade = 0
    compara = []
    while x < 1000:
        preço1= taxa1 + (vkm1*x)
        preço2= taxa2 + (vkm2*x)
        listapreço1.append(preço1)
        listapreço2.append(preço2)
        x +=1.0
    for i in range(len(listapreço1)):
        if listapreço1[i] == listapreço2[i]:
            igualdade = i
        if listapreço1[0] < listapreço2[0]:
            comparação = "Empresa 1"
            compara.append(comparação)
        if listapreço2[0] < listapreço1[0]:
            comparação = "Empresa 2"
            compara.append(comparação)
    if taxa1 == taxa2 and vkm1 == vkm2:
        resposta = "Tanto faz"
    elif taxa1 <= taxa2 and vkm1 <= vkm2:
        resposta = "Empresa 1"
    elif taxa2 <= taxa1 and vkm2 <= vkm1:
        resposta = "Empresa 2"
    elif compara[0] == "Empresa 1":
        resposta = "Empresa 1 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 2 quando a distância > {}".format(float(igualdade),float(igualdade),float(igualdade))
    elif compara[0] == "Empresa 2":
        resposta = "Empresa 2 quando a distância < {}, Tanto faz quando a distância = {}, Empresa 1 quando a distância > {}".format(float(igualdade),float(igualdade),float(igualdade))
    return resposta



print(escolhe_taxi("2.5","1.0","5.0","0.75"))