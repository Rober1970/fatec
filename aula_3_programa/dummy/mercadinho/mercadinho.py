# author: Rodrigo Nunes Ciriaco
# version: 1.0.1
# date: abr/09/2022
# description: este programa cadastra usuários
# name: mercadinho fatec


from hashlib import sha256
import sys
from time import sleep

# mensagem de boas vindas
mensagem = "Olá seja bem-vindo ao Mercadinho Fatec"

# imprimindo mensagem de boas vindas como máquina de escrever
for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    sleep(0.1)
print()
  
# setando as opções do menu
opcoes_de_menu = ["sign in", "sign up", "fale conosco"]

# imprimindo menu de opções
count = 1
for opcao in opcoes_de_menu:
    print(f"[{count}] - {opcao}")
    count += 1 # count = count + 1
    
opcao_digitada = input("Qual opção deseja? ")


with open("db.csv") as arquivo: # with open("db.csv","w") as arquivo: criar um arquivo no windows
    print(arquivo.read())  





