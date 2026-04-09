import os
import subprocess

def executar_comando(comando):
    try:
        result = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro.", e)

def ping():
    executar_comando("ping 8.8.8.8")

def notepad():
    executar_comando("notepad")

def calculadora():
    executar_comando("calc")

def tempo():
    executar_comando("time")

def painel():
    executar_comando("control panel")

menu = input("==========MENU - PROMPT==========\n1 — Ping\n2 — Notepad\n3 — Calculadora\n4 — Tempo\n5 — Painel de controle\n=========================\n")
match menu:
    case "1":
        ping()
    case "2":
        notepad()
    case "3":
        calculadora()
    case "4":
        tempo()
    case "5":
        painel()
    case _:
        print ("Opção inválida.")

menu