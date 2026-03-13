import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar o comando.",e)

def mostrar_ip():
    executar_comando("ipconfig")

def renovar_ip():
    executar_comando("ipconfig /renew")

def mostrar_ip_completo():
    executar_comando("ipconfig /all")

def ping_host():
    host = str(input("Digite o IP ou HOSTNAME: "))
    executar_comando(f"ping {host}")    

def menu():
    while True:
        print("=========Ferramenta de Rede=========")
        print("1 - Mostrar IP")
        print("2 - Renovar IP")
        print("3 - Mostrar configurações de rede completa")
        print("4 - Ping")
        print("0 - Sair")
        print("=========Criado por: Victor=========")
        opcao = str(input("Escolha: "))

        match opcao:
            case "1":
                mostrar_ip()
            case "2":
                renovar_ip()
            case "3":
                mostrar_ip_completo()
            case "4":
                ping_host()
            case "0":
                print("Saindo.")
                break
            case _:
                print("Erro.")
if __name__ == "__main__":
    menu()