import sys
import clingo
from sudoku_board import Sudoku


class SudokuApp(clingo.Application):
    program_name = "sudoku4"

    def main(self, control, files):
        control.load("sudoku.lp")
        for f in files:
            control.load(f)

        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(str(sudoku))


if __name__ == "__main__":
    app = SudokuApp()
    sys.exit(clingo.clingo_main(app, sys.argv[1:]))