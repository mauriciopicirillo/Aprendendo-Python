import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write('Minha primeira escrita')
    arquivo.write('\nSegunda Linha')
    arquivo.write('\nTerceira Linha')
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
#         print(sum(lista_notas))

def copia_arquivo(nome_arquivo):
        shutil.copy(nome_arquivo, 'E:/Digital Innovation One/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'E:/Digital Innovation One/app-python/')


if __name__ == '__main__':
    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
        # lista_media = media_notas('notas.txt')
        # print(lista_media)
     #    escrever_arquivo('Primeira linha.\n')
     #    aluno = '\nCaio,7,8,5,10'
     #    atualizar_arquivo('notas.txt', aluno)
     #    ler_arquivo('teste.txt')