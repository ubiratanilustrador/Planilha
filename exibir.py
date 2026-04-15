import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

def exibir_grafico():
    # 1. Carregar a planilha do Calc
    df = pd.read_excel('dados.ods', engine='odf')

    # 2. Criar o gráfico usando uma coluna (ex: 'Valores') e outra para os nomes (ex: 'casa')
    plt.bar(df['valores'], df['casa'], color='skyblue')

    # 3. Personalizar o gráfico
    plt.title('Despesas do mes')
    plt.xlabel('intervalo de valores')
    plt.ylabel('Valores em R$')

    # 4. Exibir o resultado
    plt.show()

def exibir_coluna():
    # Carrega a planilha do Calc (.ods)
    # O parâmetro engine='odf' é essencial para arquivos .ods
    df = pd.read_excel('dados.ods', engine='odf')
    pd.set_option('display.max_rows', None)
    # Exibe a coluna formatada como uma grade de tabela
    print(tabulate(df[['valores']], headers='keys', tablefmt='psql'))


def exibir_primeira_cinco_linhas():
    # Carrega a planilha do Calc (.ods)
    # O parâmetro engine='odf' é essencial para arquivos .ods
    df = pd.read_excel('dados.ods', engine='odf')
    # Criamos uma cópia formatada para exibição
    df_view = df[['valores']].head().copy()
    df_view['valores'] = df_view['valores'].apply(lambda x: f"R$ {x:,.2f}")
    print(tabulate(df_view, headers='keys', tablefmt='psql'))

