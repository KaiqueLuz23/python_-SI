# Imports:
import os

#############################################
# ping IP único
#############################################
#print("#" * 60)
#ip_host = input("Digite seu IP ou Host: ")
#print("#" * 60)
#os.system('ping -n 6 {}'.format(ip_host))
#print("-" * 60)

#############################################
# ping IP múltiplo
#############################################
import time

print("#" * 60)
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()


    for ip in dump:
        print("Verificando IP: ", ip)
        print("-" * 60)
        os.system('ping -n 3 {}'.format(ip))
        print("-" * 60)
        time.sleep(5)

