tongptle([],0):- !.
tongptle([H|T], X):- 1 is H mod 2, tongptle(T,X1), X is X1 + H.
tongptle([H|T], X):- 0 is H mod 2, tongptle(T,X).