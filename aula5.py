lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista. Será incluido.')
#     lista_animal.append('lobo')
#     print(lista_animal)


# lista_animal.remove('elefante')
# print(lista_animal)

# lista_animal.pop(0)
# print(lista_animal)

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista')

# print(lista_animal[1])
# print(min(lista))
# print(max(lista))
# print(sum(lista))

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# for x in lista_animal:
#     print(x)