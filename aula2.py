a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
#a = 10
#b = 6
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('O valor total da soma: ' + str(soma))
print('O valor total da subtração: ' + str(subtracao))
print('O valor total da multiplicação: ' + str(multiplicacao))
print('O valor total da divisão: ' + str(divisao))
print('O valor total do resto: ' + str(resto))
print('Soma: {}. \nSubtracao: {}. \nMultiplicacao: {}. \nDivisao: {}. \nResto: {}'.format(soma, subtracao, multiplicacao, divisao, resto))