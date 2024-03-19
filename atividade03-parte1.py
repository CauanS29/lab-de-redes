#!/usr/bin/python

import os
import subprocess
import socket

SERVIDORNOMEIP = "192.0.2.100"
SERVIDORNOMEPORTA = 53
SERVIDOR_WEB_IP = "192.168.1.101"
SERVIDOR_WEB_PORTA = 80

def imprimir_informacoes_servico():
    print("Servidor de Nome:", SERVIDOR_NOME_IP + ":" + str(SERVIDOR_NOME_PORTA))
    print("Servidor Web:", SERVIDOR_WEB_IP + ":" + str(SERVIDOR_WEB_PORTA))

def iniciar_captura_trafego():
    nome_arquivo = "captura_trafego_VictorChagas.pcap"
    print("Iniciando captura de trafego...")
    os.system("sudo tcpdump -i any -w " + nome_arquivo + " &")

def testar_conectividade_host(endereco_ip):
    resposta = os.system("ping -c 1 " + endereco_ip)
    if resposta == 0:
        print("O host", endereco_ip, "está online.")
    else:
        print("O host", endereco_ip, "esta offline.")

def testar_resposta_servico(endereco_ip, porta, nome_servico):
    print("Testando servico", nome_servico, "...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        resultado = s.connect_ex((endereco_ip, porta))
        if resultado == 0:
            print("O servico", nome_servico, "está respondendo corretamente.")
        else:
            print("Nao foi possivel conectar ao servico", nome_servico)
    finally:
        s.close()

def encerrar_captura_trafego():
    print("Encerrando captura de trafego...")
    os.system("sudo pkill tcpdump")

def main():
    imprimir_informacoes_servico()
    iniciar_captura_trafego()

    testar_conectividade_host(SERVIDOR_NOME_IP)
    testar_resposta_servico(SERVIDOR_NOME_IP, SERVIDOR_NOME_PORTA, "de Nome")

    testar_conectividade_host(SERVIDOR_WEB_IP)
    testar_resposta_servico(SERVIDOR_WEB_IP, SERVIDOR_WEB_PORTA, "Web")

    encerrar_captura_trafego()

if __name == "__main":
    main()
