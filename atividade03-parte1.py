#!/usr/bin/python

import os
import socket

servidorNomeIp = "192.0.2.100"
servidorNomePorta = 53
servidorWebIp = "192.168.1.101"
servidorWebPorta = 80

def main():
    print "Informacoes dos Servidores:"
    print "Servidor de Nome: %s:%d" % (servidorNomeIp, servidorNomePorta)
    print "Servidor Web: %s:%d" % (servidorWebIp, servidorWebPorta)
    
    nomeArquivoCaptura = "captura_Cauan_Santos.pcap"    
    print "Iniciando a captura"
    os.system("sudo tcpdump -i any -w %s &" % nomeArquivoCaptura)
    
    respostaPingNome = os.system("ping -c 1 %s" % servidorNomeIp)
    if respostaPingNome == 0:
        print "O servidor de nome %s esta acessivel." % servidorNomeIp
    else:
        print "O servidor de nome %s nao esta acessivel." % servidorNomeIp
    
    print "Verificando a resposta do servico de nome..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        resultadoConexaoNome = s.connect_ex((servidorNomeIp, servidorNomePorta))
        if resultadoConexaoNome == 0:
            print "O servico de nome esta respondendo corretamente."
        else:
            print "Nao foi possivel estabelecer conexao com o servico de nome."
    finally:
        s.close()
    
    respostaPingWeb = os.system("ping -c 1 %s" % servidorWebIp)
    if respostaPingWeb == 0:
        print "O servidor web %s esta acessivel." % servidorWebIp
    else:
        print "O servidor web %s nao esta acessivel." % servidorWebIp
    
    print "Verificando a resposta do servico web..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        resultadoConexaoWeb = s.connect_ex((servidorWebIp, servidorWebPorta))
        if resultadoConexaoWeb == 0:
            print "O servico web esta respondendo corretamente."
        else:
            print "Nao foi possivel estabelecer conexao com o servico web."
    finally:
        s.close()
    
    print "Encerrando a captura"
    os.system("sudo pkill tcpdump")

if __name__ == "__main__":
    main()
