def sum_index_of_lists(first_list: list, second_list: list):
    result_list = []
    for count in range(min(len(first_list), len(second_list))):
        result_list.append(first_list[count] + second_list[count])
    return result_list


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


print(sum_index_of_lists(lista_a, lista_b))
