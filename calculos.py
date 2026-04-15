import pandas as pd
from tabulate import tabulate

def soma_coluna():
    #soma todos os dados da coluna
    df = pd.read_excel('dados.ods', engine='odf')
    total = df['valores'].sum()
    #exibi no console
    print('TOTAL: R$',total)