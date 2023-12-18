import os

restaurantes = [{"nome":"Praça","categoria":"Japonesa","ativo":False},
                {"nome":"Pizza Suprema","categoria":"Pizza","ativo":True},
                {"nome":"Cantina","categoria":"Italiano","ativo":False}
]

def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''

    print("Sabor Express\n")

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    os.system("cls")
    linha = "*" * len(texto)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
        
    input ("\nDigite uma recla para voltar ao menu principal: ")
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print (f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso.")
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''

    exibir_subtitulo("Lista de restaurantes cadastrados")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status".ljust(20)}")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] == True else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}")

    voltar_ao_menu_principal()

def ativar_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo("Ativar restaurantes")

    nome_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]

            mensagem = f"\nO restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] == True else f"\nO restaurante {nome_restaurante} foi desativado com sucesso"

            print (mensagem)

    if not restaurante_encontrado:
        print("\nRestaurante não encontrado")

    voltar_ao_menu_principal()

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''

    exibir_subtitulo("Encerrando o aplicativo")

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    exibir_subtitulo("Opção Invalida")
    
    voltar_ao_menu_principal()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input("Digite uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()            

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            ativar_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()

