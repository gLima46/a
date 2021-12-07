import random as rdm
import psutil
import time
from functools import reduce
from connectAuto import *
from connectBot import *
import mysql.connector
from credentials import usr, pswd

var = 0

def pegarDados():
    print('='*10, 'INÍCIO DAS MEDIÇÕES', '='*10)
    print('-'*10, 'Ctrl+C para parar', '-'*10, '\n')

    try:
        discretizacao = 30
        cont = 1

        qntDeMaquinasTotais()

        while True:

            disco = psutil.disk_usage('/').percent
            ram = psutil.virtual_memory().percent
            cpu = psutil.cpu_percent()
            temperatura = 40 + (cpu * 0.6)
            dataCaptura = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


            for row in funcMaquinas():
                fkMaquinas = row
                    
                valorRandom = round(rdm.random()+1.01,1)

                discoRandom = valorRandom * disco
                ramRandom = valorRandom * ram
                temperaturaRandom = valorRandom * temperatura
                cpuRandom = valorRandom * cpu

                if discoRandom > 100:
                    discoRandom = 100
                if ramRandom > 100:
                    ramRandom = 100
                if cpuRandom > 100:
                    cpuRandom = 100

                if(row == 1):
                    print("\n| Maquina: ", fkMaquinas, 
                    "| Disco:", float('{0:.2f}'.format(disco)),
                    "| Ram:",float('{0:.2f}'.format(ram)),
                    "| CPU:",float('{0:.2f}'.format(cpu)),
                    "| temperatura:",float('{0:.2f}'.format(temperatura)),
                    "| Date:",dataCaptura)
                else:
                    print("\n| Maquina: ", fkMaquinas, 
                    "| Disco:", float('{0:.2f}'.format(discoRandom)),
                    "| Ram:",float('{0:.2f}'.format(ramRandom)),
                    "| CPU:",float('{0:.2f}'.format(cpuRandom)),
                    "| Temperatura:",float('{0:.2f}'.format(temperaturaRandom)),
                    "| Date:",dataCaptura)
                    

                if discoRandom >= 30 or ramRandom >= 100 or cpuRandom >= 50:
                    cont = 3
                if cont == 3:
                    if(row == 1):
                        insert_db(fkMaquinas, disco, ram, cpu, temperatura)
                    else:
                        insert_db(fkMaquinas, discoRandom, ramRandom, cpuRandom, temperaturaRandom)

                    cont = 0
                
                global var
                if(row == 1):
                    var = verificacao(fkMaquinas, disco, ram, cpu)
                else:
                    var = verificacao(fkMaquinas, discoRandom, ramRandom, cpuRandom) 

            print("\n")

            time.sleep(discretizacao)
            cont += 1


    except KeyboardInterrupt:
        pass


def enviarDados():
    return var