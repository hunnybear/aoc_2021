import lib


class Cell(object):
    """
    Just a mutable glop of data leaking memory everywhere
    """

    def __init__(self, val, marked=False):
        self.marked = marked
        self.val = val

    def __bool__(self):
        return bool(self.marked)

    def __eq__(self, other):
        return other == self.val

    def __str__(self):
        if self.marked:
            return '><'
        return f'{self.val:02d}'

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return self.val + other


class Board(object):
    """
    A bingo board
    """

    def __init__(self, rows):
        if not len(rows) == 5 and all(len(row) == 5 for row in rows):
            raise ValueError('rows is wrong....s')

        self.rows = rows

    def __str__(self):
        """
        printing for debugging. Haven't even tried, but the point of this is
        giving me a place for my premature optimization and silly indulgences to run free
        """

        return '\n'.join(' '.join(str(v) for v in row) for row in self.rows)

    def mark(self, call: int) -> bool:
        """
        Not sure if numbers can occur more than once in a board, the instructions
        are not explicit, but it's not like i'm going to be judged on
        computational speed, so gonna save myself any hassle and just keep
        marking regardless of whether I've found one
        """

        for row in self.rows:
            for cell in row:
                if cell == call:
                    cell.marked = True

        return (
            any(all(row) for row in self.rows)
            or any(all(row[c] for row in self.rows) for c in range(len(self.rows)))
        )

    def score(self, final_call: int) -> int:

        return final_call * sum(sum(cell for cell in row if not cell.marked) for row in self.rows)

    @classmethod
    def create(cls, board):
        """ Generate the cell objects and stuff"""
        board = [[Cell(int(cell)) for cell in line.strip().split()] for line in board.splitlines() if line.strip()]
        return cls(board)


def run():
    in_data = lib.get_input().split('\n\n')
    calls = [int(v) for v in in_data.pop(0).split(',')]

    boards = [Board.create(board) for board in in_data]

    for call in calls:
        winners = list()

        for board in boards:
            if board.mark(call):
                if board not in winners:
                    winners.append(board)
        if winners:
            assert len(winners) == 1


            score = winners[0].score(call)
            if not score > 859:
                raise ValueError(f'score {score} is too low! (aoc sets floor at 859)')
            print('\n WINNING CARD\n\n')
            print(winners[0])
            print(f'\nscore:{score}')
            break


run()
