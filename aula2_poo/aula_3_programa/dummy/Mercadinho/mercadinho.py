# author: Roberval.silva
# version 1.0.1
# date: 09/04/22
# description: este programa cadastra usúarios
# name: mercadinho fatec

from hashlib import sha256
import sys

from time import sleep

mensagem = "Olá seja bem-vindo ao Mercadinho Fatec"

# imprimindo mensagem de boas vindas
for letra in mensagem:
    sys.stdout.write(letra)
    sys.stdout.flush()
    #sleep(0.2)
print()

# setando as opções de menu
opcoes_de_menu = ["sign in", "sign up", "fale conosco"]

# imprimindo menu de opçoes

count = 1

for opcao in opcoes_de_menu:
    print(f"[{count}] - {opcao}")
    count += 1  # count = count +1

# prompt
opcao_digitada = input("Qual opção deseja? ")

#abrindo arquivo CSV  para leitura
with open("db.csv") as arquivo:
    print(arquivo.read(1))