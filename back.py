import pandas as pd

df = pd.read_csv("cases.csv", sep=",")

cases = []
for _, row in df.iterrows():
    cases.append(([row.iloc[0], row.iloc[1], row.iloc[2]], row.iloc[3]))

def calcular_similaridade_preco(notebook_a, notebook_b, preco_maximo):
    diff_preco = abs(notebook_a[0][0] - notebook_b[0][0])
    similaridade_preco = 1 - diff_preco / preco_maximo
    return similaridade_preco

def calcular_similaridade_finalidade(notebook_a, notebook_b):
    categorias_comuns = len(set(notebook_a[0][1]) & set(notebook_b[0][1]))
    total_categorias = len(set(notebook_a[0][1]) | set(notebook_b[0][1]))
    similaridade_finalidade = categorias_comuns / total_categorias
    return similaridade_finalidade

def calcular_similaridade_marca(notebook_a, notebook_b):
    marcas_comuns = 1 if notebook_a[0][2] == notebook_b[0][2] else 0
    similaridade_marca = marcas_comuns
    return similaridade_marca

def calcular_similaridade_global(notebook_a, notebook_b, pesos):
    similaridade_preco = calcular_similaridade_preco(notebook_a, notebook_b, pesos['preco_maximo'])
    similaridade_finalidade = calcular_similaridade_finalidade(notebook_a, notebook_b)
    similaridade_marca = calcular_similaridade_marca(notebook_a, notebook_b)

    similaridade_global = (
        pesos['peso_preco'] * similaridade_preco +
        pesos['peso_finalidade'] * similaridade_finalidade +
        pesos['peso_marca'] * similaridade_marca
    )

    return similaridade_global

def recomendar_notebook(novo_notebook):
    global cases, pesos
    similaridades = [(calcular_similaridade_global(novo_notebook, caso, pesos), caso[1]) for caso in cases]
    similaridades.sort(reverse=True)
    return similaridades[0][1]

pesos = {'preco_maximo': 10000, 'peso_preco': 0.4, 'peso_finalidade': 0.3, 'peso_marca': 0.3}

if __name__ == '__main__':
    novo_notebook = ([10000, "Casual", "Asus"], None)
    notebook_recomendado = recomendar_notebook(novo_notebook)
    print(f"Notebook recomendado: {notebook_recomendado}")
