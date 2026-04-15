# Amostras de coigos que podem ser usadas no programa

import pandas as pd
from tabulate import tabulate

# Ler a planilha
df = pd.read_excel('dados.ods', engine='odf')

# Exemplo de operação: criar uma nova coluna com a soma de outras duas
df['Total'] = df['valores'] * df['valores']

# Salvar as alterações
df.to_excel('planilha_atualizada.ods', engine='odf', index=False)

#Modificar todos os valores (ex: aplicar 10% de desconto):
df['Preço'] = df['Preço'] * 0.9

#media de valores
media = df['Preço'].mean()

#Criar uma nova coluna baseada em uma existente:
df['Imposto'] = df['Preço'] * 0.15