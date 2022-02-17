even_odd_odd([H|T], Even, [H|Odd]) :- 
    even_odd_even(T, Even, Odd).
even_odd_odd([], [], []).