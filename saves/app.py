import pandas as pd
import django as django
import matplotlib.pyplot as plt

mensagem_intro = "Olá, sou o ObrasBot, seu assistente virtual para ajudar você a encontrar informações sobre as obras e suas pendencias. Como posso ajudar hoje?"
df = pd.read_excel('obras.xlsx') #pode ser "obras" em maiusuculo, nao lembro

def print_obras_pendentes(caminho_arquivo_excel, nome_aba, inicio_linha, fim_linha, inicio_coluna, fim_coluna, caminho_saida_imagem):
    df = pd.read_excel(caminho_arquivo_excel, sheet_name=nome_aba, header=inicio_linha-1, usecols=f"{inicio_coluna}:{fim_coluna}")
    df = df.iloc[inicio_linha-1:fim_linha]
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df.iloc[:, 0], marker='o')
    plt.title('Obras Pendentes')
    plt.xlabel('Índice')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.savefig(caminho_saida_imagem)
    plt.close()

def buscar_obras_pendentes():
    obras_pendentes = df[df['Status'].isin(['NÃO', 'PARCIAL'])]
    if obras_pendentes.empty:
        return "Não há obras pendentes no momento."
    else:
        return obras_pendentes.to_dict(orient='records')
    
def buscar_obra_especifica(codigo_obra):
    obra = df[df['IPSP '] == codigo_obra]
    if obra.empty:
        return "Obra não encontrada."
    else:
        return obra.to_dict(orient='records')[0]  # Retorna a primeira ocorrência como dicionário