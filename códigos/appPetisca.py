import os

restaurantes = [{'nome':'Petisca', 'categoria':'Carnes','atividade':False}]

def inicio():
    '''
    Esta função exibe o nome do app de forma estilizada
    
    '''
    print('''█▀▀█ █▀▀ ▀▀█▀▀ ░▀░ █▀▀ █▀▀ █▀▀█ 
█░░█ █▀▀ ░░█░░ ▀█▀ ▀▀█ █░░ █▄▄█ 
█▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ''')

def escolher_opcao():
    '''
    Esta função esxibe as opções do app para o usuário
    
    '''
    print('''[1] Cadastrar restaurante
[2] Listar restaurante
[3] Alternar estado do restaurante
[4] Finalizar''')

def finalizar_app():
    '''
    exibe mensagem de finalização do app
    
    '''
    exibir_subtitulo('Sistema finalizado!')
    print('ʕ•́ᴥ•̀ʔっ')

def opcao_invalida():
    '''
    Esta funçao é utilizada quando o usuário digita uma opção inexistente
    exibe mensagem de opção inválida e retorna ao menu inicial
    
    output:
    - retorna ao meu inicial
    
    '''
    print('Opção inválida')
    voltar_ao_menu_inicial()

def exibir_subtitulo(texto):
    ''' 
    Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo

    '''
    os.system('cls')
    linha = '-' *(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()    

def voltar_ao_menu_inicial():
    '''
    O input solicita ao usuário qualquer tecla para que volte ao main
    Outputs:
    - Retorna ao menu principal
    
    '''
    input('--> Digite qualquer tecla para retornar ao menu: ')
    main()

def cadastrar_restaurante():
    '''
    Efetua o cadastro de restaurantes

    inputs:
    - nome restaurante;
    -categoria.
    
    Outputs:  
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('--> Digite o nome do resturante: ')
    categoria = input('- Digite a categoria do restaurante: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria,'atividade':False}
    restaurantes.append(dados_restaurante)
    print(f'\nRestaurante {nome_restaurante} cadastrado com sucesso!')
    voltar_ao_menu_inicial()

def listar_restaurantes():
    '''
    Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista dos restaurantes cadastrados
    
    '''
    exibir_subtitulo('Listando todos os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Atividade'.ljust(20)}\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        atividade = 'Ativo' if restaurante['atividade'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {atividade.ljust(20)}')
    voltar_ao_menu_inicial()

def alternar_atividade():
    '''
    Alterna a atividade dos restaurantes (True/False)
    input: 
    - nome do restaurante.
    Outputs:
    - Exibe mensagem indicando o sucesso da operação

    '''
    exibir_subtitulo('Ativação e Desativação de Restaurantes')
    nome_restaurante = input('Digite o  nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['atividade'] = not restaurante['atividade']
            mensagem = f'Restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['atividade'] else f'O restaurante {nome_restaurante} foi desaativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_inicial()


def analize_de_opcao():
    '''
    Solicita e executa a opção escolhida pelo usuário
    Outputs:
    - Executa a opção escolhida pelo usuário

    '''
    try:
        opcao_escolhida = int(input('Escolha a opção desejada: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_atividade()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
            
def main():
    '''
    Função principal que inicia o programa
    
    '''
    os.system('cls')
    inicio()
    escolher_opcao()
    analize_de_opcao()

if __name__ == '__main__':
    main()