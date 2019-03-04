from tkinter import *
import inspect
import exercise


# Test if functions exist
def test_functions_exist():
    T.insert(END, 'Test if functions exist:\n\n')

    # Test convert_field function exists
    if not hasattr(exercise, 'convert_field') or not inspect.isfunction(exercise.convert_field):
        T.insert(END, 'FAILED\ttest convert_field function exist\n')
    else:
        T.insert(END, 'OK\ttest convert_field function exist\n')

        # Test convert_field function arguments
        if len(inspect.getfullargspec(exercise.convert_field).args) != 1 or 'field' not in inspect.getfullargspec(exercise.convert_field).args:
            T.insert(END, 'FAILED\ttest if arguments of convert_field(field) function are correct\n')
        else:
            T.insert(END, 'OK\ttest if arguments of convert_field(field) are correct\n')

    # Test get_neighbour_positions function exists
    if not hasattr(exercise, 'get_neighbour_positions') or not inspect.isfunction(exercise.get_neighbour_positions):
        T.insert(END, 'FAILED\ttest get_neighbour_positions function exist\n')
    else:
        T.insert(END, 'OK\ttest get_neighbour_positions function exist\n')

        # Test get_neighbour_positions function arguments
        if len(inspect.getfullargspec(exercise.get_neighbour_positions).args) != 2 or 'y' != inspect.getfullargspec(exercise.get_neighbour_positions).args[0] or 'x' != inspect.getfullargspec(exercise.get_neighbour_positions).args[1]:
            T.insert(END, 'FAILED\ttest if arguments of get_neighbour_positions(y, x) function are correct\n')
        else:
            T.insert(END, 'OK\ttest if arguments of get_neighbour_positions(y, x) are correct\n')

    # Test click_position function exists
    if not hasattr(exercise, 'click_position') or not inspect.isfunction(exercise.click_position):
        T.insert(END, 'FAILED\ttest click_position function exist\n')
    else:
        T.insert(END, 'OK\ttest click_position function exist\n')

        # Test click_position function arguments
        if len(inspect.getfullargspec(exercise.click_position).args) != 3 or 'y' != inspect.getfullargspec(exercise.click_position).args[0] or 'x' != inspect.getfullargspec(exercise.click_position).args[1] or 'field' != inspect.getfullargspec(exercise.click_position).args[2]:
            T.insert(END, 'FAILED\ttest if arguments of click_position(y, x, field) function are correct\n')
        else:
            T.insert(END, 'OK\ttest if arguments of click_position(y, x, field) are correct\n')

    # Test check_if_solved function exists
    if not hasattr(exercise, 'check_if_solved') or not inspect.isfunction(exercise.check_if_solved):
        T.insert(END, 'FAILED\ttest check_if_solved function exist\n')
    else:
        T.insert(END, 'OK\ttest check_if_solved function exist\n')

        # Test check_if_solved function arguments
        if len(inspect.getfullargspec(exercise.check_if_solved).args) != 1 or 'field' not in inspect.getfullargspec(exercise.check_if_solved).args:
            T.insert(END, 'FAILED\ttest if arguments of check_if_solved() function are correct\n')
        else:
            T.insert(END, 'OK\ttest if arguments of check_if_solved() are correct\n')

    # Test user_input function exists
    if not hasattr(exercise, 'user_input') or not inspect.isfunction(exercise.user_input):
        T.insert(END, 'FAILED\ttest user_input function exist\n')
    else:
        T.insert(END, 'OK\ttest user_input function exist\n')

    T.insert(END, '------------------------------------------------------------------------------------------\n')


# Helper function for test_get_neighbour_positions
def insert_positions_of_list(neighbour_list):
    for position in neighbour_list:
        T.insert(END, '[' + str(position[0]) + '|' + str(position[1]) + '] ')

    T.insert(END, '\n')


