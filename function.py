def analise_list(list):
    
    # media
    media = 0
    maior = 0
    menor = 0
    par = []
    
    for n in list:
        if list.index(n) == 0:
            media = n
            maior = n
            menor = n
        else:
            media += n
            
            if n > maior:
                maior = n
            
            if n < menor:
                menor = n
            
        if n % 2 == 0:
            par.append(n)
            
            
    
    media = f'{media / len(list):.2f}'
    
    return [media, maior, menor, len(par)]
