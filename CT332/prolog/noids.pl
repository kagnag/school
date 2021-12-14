noids([ ],L,L).
noids([X|L1],L2,[X|L3]) :- noids(L1,L2,L3).