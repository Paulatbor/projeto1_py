a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado ='soma: {}. ' \
           '\nsubtracao: {}.' \
           '\nmultiplicacao: {}.' \
           '\ndivisao: {} ' \
           '\nresto: {} '  .format(soma,
                                           subtracao,
                                           multiplicacao,
                                           divisao,
                                           resto)

print(resultado)