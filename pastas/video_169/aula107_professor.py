# Forma desenvolvida 1 
def zipper(first_list: list, second_list: list):
    max_range = min(len(first_list), len(second_list))
    return [
        (first_list[count], second_list[count]) for count in range(max_range)
    ]


cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_acronym_list = ['BA', 'SP', 'MG', 'RJ']
print(zipper(cities_list, states_acronym_list))


# Forma desenvolvida 2
cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_acronym_list = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(cities_list, states_acronym_list)))


# Forma desenvolvida 3
from itertools import zip_longest
cities_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states_acronym_list = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(cities_list, states_acronym_list, fillvalue='City not found')))
