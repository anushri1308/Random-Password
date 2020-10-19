import secrets
chars=[chr(x) for x in range(33,127)]
print(''.join([secrets.choice(chars) for y in range(int(input('Password Length: ')))]))
