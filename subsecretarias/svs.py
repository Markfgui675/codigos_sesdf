import pandas

dados_a_ordenar = []
dados = pandas.read_csv('subsecretarias\svs.csv')

for index, row in dados.iterrows():
    dados_a_ordenar.append([row[0],row[1],row[2],row[3]])

dados_a_ordenar = sorted(dados_a_ordenar)
ordenado_coluna1 = []
ordenado_coluna2 = []
ordenado_coluna3 = []
ordenado_coluna4 = []

for d in range(len(dados_a_ordenar)):
    #consertar os floats da ordenação
    ordenado_coluna1.append(dados_a_ordenar[d][0])
    ordenado_coluna2.append(dados_a_ordenar[d][1])
    ordenado_coluna3.append(dados_a_ordenar[d][2])
    ordenado_coluna4.append(dados_a_ordenar[d][3])

dados = pandas.DataFrame(
    {
        '552.60000000000':ordenado_coluna1,
        '060000000000':ordenado_coluna2,
        'Subsecretaria de Vigilância à Saúde':ordenado_coluna3,
        'SES/SVS':ordenado_coluna4
    }
)

dados.to_csv('subsecretarias\dados_svs.csv', index=False)
