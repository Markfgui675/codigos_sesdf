import pandas as pd

nomes = [['central', '15'], ['centro-sul', '16'], ['leste', '17'], ['norte', '18'], ['oeste', '19'], ['sudoeste', '20'], ['sul', '21']]

for n in nomes:
    nome_arquivo_recebido = f'{n[0]}.csv'
    nome_arquivo_gerado = f'dados_{n[0]}'
    caminho_arquivo_recebido = 'superintendencias\srs\dados_recebidos'
    caminho_arquivo_gerado = 'superintendencias\srs\dados_tratados'

    df = pd.read_csv(f'{caminho_arquivo_recebido}\{nome_arquivo_recebido}')
    coluna = list(df.columns)[0]

    numero1 = n[1][0]
    numero2 = n[1][1]
    new_list = []

    for index, row in df.iterrows():
        l = row[0].split(' ', 1)
        restante = l[0][2:]
        l[0] = ''
        l[0]+=numero1+numero2+restante
        new_list.append(f'{l[0]} {l[1]}')
    
    
    dados = pd.DataFrame(
        {
            coluna:new_list
        }
    )

    dados.to_excel(f'{caminho_arquivo_gerado}\{nome_arquivo_gerado}.xlsx', index=False)
    dados.to_csv(f'{caminho_arquivo_gerado}\{nome_arquivo_gerado}.csv', index=False)

