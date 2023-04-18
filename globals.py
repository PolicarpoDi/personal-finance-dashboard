import pandas as pd
import os



# Criando a estrutura do csv para utilização dos dados. 
# Primeiro verifico se já tem dentro da estrutura de pastas os arquivos 
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas  = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas  = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
# Se não tiver, crio os arquivos    
else:
    data_structure = {'Valor': [],
        'Efetuado': [],
        'Fixo': [],
        'Data': [],
        'Categoria': [],
        'Descrição': [],}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_receitas.to_csv('df_receitas.csv')
    df_despesas.to_csv('df_despesas.csv')
    
if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_despesa  = pd.read_csv("df_cat_despesa.csv", index_col=0, parse_dates=True)
    df_cat_receita  = pd.read_csv("df_cat_receita.csv", index_col=0, parse_dates=True)
    # Pega o dataframe e joga os valores para uma lista
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
    
else:
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesa = {'Categoria': ["Cartão de Credito", "Financiamento", "Impostos"]}
    
    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesa)
    df_cat_receita.to_csv('df_cat_receita.csv')
    df_cat_despesa.to_csv('df_cat_despesa.csv')
    