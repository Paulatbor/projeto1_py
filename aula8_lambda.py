contador_letras = lambda lista: [len(x) for x in lista]


lista_animais = ['Cachorro', 'Gato', 'Elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 10))

calculadora = {
    'soma': lambda a, b: a +b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}
print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}' .format(multiplicacao(10, 2)))