(define (domain up-ly)
    (:requirements :strips)
    (:predicates (ly ?l) (isUp ?l) (lientuc ?lx ?ly ?lz))
    
    (:action lat3lyth1
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
            (not (isUp ?ly1)) (not (isUp ?ly2))(not (isUp ?ly3)))
    	:effect (and (isUp ?ly1) (isUp ?ly2) (isUp ?ly3)))
    
    (:action lat3lyth2
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
            (not (isUp ?ly1)) (not (isUp ?ly2)) (isUp ?ly3))
    	:effect (and (isUp ?ly1) (isUp ?ly2) (not (isUp ?ly3))))
    
    (:action lat3lyth3
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
            (not (isUp ?ly1)) (isUp ?ly2) (not (isUp ?ly3)))
    	:effect (and (isUp ?ly1) (not(isUp ?ly2)) (isUp ?ly3)))
    
    (:action lat3lyth4
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
            (not (isUp ?ly1)) (isUp ?ly2) (isUp ?ly3))
    	:effect (and (isUp ?ly1) (not (isUp ?ly2)) (not (isUp ?ly3))))
    
    (:action lat3lyth5
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
            (isUp ?ly1) (not (isUp ?ly2))(not (isUp ?ly3)))
    	:effect (and (not (isUp ?ly1)) (isUp ?ly2) (isUp ?ly3)))
    
    (:action lat3lyth6
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
             (isUp ?ly1) (not (isUp ?ly2)) (isUp ?ly3))
    	:effect (and (not (isUp ?ly1)) (isUp ?ly2) (not (isUp ?ly3))))
    
    (:action lat3lyth7
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
                (isUp ?ly1) (isUp ?ly2) (not (isUp ?ly3)))
    	:effect (and (not (isUp ?ly1)) (not (isUp ?ly2)) (isUp ?ly3)))
    	
    (:action lat3lyth8
        :parameters (?ly1 ?ly2 ?ly3)
    	:precondition (and (ly ?ly1) (ly ?ly2) (ly ?ly3)
    	        (lientuc ?ly1 ?ly2 ?ly3)
    	        (isUp ?ly1) (isUp ?ly2) (isUp ?ly3))
    	:effect (and (not (isUp ?ly1)) (not (isUp ?ly2))(not (isUp ?ly3))))
)
