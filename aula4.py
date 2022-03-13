a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado a Nota do Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado a Nota do Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você digitou errado a Nota do Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou errado a Nota do Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('A média é: {}'. format(media))


# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota: '))


# a = 0
# while a <= 10:
#     print(a)
#     a +=1


# a = int(input('Entre com um valor: '))
# for num in range (a+1):
#     div = 0
#
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)



# a = int(input('Entre com um numero: '))
# div = 0
#
# for x in range (1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('O número {} é primo!'. format(a))
#
# else:
#     print('O número {} não é primo'. format(a))


# for x in range(100):
#     print(x)