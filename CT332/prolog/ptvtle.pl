ptvtle([],0) :- !.
ptvtle([_],[]).
ptvtle([],[_]).
ptvtle([H,_|T],[H|X]) :- ptvtle(T,X).