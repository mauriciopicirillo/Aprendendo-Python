lista = [1, 10]


try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a



except ZeroDivisionError:
    print('Não é possivel realizar um divisão por 0')
except ArithmeticError:
    print('Não é possivel realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indece invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()