#  Análise Exploratória de Vendas de Video Games

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) utilizando um conjunto de dados sobre vendas de jogos de video game, disponível no Kaggle.

##  Dataset

- Nome: **Video Game Sales**
- Fonte: [Kaggle](https://www.kaggle.com/datasets/gregorut/videogame-sales-with-ratings)
- Contém informações sobre jogos lançados até 2016, incluindo:
  - Nome
  - Plataforma
  - Ano de lançamento
  - Gênero
  - Publisher
  - Vendas em diferentes regiões (NA, EU, JP, Other)
  - Vendas Globais

## Objetivos da Análise

- Identificar os jogos e Distribuidoras mais vendidos por região.
- Avaliar a relação entre gênero e volume de vendas.
- Investigar se a quantidade de jogos publicados influencia nas vendas.
- Calcular a dependência das Distribuidoras em relação aos gêneros mais lucrativos.

## Principais Descobertas

- **Nintendo** lidera como distribuidora com maior volume de vendas globais.
- Gêneros como **Action**, **Sports** e **Platform** são os mais lucrativos.
- A correlação entre **quantidade de jogos publicados** e **vendas totais** é forte (**r = 0.80**).
- Algumas publishers têm alta dependência de um único gênero para gerar receita.
- Publishers com portfólios diversificados tendem a ter maior resiliência no mercado.

## Gráficos Gerados

- Jogos mais vendidos por região
- Publishers com maior volume de vendas (pizza + barras)
- Correlação entre número de jogos publicados e vendas
- Gênero mais lucrativo por publisher
- Proporção do gênero principal nas vendas de cada publisher

## Conclusão

A análise evidencia como o sucesso nas vendas pode estar atrelado tanto ao volume de títulos quanto à escolha estratégica de gêneros. Publishers como Nintendo e EA demonstram alta dependência de gêneros específicos, enquanto outras adotam uma abordagem mais diversificada.

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

