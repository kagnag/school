(define (problem up-ly1)
    (:domain up-ly)
    
    (:objects ly1 ly2 ly3 ly4 ly5 ly6)
    	
    (:init  (ly ly1) (ly ly2) (ly ly3) (ly ly4) (ly ly5) (ly ly6)
            (lientuc ly1 ly2 ly3) (lientuc ly2 ly3 ly4) 
            (lientuc ly3 ly4 ly5) (lientuc ly4 ly5 ly6)
            (isUp ly1) (isUp ly3) (isUp ly5))
    
    (:goal (and (not (isUp ly1)) (not (isUp ly2)) (not (isUp ly3))
            (not (isUp ly4)) (not (isUp ly5)) (not (isUp ly6))))
)