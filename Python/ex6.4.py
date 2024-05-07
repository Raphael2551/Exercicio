# use list comprehension para cirar lista com divisiveis de 3 e 5 de 0 a 30

divisiveis_3_5 = [num for num in range(31) if num % 3 == 0 and num % 5 == 0]

print("Números divisíveis por 3 e 5 de 0 a 30:", divisiveis_3_5)
