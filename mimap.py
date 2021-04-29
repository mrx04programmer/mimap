#! /usr/bin/env python
import os,sys
import argparse
W = '\033[37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray
#Logo
def banner():
    print("""
              $$\                                   
              \__|                                  
$$$$$$\$$$$\  $$\ $$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$  _$$  _$$\ $$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ / $$ / $$ |$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ | $$ | $$ |$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | $$ | $$ |$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__| \__| \__|\__|\__| \__| \__| \_______|$$  ____/ 
                                          $$ |      
                                          $$ |      
                                          \__|     By Mrx04programmer 
""")
#Opciones
parse = argparse.ArgumentParser()
parse.add_argument("-i", "--ip",help="IP/Dominio Objetivo")
parse.add_argument("-m", "--module", help="Establecer modulo a usar")
parse.add_argument("-l", "--list",help="Mostar lista de modulos( -l L)")
parse = parse.parse_args()
#Modules
def mod_os():
    print(B+"[*] "+W+"Resultados del sistema operativo de "+parse.ip+":")
    os.system("sudo nmap -T4 -O "+parse.ip+" -oG so_"+parse.ip)
def spoofing():
    ipomac = input(B+"Que tipo de objetivo es (Mac/Ip)[M/i] ")
    if ipomac == "Mac" or ipomac == "m" or ipomac == "M":
        action = input(C+"comandos a correr en "+parse.ip+" (ej: -O -T5 8.8.8.8) > "+W)
        os.system("nmap --spoof-mac "+parse.ip+" "+action)
    else:
        action = input(C+"comandos a correr en "+parse.ip+" (ej: -O -T5 8.8.8.8) > "+W)
        os.system("nmap -S "+parse.ip+" "+action)

os.system("clear")
banner()
#if parse.
if parse.list:
    print(P+"Lista de modulos")
    print(W+"""
    os : Buscar información del sistema operativo del objetivo
    scan : Escanear y encontrar puertos abiertos en el objetivo
    scanB : Escanear bruscamente para encontrar puertos abiertos en el objetivo
    spoofing : Correr otro modulo con señuelos para el ataque de evaciones
    http : Ver peticiones HTTP de una IP 

    """)
    exit()
if parse.module == "os":
    mod_os()
    exit()
if parse.module == "spoofing":
    spoofing()
    exit()
if parse.module == "scan":
    print(G+"[X] "+W+"Buscando puertos en "+parse.ip)
    os.system("sudo ./s "+parse.ip)
