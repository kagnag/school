man(marcus).
pompeian(marcus).
roman(X) :- pompeian(X).
lord(ceasar).
assassinate(X, Y) :- roman(X), lord(Y).
unloyalto(X, Y).
unloyalto(marcus, ceasar).

