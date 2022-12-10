from unidecode import unidecode

"""
1. Escreva um programa que verifique se duas palavras são anagramas.
Se possível, passe caracteres com acentos para sua versão sem acento.
usaria o unided code
ex: ç -> c; á -> a..
"""

print('Questão 1 :')


def anagram(word1, word2) -> bool:
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(unidecode(word1)) == sorted(unidecode(word2)):
        print(f'anagram: {word1} & {word2}')
        return True
    print(f'Not anagram: {word1} && {word2}')
    return False


anagram("Amor", "roma")
anagram("Papo", "Pão")
print('-' * 50)

"""
2. Escreva um programa que itere em uma listagem de números de 1 a 50.
Para múltiplos de 3 imprima na tela a palavra ping ao invés do número.
Para múltiplos de 5 imprima na tela a palavra pong ao invés do número.
Para múltiplos de 3 e 5 imprima na tela a palavra pingpong ao invés do número.
Se não for múltiplo de nenhum dos dois apenas imprima o número
"""

print('Questão 2 :')


def ping_pong(lista: list) -> None:
    for i in range(50):
        if i % 3 == 0:
            print("ping multiplo de 3")
        if i % 5 == 0:
            print("pong multiplo de 5")
        if i % 3 == 0 and i % 5 == 0:
            print("pingPong, multiplo de 3 e 5")
        if not i % 3 == 0 and not i % 5 == 0:
            print(i)


test_list = [x for x in range(50)]
ping_pong(test_list)
print('-' * 50)

print('Questão 3 :')
"""
# 3. complete a função abaixo:
# A função deve verificar se a string
# recebida como parâmetro é um palíndromo* válido
# * frase ou palavra que se pode ler, indiferentemente,
#   da esquerda para a direita ou vice-versa.
"""


def valid_palindrome(check_palindrome: str) -> bool:
    try:
        if not check_palindrome == (check_palindrome[::-1]):
            print(False)
            print(check_palindrome)
            return False
        if check_palindrome == (check_palindrome[::-1]):
            print(check_palindrome)
            print(True)
            return True
    except TypeError:
        raise TypeError(f'{valid_palindrome} only accept str type')


valid_palindrome('ovo')
# test error valid_palindrome(10)
print('-' * 50)

"""
4. Dadas as tres variáveis abaixo
escreva uma função que retorne a saída
no formato desejado
todas as listas SEMPRE terão o mesmo tamanho
"""

fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

"""
saída desejada:
[('Apples', 5, 1.50),
 ('Oranges', 3, 2.25),
 ('Bananas', 4, 0.89)]
"""
print('Questão 4 :')


def process_values(
        fruits: list,
        quantities: list,
        prices: list) -> list:
    wished_return = []
    for i in range(len(fruits)):
        wished_return.append((fruits[i], quantities[i], prices[i]))
    print(wished_return)
    return wished_return


process_values(fruits, quantities, prices)

print('-' * 50)
