from Sistema.Lib.Interface import*
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError, FileExistsError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt+' )
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        return f'Arquivo {nome} criado com sucesso.'


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o aquivo')
    else:
        textform('Pessoas cadastradas')
        print(f'{"Nome: ":<30}{"Idade: ":>10}')
        for line in a:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, nome, idade) :
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo para cadastro.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro na escrita do arquivo.')
        else:
            print(f'Cadastro de {nome} criado com sucesso.')
        finally:
            a.close()






