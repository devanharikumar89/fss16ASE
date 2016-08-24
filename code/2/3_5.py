def draw_plus_minus():
    """
    draws:
    + - - - -
    """
    print '+' + ' -' * 4,


def draw_pipe_space():
    """
    draws:
    |
    """
    print '|' + '  ' * 4,


def draw_plus_minus_plus_row(count):
    """
    draws draw_plus_minus() count times
    and append the result with '+'
    """
    for i in range(count):
        draw_plus_minus()
    print '+'


def draw_pipe_space_pipe_row(count):
    """
    draws draw_pipe_space() count times
    and append the result with '|'
    """
    for _ in range(count):
        draw_pipe_space()
    print '|'

rows = 4
columns = 4
cell_height = 4
for _ in range(columns):
    draw_plus_minus_plus_row(rows)
    for _ in range(cell_height):
        draw_pipe_space_pipe_row(rows)
draw_plus_minus_plus_row(rows)
