user = list()
users = list()
while True:
    user.append(str(input('Digite seu nome')).upper().strip())
    user.append(int(input('Digite sua idade')))
    users.append(user[:])
    user.clear()
    prg = str(input('Deseja para [S/N]')).upper().strip()
    if prg == 'N':
        break

print(users)

for p in users:
    print(p[0], end=', Idade: ')
    print(p[1])