# Test get_neighbour_positions function
def test_get_neighbour_positions():
    T.insert(END, 'Test get_neighbour_positions function:\n\n')

    # Test if function throws error
    try:
        exercise.get_neighbour_positions(-1, 4)
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (-1, 4)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (-1, 4)\n')

    try:
        exercise.get_neighbour_positions(5, 4)
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (5, 4)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (5, 4)\n')

    try:
        exercise.get_neighbour_positions(0, 5)
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (0, 5)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (0, 5)\n')

    try:
        exercise.get_neighbour_positions(0, -1)
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (0, -1)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (0, -1)\n')

    # Test if function returns a list
    if not type(exercise.get_neighbour_positions(3, 2)) == list:
        T.insert(END, 'FAILED\treturn value is not a list\n')
    else:
        T.insert(END, 'OK\treturn value is a list\n')

    # Test position [3, 2]
    correct_positions = True
    test_return_statement = exercise.get_neighbour_positions(3, 2)

    if not len(test_return_statement) == 4:
        T.insert(END, 'FAILED\tposition [3|2] should return a list with 4 positions but was ' + str(
            len(test_return_statement)) + '\n')
    else:
        T.insert(END, 'OK\tposition [3|2] returns a list with 4 positions\n')

        if [2, 2] in test_return_statement:
            if [3, 3] in test_return_statement:
                if [4, 2] in test_return_statement:
                    if [3, 1] in test_return_statement:
                        T.insert(END, 'OK\tposition [3|2] returns a list with positions [2|2] [3|3] [4|2] [3|1]\n')
                    else:
                        correct_positions = False
                else:
                    correct_positions = False
            else:
                correct_positions = False
        else:
            correct_positions = False

        if not correct_positions:
            T.insert(END,
                     'FAILED\tposition [3|2] should return a list with positions [2|2] [3|3] [4|2] [3|1] but was ')
            insert_positions_of_list(test_return_statement)

    # Test position [0, 2]
    correct_positions = True
    test_return_statement = exercise.get_neighbour_positions(0, 2)

    if not len(test_return_statement) == 3:
        T.insert(END, 'FAILED\tposition [0|2] should return a list with 3 positions but was ' + str(
            len(test_return_statement)) + '\n')
    else:
        T.insert(END, 'OK\tposition [0|2] returns a list with 3 positions\n')

        if [0, 1] in test_return_statement:
            if [0, 3] in test_return_statement:
                if [1, 2] in test_return_statement:
                    T.insert(END, 'OK\tposition [0|2] returns a list with positions [0|1] [0|3] [1|2]\n')
                else:
                    correct_positions = False
            else:
                correct_positions = False
        else:
            correct_positions = False

    if not correct_positions:
        T.insert(END,
                 'FAILED\tposition [0|2] should return a list with positions [0|1] [0|3] [1|2] but was ')
        insert_positions_of_list(test_return_statement)

    # Test position [2, 4]
    correct_positions = True
    test_return_statement = exercise.get_neighbour_positions(2, 4)

    if not len(test_return_statement) == 3:
        T.insert(END, 'FAILED\tposition [2|4] should return a list with 3 positions but was ' + str(
            len(test_return_statement)) + '\n')
    else:
        T.insert(END, 'OK\tposition [2|4] returns a list with 3 positions\n')

        if [1, 4] in test_return_statement:
            if [2, 3] in test_return_statement:
                if [3, 4] in test_return_statement:
                    T.insert(END, 'OK\tposition [2|4] returns a list with positions [1|4] [2|3] [3|4]\n')
                else:
                    correct_positions = False
            else:
                correct_positions = False
        else:
            correct_positions = False

    if not correct_positions:
        T.insert(END,
                 'FAILED\tposition [2|4] should return a list with positions [1|4] [2|3] [3|4] but was ')
        insert_positions_of_list(test_return_statement)

    T.insert(END, '------------------------------------------------------------------------------------------\n')


