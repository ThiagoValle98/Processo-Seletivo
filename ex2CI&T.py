def retorna_menor_e_maior_valor_de_vendas(tickets):
    tickets_filtrados=[]
    t = []
    for i, z in enumerate(tickets):
        for x in range(len(z)):
            if z[x]>=20 and z[x]<=500:
                t.append(z[x])
    tickets_filtrados.insert(0,min(t))
    tickets_filtrados.insert(1,max(t))
    return tickets_filtrados







retorna_menor_e_maior_valor_de_vendas([[20,100],[300], [100,300]])



