# importando bibliotecas
import pandas as pd

# função para leitura de arquivos json
def leitura_json(json_file):
    # input para deixar o nome do arquivo em caixa baixa
    json = json_file.lower()
    # print para informar ao usuario que o arquivo foi lido com suecesso
    print('Leitura finalizada!\n')
    # retornando o arquivo json lido
    return pd.read_json(f'{json}.json', lines=True)

# função para filtrar os dados da coluna do dataframe passada pelo usuario entre sim e não
def classificar(tipo, input_usuario):
    # condição para verificar se o input do usuario é sim
    if input_usuario == 'Sim':
        
        return df[df[tipo]=='sim']
    # condição para verificar se o input do usuario é não
    elif input_usuario == 'Não':
        
        return df[df[tipo]=='nao']

# função para definir a coluna que levara a clasificação da função classificar
def definir_tipo(tipo):
    tipos = ['Instrumento', 'Piadas', 'Fantasia', 'Palhaço'] 
    
    # loop para verificar se o tipo digitado pelo usuario é valido
    while tipo in tipos:
        # loop para verificar se o tipo digitado pelo usuario é valido
        for t in tipos:
            # condição para verificar o tipo de classificação que o usuario deseja
            if tipo == t:
                print(f'Qual será a classificação desejada para o {t}?\n')
                usuario = input('Sim, Não ou Finalizar: ').capitalize()
                resumo.append(usuario)
                
                t_class = t.lower()
                df = classificar(t_class, usuario)
                return df 
            # condição para informar que a classificação digitada pelo usuario é inválida
            else:
            
                print('Classificação inválida')
    print('Tipo inválido')

# função para converter o arquivo para o formato desejado
def conversor_arquivo(formato, arquivo, arquivo_novo):
    # condição para verificar o formato de conversão que o usuario deseja
    if formato == 'excel':
        # convertendo o arquivo para excel
        arquivo.to_excel(f'{arquivo_novo}.xlsx', index=False)
        print('Arquivo convertido com sucesso!')
    elif formato == 'csv':
        # convertendo o arquivo para csv
        arquivo.to_csv(f'{arquivo_novo}.csv', index=False)
        print('Arquivo convertido com sucesso!')
    elif formato == 'json':
        # convertendo o arquivo para json
        arquivo.to_json(f'{arquivo_novo}.json', orient='records', lines=True)
        print('Arquivo convertido com sucesso!')
    else:
        # print para informar ao usuario que o formato digitado é inválido
        print('Formato inválido')

# print para inciar o programa com uma tela inicial estilizada e menu de opções
print('█▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒█▒▒▒█▒▒███▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█████▒▒▒█▒▒▒████▒▒█▒▒███▒▒▒███▒▒█')
print('█▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒█▒▒▒█▒██▒▒█▒▒▒█▒▒▒▒█▒█▒▒█▒▒▒█▒▒▒█▒▒▒█▒█▒▒▒▒▒█')
print('█▒▒█▒█▒▒█▒▒▒█▒█▒▒▒▒█▒▒▒█▒█▒█▒█▒▒▒█▒▒▒█▒▒▒█▒█▒▒▒█▒█▒█▒▒▒█▒▒███▒▒█')
print('█▒▒█▒█▒▒█▒▒▒█▒█▒▒▒▒█▒▒▒█▒█▒▒██▒▒▒█▒▒▒█████▒████▒▒█▒█▒▒▒█▒▒▒▒▒█▒█')
print('█▒▒▒█▒▒▒▒███▒▒████▒▒███▒▒█▒▒▒█▒▒▒█▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒███▒▒▒███▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄█')
print('\n')
print('- Começar \n')
print('- Finalizar\n')

# lista para armazenar as respostas do usuario
resumo = []

# input do usuario para iniciar o programa
usuario = input('Resposta: ').capitalize()
# adicionando a resposta do usuario a lista resumo
resumo.append(usuario)

# tela de inicio da classificação dos dados
print('█▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒█▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒████▒█▒▒▒▒▒▒▒█▒▒▒▒███▒▒███▒▒█▒█████▒█▒▒████▒▒▒█▒▒▒▒████▒▒▒█▒▒▒█████▒█')
print('█▒█▒▒▒▒▒█▒▒▒▒▒▒█▒█▒▒█▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒▒▒▒▒█▒█▒▒█▒▒▒▒▒▒█▒█▒▒█▒▒▒█▒█')
print('█▒█▒▒▒▒▒█▒▒▒▒▒█▒▒▒█▒▒███▒▒███▒▒█▒█████▒█▒█▒▒▒▒▒█▒▒▒█▒█▒▒▒▒▒█▒▒▒█▒█▒▒▒█▒█')
print('█▒█▒▒▒▒▒█▒▒▒▒▒█████▒▒▒▒▒█▒▒▒▒█▒█▒█▒▒▒▒▒█▒█▒▒▒▒▒█████▒█▒▒▒▒▒█████▒█▒▒▒█▒█')
print('█▒▒████▒█████▒█▒▒▒█▒▒███▒▒███▒▒█▒█▒▒▒▒▒█▒▒████▒█▒▒▒█▒▒████▒█▒▒▒█▒█████▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄█')

