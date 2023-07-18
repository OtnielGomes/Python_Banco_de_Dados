from Sistema.Lib.Interface import*
from Sistema.Lib.Arquivo import*
from colorama import init, Fore, Back, Style
from time import sleep
arq = 'pessoascadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    menu(['Ver Pessoas Cadastradas',
          'Cadastrar Novas Pessoas',
          'Sair do Sistema'])
    opc = verificaInt(Fore.BLUE + Back.LIGHTBLACK_EX + 'Escolha sua Opção: '
                      + Style.RESET_ALL)
    if opc == 1:
        lerArquivo(arq)
        sleep(3)
    elif opc == 2:
        textform('Cadastro de Novas Pessoas: ')
        nome = str(input('Digite o Nome: '))
        idade = verificaInt('Digite a idade:')
        cadastrar(arq, nome, idade)
    elif opc == 3:
        textform('Saindo do SISTEMA ...')
        sleep(3)
        break
    elif opc == 0:
        break
    else:
        print(Fore.RED + Back.BLACK + 'Opção inválida. Tente novamente'
              + Style.RESET_ALL)


