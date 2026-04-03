import sys
import clingo
from sudoku_board import Sudoku


class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.Symbol]:
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
        if len(files) != 1:
            raise RuntimeError("Expected exactly one input file.")

        with open(files[0], "r", encoding="utf-8") as f:
            puzzle_text = f.read()

        board = Sudoku.from_str(puzzle_text)
        self.context = Context(board)

        control.load("sudoku.lp")
        control.load("sudoku_py.lp")
        control.ground([("base", [])], context=self.context)
        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        printer(str(sudoku))
        return True


if __name__ == "__main__":
    app = SudokuApp()
    sys.exit(clingo.clingo_main(app, sys.argv[1:]))