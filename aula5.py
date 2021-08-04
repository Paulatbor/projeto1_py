lista = [12, 10, 7, 5]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print(len(tupla))
tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))

lista_numerica[0] = 100
print(lista_numerica)
# print(lista_animais[1])
# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# lista_animais.reverse()
# print(lista_animais)


# a = input('Localizar animais no zoo. Escreva qual animal gostaria de visitar: ')
# if a in lista_animais:
#     print('existe um {} na lista' .format(a))
# else:
#     print('não existe um {} na lista. Será incluído' .format(a))
#     lista_animais.append(a)
#     print(lista_animais)

# lista_animais.pop()
# print(lista_animais)

# lista_animais.remove('elefante')
# print(lista_animais)
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
