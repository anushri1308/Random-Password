import secrets

print(''.join([secrets.choice([chr(x) for x in range(33,127)]) for y in range(int(input('Password Length: ')))]))
