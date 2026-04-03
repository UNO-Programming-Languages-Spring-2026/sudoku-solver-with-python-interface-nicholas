import sys
import clingo


class SudokuApp(clingo.Application):
    program_name = "sudoku1"

    def main(self, control, files):
        control.load("sudoku.lp")
        for f in files:
            control.load(f)
        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        atoms = sorted(str(atom) for atom in model.symbols(shown=True))
        print(" ".join(atoms))
        return True


if __name__ == "__main__":
    app = SudokuApp()
    sys.exit(clingo.clingo_main(app, sys.argv[1:]))