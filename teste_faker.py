from faker import Faker
import random

fake = Faker("pt_BR")

#print(fake.city())
#print(fake.date_between(start_date="-2y", end_date="today"))
#print(fake.random_int(min=100, max=400))

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

print(lista_marcas)
print(lista_datas)
    