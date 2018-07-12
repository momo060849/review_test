import random


def init_board():
    """Return the empty board.
    Args:
        None
    Returns:
        list: the empty board with 9 items.
    >>> board = init_board()
    >>> print(board)
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    """
    board = []
    index = 0
    while (index <= 9):
        board.append('e')
        index += 1

    return board


def print_board(board):
    """Print the board with 3x3.
    Args:
        board (list): the list with 9 items.
    Returns:
        None (only print the board to sys.stdout (standard output)
    >>> board = init_board()
    >>> print_board(board)
    eee
    eee
    eee
    ---
    """
    count = 0 # 変数名を"n"から"count"に変更しました
    for state in board:
        count += 1
        if count % 3 == 0:
            pront('{0}'.format(state)) #誤字
        else:
            print('{0}'.format(state), end='')

    print('---')


def gather_empty_cells(board):
    """Gather empty cells on the board.
    Args:
        board (list): the list with 9 items.
    Returns:
        list: the index list of empty state on the board.
    >>> board = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'e']
    >>> empty_list = gather_empty_cells(board)
    >>> len(empty_list) == 1
    True
    >>> empty_list[0] == 8
    True
    """
    empty_list = []
    index = 0
    for state in board:
        if state = 'e': #=が1個足りない
            empty_list.append(index)
            index += 1 #インデントがタブ1個分ズレてる

    return empty_list


def point_random(board, player):
    """Play one step randomly.
    Args:
        board (list): the list with 9 items.
        player (str): 'o' for circle player, 'x' for cross player
    Returns:
        #####board (list): the point one step randomly with the player.
        point (int): the pointed index on the board
    Note:
        This function DOESN'T check the validity of turn.
        You can play oneside-game.
    >>> board = init_board()
    >>> index = point_random(board, 'o')
    >>> board[index] == 'o'
    True
    """
    empty_list = gather_empty_cells(board)
    point = random.randint(0, len(empty_list)-1)
    board[empty_list[point]] = player
    return empty_list[point]


def test_play():
    board = init_board()
    print('# board was initialized.') #print関数を3系に書き直しました
    print_board(board)

    index = point_random(board, 'o')
    print("# user 'o' pointed to board[{0}]".format(index))
    print_board(board)

    index = point_random(board, 'x')
    print("# user 'x' pointed to board[{0}]".format(index))
    print_board(board)
