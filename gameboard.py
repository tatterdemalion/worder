board = [
    [[   ], ['a'], ['b'], ['a'], [   ], ['a'], ['b']],
    [[   ], [   ], ['a'], [   ], [   ], [   ], [   ]],
    [[   ], [   ], ['b'], [   ], [   ], [   ], [   ]],
    [['a'], ['d'], ['a'], [   ], [   ], [   ], [   ]],
    [[   ], [   ], [   ], [   ], [   ], [   ], [   ]],
    [[   ], [   ], [   ], [   ], [   ], [   ], [   ]],
    [[   ], [   ], [   ], [   ], [   ], [   ], [   ]],
]

lines_count = len(board) - 1
boxes_count = len(board[0]) - 1


def find_positions():
    for line_no, line in enumerate(board):
        for box_no, box in enumerate(line):
            if box_no < boxes_count and line_no < lines_count:
                if line[box_no + 1] or board[line_no + 1][box_no] and not box:
                    print line_no, box_no
            if box_no > 0 and line_no > 0:
                if line[box_no - 1] or board[line_no - 1][box_no] and not box:
                    print line_no, box_no

find_positions()


def read_words():
    def left2right(no, word):
        try:
            if line[no]:
                word.append(line[no][0])
                left2right(no + 1, word)
        except IndexError:
            pass
        return ''.join(word)

    for line_no, line in enumerate(board):
        for box_no, box in enumerate(line):
            if box_no > 0:
                if box and not line[box_no - 1]:
                    print left2right(box_no, [])
            else:
                if box:
                    print left2right(box_no, [])

read_words()
