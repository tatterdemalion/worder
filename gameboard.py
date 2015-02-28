class Box(object):
    L2R = 'L2R'
    T2B = 'T2B'

    def __init__(self, board, x, y, value='', *args, **kwargs):
        self.board = board
        self.x = x
        self.y = y
        self.set(value)

    def __unicode__(self):
        return '[%s]' % (self.value or ' ')

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def set(self, value):
        if len(value) > 1:
            raise ValueError('Value must be either one char or None')
        self.value = value
        return self

    @property
    def left(self):
        if self.x > 0:
            return self.board.get(self.x - 1, self.y)

    @property
    def right(self):
        if self.x < self.board.width - 1:
            return self.board.get(self.x + 1, self.y)

    @property
    def above(self):
        if self.y > 0:
            return self.board.get(self.x, self.y - 1)

    @property
    def below(self):
        if self.y < self.board.width - 1:
            return self.board.get(self.x, self.y + 1)

    def first_empty(self, direction):
        if not self.value:
            return self
        _box = self
        if direction == self.L2R:
            while _box.value:
                _box = _box.right
        elif direction == self.T2B:
            while _box.value:
                _box = _box.below
        return _box

    def first_deployed(self, direction):
        if self.value:
            return self
        _box = self
        if direction == self.L2R:
            while not _box.value:
                _box = _box.right
        elif direction == self.T2B:
            while not _box.value:
                _box = _box.below
        return _box


class Board(list):
    def __init__(self, width=0, height=0, *args, **kwargs):
        super(Board, self).__init__(*args, **kwargs)
        self.height = height
        self.width = width
        self._init_rows()

    def _init_rows(self):
        for y in range(self.height):
            self.append([Box(self, x, y) for x in range(self.width)])
        return self

    def append(self, row):
        super(Board, self).append(row)
        self.height += 1
        self.width = len(row)

    def get(self, x, y):
        return self[y][x]


csv = """,a,b,a,,a,b
,,a,r,a,f,
s,a,l,,,,
,,,,,,
,,,,,,
,,,,,,"""
board = Board()
for y, line in enumerate(csv.split('\n')):
    row = [Box(board, x, y, val) for x, val in enumerate(line.split(','))]
    board.append(row)
