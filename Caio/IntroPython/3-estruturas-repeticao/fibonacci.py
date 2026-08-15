import sys

n = int(sys.argv[1])

a, b = 0, 1

for i in range(n):

    print(f' {a}')
    b, a = a + b, b
    
    
