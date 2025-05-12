from function import analise_list

lista_ex = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

media, maior, menor, pares = analise_list(lista_ex)

print(f'Média: {media}')
print(f'Maior Número: {maior}')
print(f'Menor Número: {menor}')
print(f'Quantidade de Números Pares: {pares}')