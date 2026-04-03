import sys
import clingo
from sudoku_board import Sudoku


class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self):
        facts = []
        for (row, col), val in sorted(self.board.board.items()):
            facts.append(
                clingo.Function(
                    "initial",
                    [
                        clingo.Number(row),
                        clingo.Number(col),
                        clingo.Number(val)
                    ]
                )
            )
        return facts


class SudokuApp(clingo.Application):
    program_name = "sudoku6"

    def __init__(self):
        super().__init__()
        self.context = None

    def main(self, control, files):
        with open(files[0], "r", encoding="utf-8") as f:
            text = f.read()

        board = Sudoku.from_str(text)
        self.context = Context(board)

        control.load("sudoku.lp")
        control.load("sudoku_py.lp")
        control.ground([("base", [])], context=self.context)
        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(str(sudoku))


if __name__ == "__main__":
    app = SudokuApp()
    sys.exit(clingo.clingo_main(app, sys.argv[1:]))