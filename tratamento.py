
print(dados.head())
import pandas as pd

# 1. Ler a planilha
dados = pd.read_excel("base_clinica_bi_2025_bruta_v2.xlsx")

print("Linhas antes do tratamento:", len(dados))

# 2. Remover registros duplicados
duplicados = dados.duplicated().sum()
dados = dados.drop_duplicates()

print("Duplicidades removidas:", duplicados)

# 3. Padronizar os nomes dos convênios
dados["Convenio"] = dados["Convenio"].replace({
    "bradesco": "Bradesco",
    "BRADESCO": "Bradesco",
    "Bradesco Saúde": "Bradesco",
    "sul america": "Sul América",
    "SUL AMERICA": "Sul América",
    "Sul America": "Sul América",
    "porto seguro": "Porto Seguro",
    "PORTO SEGURO": "Porto Seguro"
})

# 4. Padronizar a coluna de datas
dados["Data_Consulta"] = pd.to_datetime(
    dados["Data_Consulta"],
    dayfirst=True,
    errors="coerce"
)

# 5. Conferir o resultado
print("\nLinhas depois do tratamento:", len(dados))
print("\nPrimeiras linhas:")
print(dados.head())

# 6. Salvar a planilha tratada
dados.to_excel("base_clinica_bi_2025_tratada.xlsx", index=False)

print("\nPlanilha tratada criada com sucesso!")
