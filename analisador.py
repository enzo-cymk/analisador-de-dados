import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("alugueis.csv")
df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")

# Cria coluna do mês
df["mes"] = df["data"].dt.month

# Marca mais alugada
resultado = df.groupby("marca")["quantidade"].sum().reset_index()
resultado = resultado.sort_values("quantidade", ascending=False)

# Cidade com mais receita
cidade = df.groupby("cidade")["valor"].sum().reset_index()
cidade = cidade.sort_values("valor", ascending=False)

mes = df.groupby("mes")["quantidade"].sum().reset_index()
mes = mes.sort_values("quantidade", ascending=False)

#print(df.dtypes)
#print(df.head())
print(resultado)
print(cidade)
print(mes)

plt.bar(resultado["marca"], resultado["quantidade"])
plt.title("Marcas mais alugadas")
plt.xlabel("Marca")
plt.ylabel("Quantidade")


plt.figure()
plt.bar(cidade["cidade"], cidade["valor"])
plt.title("Receita por cidade")
plt.xlabel("Cidade")
plt.ylabel("Valor")


plt.figure()
plt.bar(mes["mes"], mes["quantidade"])
plt.title("Aluguéis por mês")
plt.xlabel("Mês")
plt.ylabel("Valor")
plt.show()