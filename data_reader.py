import csv


def read_game_input():
    rows = []
    with open("macierz_literek.csv", encoding="UTF-8") as csvfile:
        file_data = csv.reader(csvfile, delimiter=",")
        for row in file_data:
            rows.append(row)
    return rows
