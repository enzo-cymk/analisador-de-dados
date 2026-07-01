import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
import random
fake = Faker("pt_BR")

marcas = ["Fiat", "Honda", "Toyota", "Mercedes", "Hyundai"]
modelos = ["Argo", "Civic", "Hilux", "G62", "i30"]
cidades = ["Belo Horizonte", "Uberlandia", "Uberaba", "Divinopolis", "Contagem"]

lista_marcas = []
lista_modelos = []
lista_cidades = []
lista_datas = []
lista_valores = []
lista_quantidade = []

for i in range(50):
    lista_marcas.append(random.choice(marcas))
    lista_modelos.append(random.choice(modelos))
    lista_cidades.append(random.choice(cidades))
    lista_datas.append(fake.date_between(start_date="-2y", end_date="today"))
    lista_valores.append(fake.random_int(min=100, max=400))
    lista_quantidade.append(fake.random_int(min=1, max=40))

dados = {
    "marca": lista_marcas,
    "modelo": lista_modelos,
    "cidade": lista_cidades,
    "data": lista_datas,
    "valor": lista_valores,
    "quantidade": lista_quantidade
}

df = pd.DataFrame(dados)
df.to_csv("alugueis.csv", index=False)

df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")

# Cria coluna do mês
df["mes"] = df["data"].dt.month

# Marca mais alugada
resultado = df.groupby("marca")["quantidade"].sum().reset_index()
resultado = resultado.sort_values("quantidade", ascending=False)

# Media da marca mais alugado
media_resultado = df.groupby("marca")["quantidade"].mean().reset_index()
media_resultado = media_resultado.sort_values("quantidade", ascending=False)



# Cidade com mais receita
cidade = df.groupby("cidade")["valor"].sum().reset_index()
cidade = cidade.sort_values("valor", ascending=False)

# Media da cidade com mais receita 
media_cidade = df.groupby("cidade")["valor"].mean().reset_index()
media_cidade = media_cidade.sort_values("valor", ascending=False)


mes = df.groupby("mes")["quantidade"].sum().reset_index()
mes = mes.sort_values("quantidade", ascending=False)

# Media do mes com mais algueis 
media_mes = df.groupby("mes")["quantidade"].mean().reset_index()
media_mes = media_mes.sort_values("quantidade", ascending=False )

#print(df.dtypes)
#print(df.head())
print(resultado)
print(media_resultado)

print(cidade)
print(media_cidade)

print(mes)
print(media_mes)

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

plt.figure()
plt.bar(media_cidade["cidade"], media_cidade["valor"])
plt.title("Média por cidade")
plt.xlabel("Cidade")
plt.ylabel("Valor")

plt.figure()
plt.bar(media_resultado["marca"], media_resultado["quantidade"])
plt.title("Média de resultado")
plt.xlabel("Marca")
plt.ylabel("Quantidade")

plt.figure()
plt.bar(media_mes["mes"], media_mes["quantidade"])
plt.title("Média mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade")
plt.show()