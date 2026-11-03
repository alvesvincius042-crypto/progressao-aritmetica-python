

n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
for c in range(10):
    print(n1 + c * r)
n = int(input('Você quer mostrar mais quantos termos? '))
while n != 0:
    for c in range(c + 1, c + n + 1):
        print(n1 + c * r)
    n = int(input('Você quer mostrar mais quantos termos? '))

