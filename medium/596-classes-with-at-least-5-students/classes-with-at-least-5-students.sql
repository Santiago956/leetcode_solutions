WITH min_student AS (
    SELECT 
        class,
        COUNT(student) AS qntd
    FROM Courses
    GROUP BY class
    HAVING COUNT(student) >= 5
)

SELECT
    class
FROM min_student;
