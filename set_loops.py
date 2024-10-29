def unique_strings(words):
    unique_chars = []  
    seen = set()  

    for char in words:
        if char not in seen:
            seen.add(char)  # Agregar el carácter al set
            unique_chars.append(char)  # Añadir solo si no está en la lista

    return set(unique_chars)  # Devolver como conjunto


input_str = "hello"
result = unique_strings(input_str)
print(result)
