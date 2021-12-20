demptchan([], 0).
demptchan([H|T], X):- H mod 2 =:= 0, demptchan(T,X1), X is X1 + 1.
demptchan([H|T], X):- H mod 2 =\= 0, demptchan(T,X).
