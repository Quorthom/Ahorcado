import random
PROPS_AHORCADO = ['''

    +---+ |  |
        |
        |
        |
        |
        |
   =======''','''

    +---+
    |   |
    O   |
        |
        |
        |
   =======''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
   =======''','''

    +---+  
    |   |
    O   |
   /|   |
        |
        |
   =======''','''

    +---+  
    |   |
    O   |
   /|\  |
        |
        |
   =======''','''

    +---+  
    |   |
    O   |
   /|\  |
   /    |
        |
   =======''','''

    +---+  
    |   |
    O   |
   /|\  |
   / \  |
        |
   =======''']
words = 'muerte destrucción mayhem snow nocturnal ulver'.split()

def get_randword(word_list):
    return word_list[random.randint(0, len(word_list)-1)]
def show_game(PROPS_AHORCADO, wrong_letters, correct_letters, secret_word):
    print(PROPS_AHORCADO[len(wrong_letters)])
    print()