# Condição para iniciar o programa apenas se o usuario digitar 'Começar'
if usuario == 'Começar':
    # loop para rodar o programa até o usuario digitar finalizar
    while usuario != 'Finalizar':
        
        # informando ao usuario que o programa esta lendo o arquivo json
        print('LENDO AQUIVO JSON....\n')
        # input do usuario para o nome do arquivo json  
        usuario = input('Digite o nome do arquivo JSON ou Finalizar: ').capitalize()
        # adicionando a resposta do usuario a lista resumo
        if usuario == 'Finalizar':
            resumo.append(usuario)
        else:
            resumo.append(f'O usuario leu o arquivo {usuario}.json')
        
        # Usamos a função try para tratarmos de possíveis erros que possam ocorrer ao tentar ler o arquivo json
        try:
            # chamando a função leitura_json para ler o arquivo json e amarzenando-a numa variavel
            df = leitura_json(usuario)
        # tratamento de erro para caso o arquivo não seja encontrado
        except FileNotFoundError:
            # print para informar ao usuario que o arquivo não foi encontrado e algumas diretizes para verificar o porque dele não ter sido encontrado
            print(f'Arquivo: {usuario}.json não encontrado!\n')
            print('Verifique se o mesmo existe, se o nome foi digitado corretamente ou se encontra na pasta correta.')
            break
            
        # menu de opções para o usuario escolher o tipo de classificação
        print('TIPOS:\n - Instrumento\n - Piadas\n - Fantasia\n - Palhaço\n - Finalizar\n')
        # input do usuario para escolher o tipo de classificação
        usuario = input('Digite o tipo ou finalize o programa: ').capitalize()
        # adicionando a resposta do usuario a lista resumo
        resumo.append(usuario)
        
        # chamando a função definir_tipo para classificar os dados do dataframe
        if usuario != 'Finalizar':
            df = definir_tipo(usuario)
        else:
            # finalizando o loop
            print('Finalizando....')
            usuario = 'Finalizar'
            
        # print para informar ao usuario que estamos entrando na área de conversão de arquivos
        print('CONVERTENDO ARQUIVO....\n')
        # lista de formatos disponiveis para o usuario escolher
        print('FORMATOS:\n - excel\n - csv\n - json\n')
        # input do usuario para escolher o formato de conversão
        usuario = input('Digite o formato ou finalize o programa: ').lower()
        # adicionando a resposta do usuario a lista resumo
        resumo.append(f'O usuario realizou uma corvesão de arquivo para o formato {usuario}')
        
        # setando o df como o parametro arquivo para a função conversor_arquivo
        arquivo = df
        
        # input do usuario para o nome do novo arquivo
        arquivo_novo = input('Digite o nome do novo arquivo: ')
        resumo.append(f'O usuario nomeou o novo arquivo como {arquivo_novo}')
        # chamando a função conversor_arquivo para converter o arquivo para o formato desejado
        conversor_arquivo(usuario, arquivo, arquivo_novo)
        usuario = input('Deseja continuar? ').capitalize()
        resumo.append(usuario)
        if usuario == 'Não':
            usuario = 'Finalizar'
        else:
            continue
# condição para finalizar o programa caso o usuario digite 'Finalizar'        
elif usuario == 'Finalizar':
    print('Finalizando....')
# condição para caso o usuario digite uma opção inválida
else:
    print('Opção inválida')
    print('Finalizando....')

# print do resumo de açôes realizadas pelo usuario
print(resumo)

# print para finalizar o programa com uma tela final estilizada
print('█▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀██▀▀█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▒█████▒█▒█▒▒▒█▒▒▒█▒▒▒█▒▒▒▒▒█▒█████▒▒▒█▒▒▒███▒▒▒▒█████▒█')
print('█▒█▒▒▒▒▒▒▒██▒▒█▒▒█▒█▒▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒█▒▒█▒▒██▒▒█▒▒▒█▒█')
print('█▒█████▒█▒█▒█▒█▒█▒▒▒█▒█▒▒▒▒▒█▒▒▒█▒▒▒█▒▒▒█▒█▒▒▒▒█▒█▒▒▒█▒█')
print('█▒█▒▒▒▒▒█▒█▒▒██▒█████▒█▒▒▒▒▒█▒▒█▒▒▒▒█████▒█▒▒██▒▒█▒▒▒█▒█')
print('█▒█▒▒▒▒▒█▒█▒▒▒█▒█▒▒▒█▒█████▒█▒█████▒█▒▒▒█▒███▒▒▒▒█████▒█')
print('█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█')
print('█▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄██▄▄█')