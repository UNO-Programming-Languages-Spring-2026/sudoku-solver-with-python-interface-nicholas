row(1..9).
col(1..9).
num(1..9).

cell(X,Y) :- row(X), col(Y).

block(X,Y,BX,BY) :- row(X), col(Y), BX = (X-1)/3, BY = (Y-1)/3.

sudoku(X,Y,N) :- initial(X,Y,N).

1 { sudoku(X,Y,N) : num(N) } 1 :- cell(X,Y), not initial(X,Y,_).

:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 < Y2.
:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 < X2.

:- sudoku(X1,Y1,N), sudoku(X2,Y2,N),
   block(X1,Y1,BX,BY), block(X2,Y2,BX,BY),
   (X1,Y1) < (X2,Y2).

#show sudoku/3.