(define (problem pdl)
    (:domain air-cargo)
    (:objects c1 c2 p1 p2 SFO JFK)
    (:init
        (cargo c1) (cargo c2) (plane p1) (plane p2)
        (airport SFO) (airport JFK)
        (at c1 SFO) (at c2 JFK) (at p1 SFO) (at p2 JFK)
    )
    (:goal (and (at c1 JFK) (at c2 SFO)))

)