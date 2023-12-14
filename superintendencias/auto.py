import pandas

nomes = ['ajl', 'cont', 'fsdf', 'gab', 'sais', 'sinfra', 'suag', 'sucomp', 'sugep', 'sulog', 'suplans', 'svs']

for n in nomes:
    nome_arquivo_recebido = f'{n}.csv'
    nome_arquivo_gerado = f'dados_{n}'
    caminho_arquivo_recebido = 'superintendencias\dados_recebidos'
    caminho_arquivo_gerado = 'superintendencias\dados_tratados'

    dados_a_ordenar = []
    dados = pandas.read_csv(f'{caminho_arquivo_recebido}\{nome_arquivo_recebido}')
    colunas = list(dados.columns)

    for index, row in dados.iterrows():
        dados_a_ordenar.append([row[0],row[1],row[2],row[3]])

    dados_a_ordenar = sorted(dados_a_ordenar, key=lambda x: x[1])
    ordenado_coluna1 = []
    ordenado_coluna2 = []
    ordenado_coluna3 = []
    ordenado_coluna4 = []

    for d in range(len(dados_a_ordenar)):
        ordenado_coluna1.append(dados_a_ordenar[d][0])
        ordenado_coluna2.append(dados_a_ordenar[d][1])
        ordenado_coluna3.append(dados_a_ordenar[d][2])
        ordenado_coluna4.append(dados_a_ordenar[d][3])

    dados = pandas.DataFrame(
        {
            colunas[0]:ordenado_coluna1,
            colunas[1]:ordenado_coluna2,
            colunas[2]:ordenado_coluna3,
            colunas[3]:ordenado_coluna4
        }
    )

    dados.to_excel(f'{caminho_arquivo_gerado}\{nome_arquivo_gerado}.xlsx', index=False)
    dados.to_csv(f'{caminho_arquivo_gerado}\{nome_arquivo_gerado}.csv', index=False)
