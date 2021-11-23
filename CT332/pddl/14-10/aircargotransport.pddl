(define (domain air-cargo)

    (:requirements :strips)
    (:predicates    (in ?obj ?place) (at ?ojb ?place) (cargo ?obj)
                    (plane ?obj) (airport ?obj))
    (:action LOAD
        :parameters (?c ?p ?a)
        :precondition (and (at ?c ?a) (at ?p ?a) (cargo ?c) (plane ?p) (airport ?a))
        :effect (and (not (at ?c ?a)) (in ?c ?p))
    )
    (:action UNLOAD
        :parameters (?c ?p ?a)
        :precondition (and (in ?c ?p) (at ?p ?a) (cargo ?c) (plane ?p) (airport ?a))
        :effect (and (not (in ?c ?p)) (at ?c ?a))
    )
    (:action FLY
        :parameters (?p ?from ?to)
        :precondition (and (at ?p ?from) (plane ?p) (airport ?from) (airport ?to))
        :effect (and (not (at ?p ?from)) (at ?p ?to))
    )
)