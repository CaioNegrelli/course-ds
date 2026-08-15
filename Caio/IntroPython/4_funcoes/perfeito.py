import sys

n = int(sys.argv[1])

def perfeito(numero):
    soma = 0
    divisores = ''
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
            divisores += f'{i}, '
    return soma == numero, divisores

eh_perfeito, divisores = perfeito(n)
if eh_perfeito:
    print(f'{n} é perfeito')
else:
    print(f'{n} Não é perfeito')
print(f'Divisores [{divisores}]')