# Test click_position function
def test_click_position():
    T.insert(END, 'Test click_position function:\n\n')

    # First test
    field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 1], [0, 0, 0, 1, 0]]
    exercise.click_position(3, 3, field)
    correct_changes = True

    for row in field:
        for column in row:
            if column == 1:
                correct_changes = False

    if not correct_changes:
        T.insert(END,
                 'FAILED\tclicking position [3|3] on field should solve it:\n\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 1 0\n\t0 0 1 1 1\n\t0 0 0 1 0\n\n\tbut was:\n\n\t')

        for row in field:
            for column in row:
                T.insert(END, str(column) + ' ')
            T.insert(END, '\n\t')
    else:
        T.insert(END,
                 'OK\tclicking position [3|3] on field solved it:\n\n\t0 0 0 0 0\t\t0 0 0 0 0\n\t0 0 0 0 0\t\t0 0 0 0 0\n\t0 0 0 1 0\t\t0 0 0 0 0\n\t0 0 1 1 1\t\t0 0 0 0 0\n\t0 0 0 1 0\t\t0 0 0 0 0')

    T.insert(END, '\n\n')

    # Second Test
    field = [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 0]]
    exercise.click_position(1, 2, field)
    correct_changes = True

    if field[1][2] == 1:
        if field[0][2] == 0:
            if field[1][3] == 1:
                if field[2][2] == 1:
                    if field[1][1] == 0:
                        T.insert(END,
                                 'OK\tclicking position [1|2] on field changes field and surrounding fields:\n\n\t0 0 1 0 0\t\t0 0 0 0 0\n\t0 1 0 0 0\t\t0 0 1 1 0\n\t0 1 0 1 0\t\t0 1 1 1 0\n\t0 0 1 1 1\t\t0 0 1 1 1\n\t1 0 0 1 0\t\t1 0 0 1 0')
                    else:
                        correct_changes = False
                else:
                    correct_changes = False
            else:
                correct_changes = False
        else:
            correct_changes = False
    else:
        correct_changes = False

    if not correct_changes:
        T.insert(END,
                 'FAILED\tclicking position [1|2] on field should be:\n\n\t0 0 1 0 0\t\t0 0 0 0 0\n\t0 1 0 0 0\t\t0 0 1 1 0\n\t0 1 0 1 0\t\t0 1 1 1 0\n\t0 0 1 1 1\t\t0 0 1 1 1\n\t1 0 0 1 0\t\t1 0 0 1 0\n\n\tbut was:\n\n\t')

        for row in field:
            for column in row:
                T.insert(END, str(column) + ' ')
            T.insert(END, '\n\t')

    T.insert(END, '\n\n')

    # Third test
    field = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]
    exercise.click_position(2, 4, field)
    correct_changes = True

    for row in field:
        for column in row:
            if column == 0:
                correct_changes = False

    if not correct_changes:
        T.insert(END,
                 'FAILED\tclicking position [2|4] on field should set every position to 1:\n\n\t1 1 1 1 1\n\t1 1 1 1 0\n\t1 1 1 0 0\n\t1 1 1 1 0\n\t1 1 1 1 1\n\n\tbut was:\n\n\t')

        for row in field:
            for column in row:
                T.insert(END, str(column) + ' ')
            T.insert(END, '\n\t')
    else:
        T.insert(END,
                 'OK\tclicking position [2|4] on field set every position to 1:\n\n\t1 1 1 1 1\t\t1 1 1 1 1\n\t1 1 1 1 0\t\t1 1 1 1 1\n\t1 1 1 0 0\t\t1 1 1 1 1\n\t1 1 1 1 0\t\t1 1 1 1 1\n\t1 1 1 1 1\t\t1 1 1 1 1')

    T.insert(END, '\n\n')

    T.insert(END, '------------------------------------------------------------------------------------------\n')


# Test check_if_solved function
def test_check_if_solved():
    T.insert(END, 'Test check_if_solved function:\n\n')

    # Test if field is solved should return false
    field = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]

    if exercise.check_if_solved(field):
        T.insert(END,
                 'FAILED\tchecking if field is solved should not be true:\n\n\t1 1 1 1 1\n\t1 1 1 1 0\n\t1 1 1 0 0\n\t1 1 1 1 0\n\t1 1 1 1 1')
    else:
        T.insert(END,
                 'OK\tchecking if field is solved is false:\n\n\t1 1 1 1 1\n\t1 1 1 1 0\n\t1 1 1 0 0\n\t1 1 1 1 0\n\t1 1 1 1 1')

    T.insert(END, '\n\n')

    # Test if field is solved should return false
    field = [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 0]]

    if exercise.check_if_solved(field):
        T.insert(END,
                 'FAILED\tchecking if field is solved should not be true:\n\n\t0 0 1 0 0\n\t0 1 0 0 0\n\t0 1 0 1 0\n\t0 0 0 1 1\n\t1 0 0 1 0')
    else:
        T.insert(END,
                 'OK\tchecking if field is solved is false:\n\n\t0 0 1 0 0\n\t0 1 0 0 0\n\t0 1 0 1 0\n\t0 0 0 1 1\n\t1 0 0 1 0')

    T.insert(END, '\n\n')

    # Test if field is solved should return true
    field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    if exercise.check_if_solved(field):
        T.insert(END,
                 'OK\tchecking if field is solved is true:\n\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0')
    else:
        T.insert(END,
                 'FAILED\tchecking if field is solved should not be false:\n\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0\n\t0 0 0 0 0')

    T.insert(END, '\n\n')

    T.insert(END, '------------------------------------------------------------------------------------------\n')


