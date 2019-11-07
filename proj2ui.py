"""
Sim
"""

"""
Constants for number coordinates
"""
ONE_TWO_ROW = 0
SIX_THREE_ROW = 10
FIVE_FOUR_ROW = 19

ONE_FIVE_COLUMN = 14
SIX_COLUMN = 4
THREE_COLUMN = 41
TWO_FOUR_COLUMN = 32

ONE_ROW = ONE_TWO_ROW
ONE_COLUMN = ONE_FIVE_COLUMN

TWO_ROW = ONE_TWO_ROW
TWO_COLUMN = TWO_FOUR_COLUMN

THREE_ROW = SIX_THREE_ROW

FOUR_ROW = FIVE_FOUR_ROW
FOUR_COLUMN = TWO_FOUR_COLUMN

FIVE_ROW = FIVE_FOUR_ROW
FIVE_COLUMN = ONE_FIVE_COLUMN

SIX_ROW = SIX_THREE_ROW

# List of all of the point coordinate constants for easy reference in a loop
POINTS = [[ONE_ROW, ONE_COLUMN], [TWO_ROW, TWO_COLUMN], [THREE_ROW, THREE_COLUMN],
          [FOUR_ROW, FOUR_COLUMN], [FIVE_ROW, FIVE_COLUMN], [SIX_ROW, SIX_COLUMN]]

# How far off of a line a "pixel" can fall to be counted on that line
LINE_ERROR_TOLERANCE = 0.021


def get_coordinate_lines(point_lines):
    """
    Translates the points (point 1, point 2, etc) to their cartesian coordinates bases on the constant list POINTS
    :param point_lines: 2d lists of lines, e.g. [[1, 3], [2, 6], [5, 3]]
    :return:
    """
    lines = []
    for point_line in point_lines:
        coords = []
        for point in point_line:
            coords.append(POINTS[point - 1])
        lines.append(coords)
    return lines


def get_distance(x1, y1, x2, y2):
    """
    Get the cartesian distance between two points

    :param x1: x coordinate of the first point
    :param y1: y coordinate of the first point
    :param x2: x coordinate of the second point
    :param y2: y coordinate of the second point
    :return: the float of the distance between the two points
    :rtype: float
    """
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)


def is_on_line(x, y, line):
    """
    Returns true if (x,y) is on a line.
    :param x: x coordinate of point
    :param y: y coordinate of point
    :param line: a 2d list of two x,y coordinates
    :return: true if (x,y) is on line (within LINE_ERROR_TOLERANCE)
    """
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    distance_to_1 = get_distance(x, y, x1, y1)
    distance_to_2 = get_distance(x, y, x2, y2)
    line_length = get_distance(x1, y1, x2, y2)
    if abs(distance_to_1 + distance_to_2 - line_length) < LINE_ERROR_TOLERANCE:
        return True
    return False


def get_pixel(i, j, p1_lines, p1_character, p2_lines, p2_character):
    """
    Given a list of line endpoints, determines whether the supplied pixel falls on one of those lines
    :param i: x coordinate of the pixel
    :param j: y coordinate of the pixel
    :param p1_lines: list of lines for player 1  e.g. [[1, 3], [2, 6], [5, 3]]
    :param p1_character: character for rendering player 1
    :param p2_lines: list of lines for player 2  e.g. [[1, 3], [2, 6], [5, 3]]
    :param p2_character: character for rendering player 2
    :return: the character that should be rendered for i,j
    """
    p1_coordinate_lines = get_coordinate_lines(p1_lines)
    p2_coordinate_lines = get_coordinate_lines(p2_lines)

    for line in p1_coordinate_lines:
        if is_on_line(i, j, line):
            return p1_character

    for line in p2_coordinate_lines:
        if is_on_line(i, j, line):
            return p2_character
    return ' '


def print_board(p1_lines, p1_character, p2_lines, p2_character):
    """
    Renders a game board and prints it to terminal

    :param p1_lines: lines for player one e.g. [[1, 3], [2, 6], [5, 3]]
    :param p1_character: the character that the lines will render with for player one
    :param p2_lines: ines for player two e.g. [[1, 3], [2, 6], [5, 3]]
    :param p2_character: the character that the lines will render with for player two
    :return: None
    """
    board = []

    # create 2d list for board characters (have to use a list so I can change by x,y coordinates)
    for i in range(FIVE_ROW + 1):
        row = []
        for j in range(THREE_COLUMN + 1):
            row.append(' ')
        board.append(row)

    for i in range(FIVE_ROW + 1):
        for j in range(THREE_COLUMN + 1):
            board[i][j] = get_pixel(i, j, p1_lines, p1_character, p2_lines, p2_character)

    # place the numbers
    board[ONE_ROW][ONE_COLUMN] = '1'
    board[TWO_ROW][TWO_COLUMN] = '2'
    board[THREE_ROW][THREE_COLUMN] = '3'
    board[FOUR_ROW][FOUR_COLUMN] = '4'
    board[FIVE_ROW][FIVE_COLUMN] = '5'
    board[SIX_ROW][SIX_COLUMN] = '6'

    # actually print the board
    for row in board:
        print(''.join(row))


if __name__ == '__main__':
    p1_lines = [[1, 2], [2, 4], [1, 6], [5, 6], [1, 6], [5, 2], [2, 6], [5, 3]]
    print_board(p1_lines, '@',
                [[3, 6], [4, 5], [1, 5], [2, 3], [1, 4], [4, 3], [1, 3], [4, 6]], '#')
