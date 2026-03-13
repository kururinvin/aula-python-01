import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar o comando.",e)

def tasklist():
    executar_comando("tasklist")

def systeminfo():
    executar_comando("systeminfo")

def netstat():
    executar_comando("netstat")

def time():
    executar_comando("time")    

def ver():
    executar_comando("ver")      

def calc():
    executar_comando("calc")      

def controlpanel():
    executar_comando("control panel")      

def data():
    executar_comando("date")    

def notepad():
    executar_comando("notepad")    

def shutdown():
    executar_comando("shutdown")    

def menu():
    while True:
        print("=========Ferramenta de Rede=========")
        print("1 - Tasklist")
        print("2 - Systeminfo")
        print("3 - Netstat")
        print("4 - Horário")
        print("5 - Versão do Windows")
        print("6 - Calculadora")
        print("7 - Painel de controle")
        print("8 - Data")
        print("9 - Bloco de notas")
        print("10 - SHUTDOWN (CUIDADO!!)")
        print("0 - Sair")
        print("=========Criado por: Victor=========")
        opcao = str(input("Escolha: "))

        match opcao:
            case "1":
                tasklist()
            case "2":
                systeminfo()
            case "3":
                netstat()
            case "4":
                time()
            case "5":
                ver()
            case "6":
                calc()
            case "7":
                controlpanel()
            case "8":
                data()
            case "9":
                notepad()
            case "10":
                shutdown()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Erro.")
if __name__ == "__main__":
    menu()