food(chicken).
food(apple).
food(X) :- eat(Y, X), alive(Y).
alive(bill).
eat(bill, peanut).
eat(john, X) :- food(X).
eat(sue, X) :- eat(bill, X).
