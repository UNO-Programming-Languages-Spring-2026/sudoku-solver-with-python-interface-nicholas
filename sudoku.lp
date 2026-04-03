row(1..9).
col(1..9).
num(1..9).

cell(X,Y) :- row(X), col(Y).

% block coordinates: 0,1,2 for row-block and col-block
block(X,Y,BX,BY) :- row(X), col(Y), BX = (X-1)/3, BY = (Y-1)/3.

% keep givens
sudoku(X,Y,N) :- initial(X,Y,N).

% fill remaining cells with exactly one number
1 { sudoku(X,Y,N) : num(N) } 1 :- cell(X,Y), not initial(X,Y,_).

% no repeated number in a row
:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 < Y2.

% no repeated number in a column
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 < X2.

% no repeated number in a 3x3 block
:- sudoku(X1,Y1,N), sudoku(X2,Y2,N),
   block(X1,Y1,BX,BY), block(X2,Y2,BX,BY),
   (X1,Y1) < (X2,Y2).

#show sudoku/3.