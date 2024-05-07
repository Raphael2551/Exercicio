# use list comprehension para cirar lista com palavras que contem "a" em uma frase digitada pelo user e substtitua a letra por "o"


frase = input("Digite uma frase: ")

palavras_com_a_substituidas = [palavra.replace('a', 'o') for palavra in frase.split() if 'a' in palavra]

print("Palavras com 'a' substituídas por 'o':", palavras_com_a_substituidas)
