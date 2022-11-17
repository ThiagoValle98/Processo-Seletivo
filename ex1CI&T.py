#def calculo_de_posto(combustivel,consumo,postos):
    #autonomia = consumo*combustivel
    #if autonomia == postos[1]:
        #print(autonomia)



def ultima_parada(combustivel,consumo,postos_de_gasolina):
    postos_de_gasolina= sorted(postos_de_gasolina)
    autonomia = combustivel*consumo
    for i in range (len(postos_de_gasolina)):
        if postos_de_gasolina[i] > autonomia and postos_de_gasolina[i] == postos_de_gasolina[0]:
            return -1

        elif postos_de_gasolina[i] < autonomia and postos_de_gasolina[i] == postos_de_gasolina[-1]:
            return postos_de_gasolina[-1]

        elif postos_de_gasolina[i] > autonomia:
            return postos_de_gasolina[i-1]


            
        
print(ultima_parada(2,4,[40,30,20,10]))




        


