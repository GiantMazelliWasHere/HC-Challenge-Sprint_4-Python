# importando bibliotecas
import pandas as pd

# função para leitura de arquivos json
def leitura_json(json_file):
    
    print('Leitura finalizada!\n')
    return pd.read_json(f'{json_file}.json', lines=True)

# função para filtrar os dados da coluna do dataframe passada pelo usuario entre sim e não
def classificar(tipo, input_usuario):
    
    if input_usuario == 'Sim':
        
        return df[df[tipo]=='sim']
    
    elif input_usuario == 'Não':
        
        return df[df[tipo]=='nao']

# função para definir a coluna que levara a clasificação da função classificar
def definir_tipo(tipo): 
    
    if tipo == 'Instrumento':
        
        print(f'Qual será a classificação desejada para o {tipo}?\n')
        usuario = input('Sim, Não ou Finalizar: ').capitalize()
        resumo.append(usuario)
        
        df = classificar('tocar instrumento', usuario)
        return df
    
    elif tipo == 'Piadas':
        
        print(f'Qual será a classificação desejada para o {tipo}?\n')
        usuario = input('Sim, Não ou Finalizar: ').capitalize()
        resumo.append(usuario)
        
        df = classificar('piadas', usuario)
        return df
    
    elif tipo == 'Fantasia':
        
        print(f'Qual será a classificação desejada para o {tipo}?\n')
        usuario = input('Sim, Não ou Finalizar: ').capitalize()
        resumo.append(usuario)
        
        df = classificar('fantasia', usuario)
        return df
    
    elif tipo == 'Palhaço':
        
        print(f'Qual será a classificação desejada para o {tipo}?\n')
        usuario = input('Sim, Não ou Finalizar: ').capitalize()
        resumo.append(usuario)
        
        df = classificar('palhaco', usuario)
        return df
    
    else:
        
        print('Classificação inválida')

# função para converter o arquivo para o formato desejado
def conversor_arquivo(formato, arquivo, arquivo_novo):
    if formato == 'excel':
        arquivo.to_excel(f'{arquivo_novo}.xlsx', index=False)
        print('Arquivo convertido com sucesso!')
    elif formato == 'csv':
        arquivo.to_csv(f'{arquivo_novo}.csv', index=False)
        print('Arquivo convertido com sucesso!')
    elif formato == 'json':
        arquivo.to_json(f'{arquivo_novo}.json', orient='records', lines=True)
        print('Arquivo convertido com sucesso!')
    else:
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

# informando ao usuario que o programa esta lendo o arquivo json
print('LENDO AQUIVO JSON....\n')

# input do usuario para o nome do arquivo json  
json = input('Digite o nome do arquivo JSON: ')
# adicionando a resposta do usuario a lista resumo
resumo.append(f'O usuario leu o arquivo {json}.json')
# Usamos a função try para tratarmos de possíveis erros que possam ocorrer ao tentar ler o arquivo json
try:
    # chamando a função leitura_json para ler o arquivo json e amarzenando-a numa variavel
    df = leitura_json(json)
# tratamento de erro para caso o arquivo não seja encontrado
except FileNotFoundError:
    # print para informar ao usuario que o arquivo não foi encontrado e algumas diretizes para verificar o porque dele não ter sido encontrado
    print(f'Arquivo: {json}.json não encontrado!\n')
    print('Verifique se o mesmo existe, se o nome foi digitado corretamente ou se encontra na pasta correta.')

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

# loop para classificar os dados do dataframe até o usuario digitar 'Finalizar'
while usuario != 'Finalizar':
    # menu de opções para o usuario escolher o tipo de classificação
    print('TIPOS:\n - Instrumento\n - Piadas\n - Fantasia\n - Palhaço\n - Finalizar\n')
    
    # input do usuario para escolher o tipo de classificação
    usuario = input('Digite o tipo: ').capitalize()
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
usuario = input('Digite o formato: ').lower()
# adicionando a resposta do usuario a lista resumo
resumo.append(f'O usuario realizou uma corvesão de arquivo para o formato {usuario}')
# setando o df como o parametro arquivo para a função conversor_arquivo
arquivo = df
# input do usuario para o nome do novo arquivo
arquivo_novo = input('Digite o nome do novo arquivo: ')
# chamando a função conversor_arquivo para converter o arquivo para o formato desejado
conversor_arquivo(usuario, arquivo, arquivo_novo)

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