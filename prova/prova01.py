menu = input("==========MENU==========\n       Confirmar?\n— Sim\n— Não\n=========================\n")
match menu:
    case "Sim":
        print("Confirmado com sucesso")
    case "Não":
        print("Negado com sucesso.")
    case _:
        print("Responda apenas com sim ou não.")

menu