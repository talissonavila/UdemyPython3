cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_acronym_list = ['BA', 'SP', 'MG', 'RJ']

print(f'States Capitals: {cities_list}.')
print(f'States Acronym: {states_acronym_list}.')

capital_with_uf_list = zip(cities_list, states_acronym_list)
print(f'States capitals with Acronym: {list(capital_with_uf_list)}')
