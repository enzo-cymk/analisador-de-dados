# 🚗 Analisador de Dados de Aluguel

Projeto simples voltado para aprendizado de Python e Pandas.

## 📋 Descrição

Análise de dados de uma locadora de veículos, respondendo perguntas de negócio
e apresentando os resultados em gráficos.

## ❓ Perguntas respondidas

- 🏆 Qual marca foi mais alugada?
- 💰 Qual cidade gerou mais receita?
- 📅 Qual mês teve mais aluguéis?

## 🛠️ Tecnologias utilizadas

- Python 3.14
- Pandas
- Matplotlib

## ▶️ Como rodar

1. Clone o repositório
2. Instale as dependências:
   pip install pandas matplotlib
3. Execute o arquivo principal:
   py analisador.py

## 💡 Sobre o projeto

Desenvolvido do zero com o auxílio de uma IA atuando como mentora,
guiando cada etapa do aprendizado sem entregar o código pronto.

## 🔄 Atualizações 

## v2 - Geração automatica de dados com Faker

- Substituída a criação manual de dados por geração automática usando a
  biblioteca **Faker**, combinada com listas fixas de marcas/modelos/cidades
  e o módulo `random` do Python.
- O dataset passou de 10 para 50 registros gerados aleatoriamente,
  tornando as análises mais realistas.
- Adicionadas novas análises com **média** (`.mean()`), além das somas
  (`.sum()`) já existentes:
  - Quantidade média alugada por marca
  - Valor médio de aluguel por cidade
  - Quantidade média de aluguéis por mês
- Novos gráficos criados para cada uma dessas médias.

### 🛠️ Nova tecnologia utilizada

- Faker (geração de dados fictícios)