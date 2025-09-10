use online_course_platform_db;

SELECT
  students.username as username,
  courses.title as course_title,
  feedback.COMMENT as comment
from feedback
INNER JOIN courses
  ON courses.id = feedback.course_id
INNER JOIN students
  ON students.id = feedback.student_id
WHERE
  students.username = 'john_doe';

SELECT
  students.username as username,
  courses.title as course_title,
  feedback.COMMENT as comment
FROM
  students
LEFT JOIN feedback ON feedback.student_id = students.id
LEFT JOIN courses ON courses.id = feedback.course_id
WHERE students.username = 'jane_smith';

SELECT f.comment
FROM students s
INNER JOIN feedback f ON s.id = f.student_id
WHERE s.username = 'mary_jones'
ORDER BY f.created_at DESC