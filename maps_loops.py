def find_max_value(dict):
    valor = -1
    nombre = ""
    for key,value in dict.items():
        if value > valor:
            valor = value
            nombre = key
    return nombre

def reverse_dict(dict):
    a = dict()
    for key, value in dict.items():
        if value in a:
            a[value] += key # de esta manera lo doy vuelta y le sumo los valores iguales
        else:
            a[value] = key
    return a


def word_freq_counter(words):
    diccionario = dict()
    for word in words:
        if word in diccionario:
            diccionario[word] += 1
        else:
            diccionario[word] = 1
    return diccionario


def find_biggest_expense(dict):
    valor = 0
    gasto = ""
    for key, value in dict.items():
        costo = sum(value) / len(value) # calculo el promedio
        if costo > valor:
            valor = costo
            gasto = key
    return gasto

def sum_of_expenses(expenses):
    diccionario = dict()
    for key, value in expenses.items():
        suma = sum(value)
        diccionario[key] = suma
    return diccionario
dictt = {'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]}
print(sum_of_expenses(dictt))



def sum_of_expenses_by_type(expenses):
        diccionario = {}
        for key, value in expenses.items():
            for type, cost in value:
                if type in diccionario:
                    diccionario[type] += cost
                else:
                    diccionario[type] = cost
        return diccionario
