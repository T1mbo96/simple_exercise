def initialize_sample() -> list:
    return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 0]]


def convert_field(field) -> str:
    output = ''

    for row in field:
        for column in row:
            output += str(column)
            output += ' '
        output = output[:len(output) - 1]
        output += '\n'

    output = output[:len(output) - 1]

    return output


def get_neighbour_positions(y, x) -> list:
    if y < 0 or y > 4 or x < 0 or x > 4:
        raise ValueError("Values of x and y need to be between 0 and 4 (included)!")

    neighbour_list = []

    if y == 0:
        neighbour_list.append([y + 1, x])
    elif y == 4:
        neighbour_list.append([y - 1, x])
    else:
        neighbour_list.append([y + 1, x])
        neighbour_list.append([y - 1, x])

    if x == 0:
        neighbour_list.append([y, x + 1])
    elif x == 4:
        neighbour_list.append([y, x - 1])
    else:
        neighbour_list.append([y, x + 1])
        neighbour_list.append([y, x - 1])

    return neighbour_list


def click_position(y, x, field):
    neighbour_list = get_neighbour_positions(y, x)
    neighbour_list.append([y, x])

    for position in neighbour_list:
        if field[position[0]][position[1]] == 0:
            field[position[0]][position[1]] = 1
        else:
            field[position[0]][position[1]] = 0


def check_if_solved(field) -> bool:
    for row in field:
        for column in row:
            if column == 1:
                return False

    return True


def user_input() -> list:
    print("Welchen Button klicken?")
    row = eval(input("Bitte geben Sie die Reihe des Buttons (0-4) an:\n"))
    column = eval(input("Bitte geben Sie die Spalte des Buttons (0-4) an:\n"))

    if row < 0 or row > 4:
        raise ValueError('Please insert number between 0 and 4 included!')

    if column < 0 or column > 4:
        raise ValueError('Please insert number between 0 and 4 included!')

    return [row, column]


def continue_playing() -> bool:
    answer = input("Möchten Sie spielen? y/n\n")

    while answer != 'n' and answer != 'y':
        print("Bitte geben Sie y für JA oder n für NEIN an!")
        answer = input("Möchten Sie spielen? y/n\n")

    if answer == 'n':
        return False
    else:
        return True


def start_new_game():
    while continue_playing():
        field = initialize_sample()

        while not check_if_solved(field):
            convert_field(field)
            next_position = user_input()
            click_position(next_position[0], next_position[1], field)

        convert_field(field)
        print("Gratulation! Sie haben des Feld gelöst!")


if __name__ == '__main__':
    start_new_game()
