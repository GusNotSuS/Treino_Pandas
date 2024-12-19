import pandas as pd
import numpy as np


#criando um objeto
dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(df2)
print(df.head(3)) #vê o topo do dataframe, parando no 3 index
print(df.tail(3)) #vê o fundo do dataframe, e para no 3 index

print(df.index) #mostra os index
print(df.columns) #mostra as colunas

print(df.describe) #resume os dados

print('\n',df.to_numpy) #converte em numpy


print(df.sort_index(axis=1, ascending=False)) #organiza pelo index fornecido

print(df.sort_values(by="B")) #organiza pelo valor na linha informada


print(df["A"]) #pede apenas a linha A
print(df[0:3]) #pede apenas a coluna 0 a 3

print(df.loc[dates[0]]) #pega a linha com a informação fornecida
print(df.loc[:,["A","C"]])

print('\n\n')
#importar dados:
df_pokemon = pd.read_csv('pokemon.csv')
print(df_pokemon)

#maneira comums de usar o pandas
print('\n\n')
print(df_pokemon[['Name','Type 1', 'Type 2', 'HP']])
print(df_pokemon.iloc[0:4])
print(df_pokemon.iloc[2,1])
for index, row in df_pokemon.iterrows():
    print(index,row['Name'])

print('\n\n')

escolha = str(input('Digite o nome do pokemon: ')).capitalize()
print(df_pokemon.loc[df_pokemon['Name'] == escolha])


#adicionando coluns em um dataframe
df_pokemon2 = pd.DataFrame()
while True:
    escolha = str(input('escolha um pokemonm, ou digite 0 pra sair'))
    if escolha == '0':
        break
    df_pokemon2 = pd.concat([df_pokemon2, df_pokemon[df_pokemon['Name'] == escolha]], ignore_index=True)
    print(df_pokemon2)