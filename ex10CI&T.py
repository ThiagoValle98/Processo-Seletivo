def shuffle_musicas(musicas_tocadas):
    musicas_tocadas = list(musicas_tocadas)
    lista = []
    for i in range (len(musicas_tocadas)):
        if i % 2 == 0:
            lista.append(max(musicas_tocadas))
            musicas_tocadas.remove(max(musicas_tocadas))
        else:
            lista.append(min(musicas_tocadas))
            musicas_tocadas.remove(min(musicas_tocadas))
    return lista



shuffle_musicas([2,10,5,3])