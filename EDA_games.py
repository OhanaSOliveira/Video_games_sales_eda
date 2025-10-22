import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgsales.csv") 

#Grafico Top 10 vendidos global
top10 = df.sort_values(by="Global_Sales", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Name", y="Global_Sales", palette="viridis")
plt.title("Top 10 Jogos Mais Vendidos Globalmente")
plt.xticks(rotation=45)
plt.show()

#Grafico Top 10 vendidos NA
top10 = df.sort_values(by="NA_Sales", ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Name", y="NA_Sales", palette="viridis")
plt.title("Top 10 Jogos Mais Vendidos Norte América")
plt.xticks(rotation=45)
plt.show()

#Grafico Top 10 vendidos EU
top10 = df.sort_values(by="EU_Sales", ascending=False).head(10) 
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Name", y="EU_Sales", palette="viridis")
plt.title("Top 10 Jogos Mais Vendidos na Europa")
plt.xticks(rotation=45)
plt.show()


#Graficos Top 5 jogos mais vendidos por região
regions = {
    "América do Norte": "NA_Sales",
    "Europa": "EU_Sales",
    "Japão": "JP_Sales",
    "Outras Regiões": "Other_Sales",
    "Global": "Global_Sales"
}
fig, axs = plt.subplots(3, 2, figsize=(16, 15))
fig.suptitle("Top 5 Jogos Mais Vendidos por Região", fontsize=20)
axs = axs.flatten()
for i, (region_name, column) in enumerate(regions.items()):

    top_games = df[["Name", column]].sort_values(by=column, ascending=False).head(5)
    sns.barplot(
        data=top_games,
        x=column,
        y="Name",
        palette="viridis",
        ax=axs[i]
    )
    
    axs[i].set_title(region_name, fontsize=14)
    axs[i].set_xlabel("Vendas (em milhões)")
    axs[i].set_ylabel("Nome do Jogo")
if len(regions) < len(axs):
    axs[-1].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


#Top 5 gêneros por região
genre_palette = {
    "Action": "red",
    "Sports": "blue",
    "Shooter": "purple",
    "Platform": "orange",
    "Racing": "green",
    "Misc": "pink",
    "Role-Playing": "gold",
    "Puzzle": "brown",
    "Simulation": "cyan",
    "Fighting": "gray",
    "Adventure": "teal",
    "Strategy": "olive"
}
regions = {
    "América do Norte": "NA_Sales",
    "Europa": "EU_Sales",
    "Japão": "JP_Sales",
    "Outras Regiões": "Other_Sales",
    "Global": "Global_Sales"
}
fig, axs = plt.subplots(3, 2, figsize=(18, 16))
fig.suptitle("Top 5 Gêneros Mais Vendidos por Região", fontsize=20)
axs = axs.flatten()

for i, (region_name, column) in enumerate(regions.items()):
    genre_sales = df.groupby("Genre")[column].sum().sort_values(ascending=False).head(5).reset_index()
    sns.barplot(
        data=genre_sales,
        x=column,
        y="Genre",
        palette=[genre_palette.get(genre, "gray") for genre in genre_sales["Genre"]],
        ax=axs[i]
    )

    axs[i].set_title(region_name, fontsize=14)
    axs[i].set_xlabel("Vendas (milhões)")
    axs[i].set_ylabel("Gênero")
if len(regions) < len(axs):
    axs[-1].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()





# Gráfico de pizza dos top 10 publishers com maiores vendas globais
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False)
top_publishers = publisher_sales.head(10)
plt.figure(figsize=(8, 8))
plt.pie(top_publishers, labels=top_publishers.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Publishers com Maior Vendas Globais')
plt.show()


# Gráfico de dispersão: Quantidade de jogos publicados vs. vendas globais por publisher
publisher_stats = df.groupby('Publisher').agg({
    'Name': 'count',
    'Global_Sales': 'sum'
}).rename(columns={'Name': 'Game_Count'})

publisher_stats = publisher_stats[publisher_stats['Game_Count'] > 1]
top_publishers_stats = publisher_stats.sort_values(by='Global_Sales', ascending=False).head(15)
plt.figure(figsize=(12, 8))
sns.regplot(
    data=top_publishers_stats,
    x='Game_Count',
    y='Global_Sales',
    scatter=True,
    ci=None,
    line_kws={"color": "red", "linewidth": 1.5}
)
for publisher, row in top_publishers_stats.iterrows():
    plt.text(row['Game_Count'] + 0.3, row['Global_Sales'], publisher, fontsize=9)

plt.title('Top 15 Publishers: Quantidade de Jogos vs. Vendas Globais (com linha de tendência)')
plt.xlabel('Quantidade de Jogos Publicados')
plt.ylabel('Vendas Globais (milhões)')
plt.grid(True)
plt.tight_layout()
plt.show()

#correlação entre quantidade de jogos e vendas globais
correlation = publisher_stats['Game_Count'].corr(publisher_stats['Global_Sales'])
print(f"Correlação entre quantidade de jogos e vendas: {correlation:.2f}")


# Gênero mais lucrativo por publisher
genre_sales_by_publisher = df.groupby(['Publisher', 'Genre'])['Global_Sales'].sum().reset_index()
top_genre_by_publisher = genre_sales_by_publisher.sort_values('Global_Sales', ascending=False).drop_duplicates('Publisher')
top_genre_by_publisher = top_genre_by_publisher.sort_values('Global_Sales', ascending=False)
print(top_genre_by_publisher.head(10)) 


# Gráfico de barras: Gênero mais lucrativo por publisher (top 15)
top15 = top_genre_by_publisher.head(15)
plt.figure(figsize=(12, 7))
sns.barplot(
    data=top15,
    y='Publisher',
    x='Global_Sales',
    hue='Genre',
    dodge=False,
    palette='tab10'
)
plt.title('Gênero Mais Lucrativo por Publisher (Top 15)')
plt.xlabel('Vendas Globais (milhões)')
plt.ylabel('Publisher')
plt.legend(title='Gênero')
plt.tight_layout()
plt.show()



# Dependência do gênero mais lucrativo por publisher
plt.figure(figsize=(12, 7))
sns.barplot(
    data=top15_genre_dependency,
    y='Publisher',
    x='Top_Genre_Percent',
    hue='Genre',
    dodge=False,
    palette='Set2'
)
plt.title('Top 15 Publishers: Dependência no Gênero Mais Lucrativo')
plt.xlabel('Proporção das Vendas Totais (%)')
plt.ylabel('Publisher')
plt.legend(title='Gênero')
plt.tight_layout()
plt.show()

