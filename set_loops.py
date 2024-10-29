def unique_strings(words):
    unique_chars = set()  # Usar un conjunto para almacenar caracteres únicos
    for char in words:
        unique_chars.add(char)  # Agrega el caracter al conjunto
    return unique_chars
