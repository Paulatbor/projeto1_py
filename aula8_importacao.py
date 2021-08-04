from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras
if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['Cachorro', 'Gato', 'Elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra de lista: {}' .format(total_letras))