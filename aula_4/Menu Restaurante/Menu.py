def ler_banco():
    # data sanitation
    """essa função lê um banco de dados"""
    with open("estoque.csv", "r") as file:
        dados_do_banco = file.read()
        dados_do_estoque = dados_do_banco.split("\n")
        menu = dados_do_estoque[0].split(",")
        quantidade_no_estoque = dados_do_estoque[1].split(",")
        return menu, quantidade_no_estoque

itens_menu = ler_banco()[0]
estoque_menu = ler_banco()[1]

print("<<<< Faça seu pedido: >>>>")

for posição, item in enumerate(itens_menu):
    print(f"[{posição + 1}] - {item}")
    

pedido = int(input(">>>> "))
#input sempre retorna texto

tamanho_menu = len(itens_menu) #len sempre retorna numeros inteiros

if pedido > tamanho_menu or pedido < 1:
    print("Opção inválida")
# mascara dop input 
pedido = pedido - 1 # pedido -=1
estoque_menu[pedido] = str(int(estoque_menu[pedido]) - 1)

with open("estoque.csv", "w") as file:
    file.write(",".join(itens_menu))
    file.write("\n")
    file.write(",".join(estoque_menu))
    
    
# opcoes = ["cha", "chocolate quente", "espresso", "capuccino", "pingado"]

# for posicao, opcao in enumerate(opcoes):
#    print(f"*[{posicao + 1}]* - {opcao}")
    
# pedido = input("Selecione uma das opções acima: ")