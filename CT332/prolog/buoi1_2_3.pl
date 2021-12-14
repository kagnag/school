anh(an, binh).
chong(an, yen).
chong(binh, hoa).
vo(hoa, binh).
vo(yen, an).
me(hoa, khang).
emgai(khang, thinh).
emgai(hanh, dung).
emgai(hanh, lanh).
emtrai(thinh, cuong).
contrai(cuong, binh).
congai(lanh, an).
congai(dung, yen).
chi(lanh, dung).
cha(X, Y) :- chong(X, Z), me(Z, Y).
bac(X, Y) :- anh(X, Z), cha(Z, Y).
chu(X, Y) :- emtrai(X, Z), cha(Z, Y).
co(X, Y) :- emgai(X, Z), cha(Z, Y).
anhemruot(X, Y) :- cha(Z, X), cha(Z, Y), me(V, X), me(V, Y).
anhho(X, Y) :- contrai(X, Z), bac(Z, Y).
chiho(X, Y) :- congai(X, Z), bac(Z, Y).
emtraiho(X, Y) :- contrai(X, Z), chu(Z, Y).
emgaiho(X, Y) :- congai(X, Z), chu(Z, Y).