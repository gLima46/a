#!/bin/bash

PURPLE='0;35'
NC='\033[0m' 
VERSAO=11
	
echo  "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) Olá caro Usuário, serei seu assistente para instalação do Java!;"
echo  "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) Estarei Verificando aqui se você possui o Java instalado...;"

java -version
if [ $? -eq 0 ]
	then
	    echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) : Olha que surpresa boa"
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) : Você já possui o java instalado!!"
	else
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Opa! Pelo que eu vejo aqui você não possui nenhuma versão do Java instalado."
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Sem problemas, irei resolver isso agora!"
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Só antes preciso da sua permissão para realmente instalar o Java (S/N)?"
	read inst
	if [ \"$inst\" == \"s\" ]
		then
			echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Ok! Vamos nessa ;D"
			echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Instalando 0 Java ;D"
			echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Adicionando o repositório!"
			sleep 2
			sudo add-apt-repository ppa:webupd8team/java -y
			clear
			echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Atualizando! Falta pouco."
			sleep 2
			sudo apt update -y
			clear
			
			if [ $VERSAO -eq 11 ]
				then
					echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) Preparando para instalar a versão 11 do Java. Confirme a instalação quando solicitado ;D"
					sudo apt install default-jre ; apt install openjdk-11-jre-headless; -y
					clear
					echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7) Java instalado com sucesso!"
				fi
		else 	
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Que pena você optou por não instalar o Java por enquanto"
		echo "$(tput setaf 10)[Bot assistant]:$(tput setaf 7)  Até breve, espero te ver logo"
	fi
fi
stop 10
# ===================================================================
# Todos direitos reservados para o autor: Dra. Profa. Marise Miranda.
# Sob licença Creative Commons @2020
# Podera modificar e reproduzir para uso pessoal.
# Proibida a comercialização e a exclusão da autoria.
# ===================================================================
