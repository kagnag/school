(define (problem pdl)
    (:domain air-cargo)
    (:objects c1 c2 c3 p1 noibai tansonnhat)
    (:init
        (Parkage c1) (Parkage c2) (Parkage c3) (Plane p1) 
        (Airport noibai) (Airport tansonnhat)
        (At c1 tansonnhat) (At c2 tansonnhat) (At c3 noibai)
		(At p1 noibai) 
    )
    (:goal (and (At c1 noibai) (At c2 noibai) (At c3 tansonnhat)))

)