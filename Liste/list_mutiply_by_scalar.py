##
# moltiplichiamo l'array per uno scalare con una funzione

def multiply_list_by_scalar(list_data, value):
    for i in range(len(list_data)):
        list_data[i] *= value
    return list_data

list_data = [1,2,3,4]
value = 2
print(list_data)

list_data_2 = multiply_list_by_scalar(list(list_data), value)

print(list_data)
print(list_data_2)