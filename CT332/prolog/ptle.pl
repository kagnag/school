ptle([],[]):-!.
ptle([H|T],[H|T1]):- 1 is H mod 2, ptle(T,T1), !.
ptle([_|T],T1):- ptle(T,T1).