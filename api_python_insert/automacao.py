import random
import mysql.connector
from connectdb import *
from credentials import usr, pswd

count = 0
repeticao = 0
jogo = True
print('Digite seu nome: ')
nome = input()
print('='*10,'BEM VINDO ','='*10)
numero = int(input('DIGITE NÚMEROS DE 1 A 10: '))
while count < 10:
 num = random.randint(1,10)
 if(numero == num):
    repeticao = repeticao + 1
 count = count + 1
print("Fim de jogo, o número escolhido se repetiu", repeticao)
insert_db(nome,repeticao)

