from colorama import init, Fore, Back, Style
init()
def linha(tam=40):
    """
    Cria uma linha de acordo com o tamanho selecionado
    :param tam: Define o tamanho da linha a ser criada
    :return: Retorna a linha em formato de print com o tamanho
    selecionado
    """
    return '-' * tam


def textform(text=''):
    print(linha())
    print(Fore.BLUE + Back.LIGHTWHITE_EX + text.center(len(linha()))
          + Style.RESET_ALL)
    print(linha())


def menu(lista):
    textform('Menu Principal')
    c = 1
    for item in lista:
        print(Fore.YELLOW + Back.BLACK + f' {c} ' + Style.RESET_ALL + ' - '
              + Fore.CYAN + f'{item}' + Style.RESET_ALL)
        print()
        c += 1
    print(linha())


def verificaInt(text=''):
    while True:
        try:
            num = int(input(text))
        except (ValueError, TypeError):
            print(Fore.RED + 'Opção inválida. Por favor digite um número.'
                  + Style.Reset_ALL)
        except KeyboardInterrupt:
            print(Fore.RED + 'Digitação interrompida pelo o usuário.'
                  + Style.RESET_ALL)
            return 0
        else:
            return num





