class Polish:
    def __init__(self):
        with open('language/polski.txt', 'r', encoding='UTF-8') as plik:
            self.tabelaslow = plik.read().splitlines()

    def does_word_exist(self, word: str) -> bool:
        return word in self.tabelaslow

