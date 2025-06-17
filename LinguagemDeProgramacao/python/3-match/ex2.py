# Crie um programa que:

# Peça ao usuário para digitar um dia da semana.
# Use match para exibir qual é o prato do dia.

# Mostre uma mensagem especial se for fim de semana.

dia = input("Digite um dia da semana (segunda, terça, quarta, quinta, sexta, sábado, domingo): ").strip().lower()

match dia:
    case "segunda"  "terça":
        print("Prato do dia: Feijoada")
    case "quarta" | "quinta":
        print("Prato do dia: Lasanha")
    case "sexta":
        print("Prato do dia: Pizza")
    case "sábado" | "domingo":
        print("Prato do dia: Churrasco")
        print("Aproveite o fim de semana!")
    case _:
        print("Dia inválido!")  
        