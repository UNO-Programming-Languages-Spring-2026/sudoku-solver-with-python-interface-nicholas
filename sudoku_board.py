import clingo


class Sudoku:
    def __init__(self, board: dict[tuple[int, int], int]):
        self.board = board

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        board = {}
        for sym in model.symbols(shown=True):
            if sym.name == "sudoku" and len(sym.arguments) == 3:
                row = sym.arguments[0].number
                col = sym.arguments[1].number
                val = sym.arguments[2].number
                board[(row, col)] = val
        return cls(board)

    def __str__(self) -> str:
        rows = []
        for r in range(1, 10):
            vals = []
            for c in range(1, 10):
                vals.append(str(self.board[(r, c)]))

            line = (
                " ".join(vals[0:3]) + "  " +
                " ".join(vals[3:6]) + "  " +
                " ".join(vals[6:9])
            )
            rows.append(line)

        return (
            "\n".join(rows[0:3]) + "\n\n" +
            "\n".join(rows[3:6]) + "\n\n" +
            "\n".join(rows[6:9])
        )

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        board = {}
        row = 0

        for line in s.splitlines():
            line = line.strip()
            if not line:
                continue

            row += 1
            cells = line.split()

            for col, cell in enumerate(cells, start=1):
                if cell != "-":
                    board[(row, col)] = int(cell)

        return cls(board)