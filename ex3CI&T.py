def calcula_numero_da_senha(senha):
    pos0=[]
    pos1=[]
    pos2=[]
    pos3=[]
    pos4=[]
    pos5=[]
    pos6=[]
    pos7=[]
    pos8=[]
    pos9=[]
    pass_word =[]
    for x in senha:
        for y,z in enumerate(x):
            if y == 0:
                pos0.append(z)
            if y == 1:
                pos1.append(z)
            if y == 2:
                pos2.append(z)
            if y == 3:
                pos3.append(z)
            if y == 4:
                pos4.append(z)
            if y == 5:
                pos5.append(z)
            if y == 6:
                pos6.append(z)
            if y == 7:
                pos7.append(z)
            if y == 8:
                pos8.append(z)
            if y == 9:
                pos9.append(z)
    contador = pos0.count("0")
    if contador >= 6:
        pass_word.append("0")
    else:
        pass_word.append("1")
    contador = pos1.count("0")
    if contador >= 6:
        pass_word.append("0")
    else:
        pass_word.append("1")
    contador = pos2.count("0")
    if contador >= 6:pass_word.append("0")
    else:pass_word.append("1")
    contador = pos3.count("0")
    if contador >= 6:pass_word.append("0")
    else:pass_word.append("1")
    contador = pos4.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    contador = pos5.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    contador = pos6.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    contador = pos7.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    contador = pos8.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    contador = pos9.count("0")
    if contador >= 6:pass_word.append("0")
    else: pass_word.append("1")
    senhastring = "".join(pass_word)
    senhaint=int(senhastring,2)
    return  senhaint






            


        



        
        


            


            
        
            
            





print(calcula_numero_da_senha(["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]))