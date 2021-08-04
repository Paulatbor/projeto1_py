def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    pass

if __name__ == '__main__':
    media_notas(notas.txt)
    # escrever_arquivo('Primeira linha. \n')
    # atualizar_arquivo('Segunda linha. \n')
    # ler_arquivo('teste.txt')