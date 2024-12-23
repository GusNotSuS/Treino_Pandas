import pandas as pd
import numpy as np
import openpyxl

#importar dados:
df_pokemon = pd.read_csv('pokemon.csv')
print(df_pokemon)

#maneira comums de usar o pandas
print('\n\n')
print(df_pokemon[['Name','Type 1', 'Type 2', 'HP']])
print(df_pokemon.iloc[0:4])
print(df_pokemon.iloc[2,1])

print('\n\n')


df_pokemon2 = pd.DataFrame(columns=df_pokemon.columns)
while True:
    escolha = int(input('Digite 1 para ver informações de um pokemon\n2 para adicionar pokemon a uma lista separada\n3 para remover pokemon da lista separda\n4 para visualisar lista\n0 para sair: '))
    if escolha == 0:
        break
    if escolha == 1:
        pokemon = str(input('digite o nome do pokemon: ')).capitalize()
        if pokemon in df_pokemon['Name'].values:
            # Seleciona a linha do Pokémon escolhido
            escolha_pokemon = df_pokemon.loc[df_pokemon['Name'] == pokemon]
            print(escolha_pokemon)
            print('\n')
    if escolha == 2:
    
        # Verifica se o Pokémon está no DataFrame original
        pokemon = str(input('digite o nome do pokemon: ')).capitalize()
        if pokemon in df_pokemon['Name'].values:
            # Seleciona a linha do Pokémon escolhido
            escolha_pokemon = df_pokemon.loc[df_pokemon['Name'] == pokemon]
            # Adiciona ao DataFrame de escolhas
            df_pokemon2 = pd.concat([df_pokemon2, escolha_pokemon], ignore_index=True)
            print(f"{pokemon} foi adicionado às suas escolhas!")   
            print(f"Suas escolhas até agora:{df_pokemon2}")
            print('\n')
        else:
            print("Pokémon não encontrado. Tente novamente.")



    if escolha == 3:
        print(df_pokemon2)
        pokemon = input('Digite o nome do Pokémon a ser removido: ').capitalize()
        

        # Localiza as linhas onde o nome é igual ao Pokémon fornecido
        df_pokemon2 = df_pokemon2[df_pokemon2['Name'] != pokemon]

        # Mostra o DataFrame atualizado
        print(df_pokemon2)
        print('\n')
    if escolha == 4:
        print(df_pokemon2)
        print('\n')



arquivo_excel = "pokemon_escolhidos.xlsx"
print('Arquivo com lista de pokemons criado com sucesso')
df_pokemon2.to_excel(arquivo_excel, index=False)
