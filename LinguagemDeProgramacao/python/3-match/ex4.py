clima = int(input("Como está o dia? (1 - ensolarado, 2 - nublado, 3 - chuvoso, 4 - nevando): "))  

match clima:
    case 1 | 2:
        print("Dia bom para sair!")
    case 3 | 4:
        print("Dia ruim para sair!")
    case _:
        print("Opção inválida, tente novamente!")