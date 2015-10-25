(defn problem1 [n]
  (let [div? #(zero? (mod %1 %2))]
    (reduce + (filter #(or (div? % 3) (div? % 5))
                      (range 1 n)))))

(println (problem1 10))
(println (problem1 1000))
