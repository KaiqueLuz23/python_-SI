# Imports:
import random, string

#############################################

tamanho = int(input("Digite um tamanho para sua senha: "))

chars = string.ascii_letters + string.digits + '!@#$%&*?'
rnd = random.SystemRandom()

password = ''.join(rnd.choice(chars) for i in range(tamanho))

#testanto
print(password)

#print(''.join(rnd.choice(chars) for i in range(tamanho)))