def test_user_input():
    T.insert(END, 'Test user_input function:\n\n')

    # Test if function throws error
    exercise.input = lambda inp: str(-1)

    try:
        exercise.user_input()
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (-1, -1)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (-1, -1)\n')

    exercise.input = lambda inp: str(5)

    try:
        exercise.user_input()
    except ValueError:
        T.insert(END, 'OK\tthrows ValueError for (5, 5)\n')
    else:
        T.insert(END, 'FAILED\tdoes not throw ValueError for (5, 5)\n')

    # Test if function returns a list
    exercise.input = lambda inp: '3'
    output = exercise.user_input()
    exercise.input = input

    if not type(output) == list:
        T.insert(END, 'FAILED\treturn value is not a list\n')
    else:
        T.insert(END, 'OK\treturn value is a list\n')

    # Test if list consists of two elements
    if len(output) == 2:
        T.insert(END, 'OK\tlist consists of two elements\n')
    else:
        T.insert(END, 'FAILED\tlist does not consist of two elements\n')

    T.insert(END, '------------------------------------------------------------------------------------------\n')


# Test print_field function
def test_convert_field():
    T.insert(END, 'Test convert_field function:\n\n')
    T.insert(END, 'Spaces will be replaced with [ ] for better visualization\n\n')

    # Test if function return str
    field = [[0, 0, 0, 1, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 1, 1, 0, 0]]
    string_representation = exercise.convert_field(field)

    if not type(string_representation) == str:
        T.insert(END, 'FAILED\treturn value is not str\n')
    else:
        T.insert(END, 'OK\treturn value is str\n')

    # First test
    string_representation = string_representation.replace(' ', '[ ]')

    if string_representation == '0[ ]0[ ]0[ ]1[ ]0\n1[ ]0[ ]0[ ]1[ ]0\n0[ ]0[ ]0[ ]0[ ]1\n0[ ]0[ ]0[ ]0[ ]0\n1[ ]1[ ]1[ ]0[ ]0':
        T.insert(END, 'OK\tstring representation of field should look like this:\n\n\t0[ ]0[ ]0[ ]1[ ]0\t\t\t0[ ]0[ ]0[ ]1[ ]0\n\t1[ ]0[ ]0[ ]1[ ]0\t\t\t1[ ]0[ ]0[ ]1[ ]0\n\t0[ ]0[ ]0[ ]0[ ]1\t\t\t0[ ]0[ ]0[ ]0[ ]1\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n\t1[ ]1[ ]1[ ]0[ ]0\t\t\t1[ ]1[ ]1[ ]0[ ]0\n')
    else:
        T.insert(END, 'FAILED\tstring representation of field should look like this:\n\n\t0[ ]0[ ]0[ ]1[ ]0\n\t1[ ]0[ ]0[ ]1[ ]0\n\t0[ ]0[ ]0[ ]0[ ]1\n\t0[ ]0[ ]0[ ]0[ ]0\n\t1[ ]1[ ]1[ ]0[ ]0\n\n\tbut was:\n\n\t')

        representation_list = string_representation.split('\n')

        for row in representation_list:
            T.insert(END, row)
            T.insert(END, '\n\t')

    T.insert(END, '\n')

    # Second test
    field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    string_representation = exercise.convert_field(field)
    string_representation = string_representation.replace(' ', '[ ]')

    if string_representation == '0[ ]0[ ]0[ ]0[ ]0\n0[ ]0[ ]0[ ]0[ ]0\n0[ ]0[ ]0[ ]0[ ]0\n0[ ]0[ ]0[ ]0[ ]0\n0[ ]0[ ]0[ ]0[ ]0':
        T.insert(END,
                 'OK\tstring representation of field should look like this:\n\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\t\t\t0[ ]0[ ]0[ ]0[ ]0\n')
    else:
        T.insert(END,
                 'FAILED\tstring representation of field should look like this:\n\n\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\n\t0[ ]0[ ]0[ ]0[ ]0\n\n\tbut was:\n\n\t')

        representation_list = string_representation.split('\n')

        for row in representation_list:
            T.insert(END, row)
            T.insert(END, '\n\t')

    T.insert(END, '\n')

    T.insert(END, '------------------------------------------------------------------------------------------\n')


if __name__ == '__main__':
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    T = Text(root, height=50, width=150, yscrollcommand=scrollbar.set)
    T.pack()
    test_functions_exist()

    try:
        test_get_neighbour_positions()
    except AttributeError:
        pass
    except TypeError:
        pass

    try:
        test_click_position()
    except AttributeError:
        pass
    except TypeError:
        pass

    try:
        test_check_if_solved()
    except AttributeError:
        pass
    except TypeError:
        pass

    try:
        test_user_input()
    except AttributeError:
        pass
    except TypeError:
        pass

    test_convert_field()
    mainloop()
