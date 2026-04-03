row(1..9).
col(1..9).
num(1..9).

cell(X,Y) :- row(X), col(Y).

block(1..3,1..3).
block(1..3,4..6).
block(1..3,7..9).
block(4..6,1..3).
block(4..6,4..6).
block(4..6,7..9).
block(7..9,1..3).
block(7..9,4..6).
block(7..9,7..9).

% keep givens
sudoku(X,Y,N) :- initial(X,Y,N).

% fill remaining cells
1 { sudoku(X,Y,N) : num(N) } 1 :- cell(X,Y), not initial(X,Y,_).

% row constraint
:- row(X), num(N), 2 { sudoku(X,Y,N) : col(Y) }.

% column constraint
:- col(Y), num(N), 2 { sudoku(X,Y,N) : row(X) }.

% 3x3 block constraint
:- block(X1..X2,Y1..Y2), num(N), 2 { sudoku(X,Y,N) : X = X1..X2, Y = Y1..Y2 }.

#show sudoku/3.