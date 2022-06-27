from typing import List, Tuple

from data_reader import read_game_input
from language.language_database import Polish


class SlowotokCrawler:

    def __init__(self, game_matrix: List[List[str]]):
        self.matrix = game_matrix

    def assemble_all_words(self, length=3):
        dnds[6][4][3] == None
        dnds = {
            [0, 0]: {
                [0, 1]: {
                    [0, 2]: True
                }
            }
        }
        snake = self.assemble_coord_snake((0, 0))

        snake = self.assemble_coord_snake((0, 0))


    def assemble_coord_snake(self, start: Tuple[int, int], length=3):
        used_coords = []
        current_coord = start
        used_coords.append(current_coord)
        for _ in range(length-1):
            available_moves = self.get_available_moves(current_coord, used_coords)
            if not available_moves:
                break
            current_coord = available_moves[0]
            used_coords.append(current_coord)
        return used_coords

    def create_word_from_coords(self, coords: List[Tuple[int, int]]) -> str:
        current_word = []
        for coord in coords:
            current_word.append(self.matrix[coord[0]][coord[1]])
        current_word = ''.join(current_word)
        return current_word

    def get_available_moves(self, coordinates: tuple, used_coords: List):
        size_y = len(self.matrix)
        size_x = len(self.matrix[0])
        all_moves = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
        all_moves.remove((0, 0))
        all_coords = [(coordinates[0]+x, coordinates[1]+y) for x, y in all_moves]
        coord_is_legal = lambda coord: coord[0] in range(size_x) and coord[1] in range(size_y)
        available_coords = list(filter(coord_is_legal, all_coords))
        return [item for item in available_coords if item not in used_coords]


if __name__ == "__main__":
    word = SlowotokCrawler(read_game_input()).assemble_random_word()
    word_exists = Polish().does_word_exist(word)
    print(f"{word} exists: {word_exists}")
