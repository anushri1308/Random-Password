import secrets

print(''.join([secrets.choice([chr(secrets.choice([x for x in range(33,127)]))]) for y in range(int(input('Password length: ')))]))
