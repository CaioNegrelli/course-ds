import sys

numeros = [int(valor) for valor in sys.argv[1:-2]]
x, y = int(sys.argv[-2]), int(sys.argv[-1])

soma = numeros[x] + numeros[y]

print(f' {soma}')
