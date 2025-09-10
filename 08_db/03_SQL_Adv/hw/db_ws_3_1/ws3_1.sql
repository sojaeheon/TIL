CREATE DATABASE online_course_platform_db
  DEFAULT CHARACTER SET 'utf8mb4';

use online_course_platform_db;

CREATE TABLE students(
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(100),
  name VARCHAR(100)
);

INSERT INTO students (username, name) VALUES
('john_doe', 'John Doe'),
('jane_smith', 'Jane Smith'),
('mary_jones', 'Mary Jones'),
('paul_brown', 'Paul Brown'),
('lisa_white', 'Lisa White'),
('tom_clark', 'Tom Clark');

CREATE TABLE courses(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100)
);

INSERT INTO courses (title) VALUES
('Introduction to Programming'),
('Data Science Fundamentals'),
('Web Development Basics'),
('Machine Learning'),
('Cybersecurity 101'),
('Cloud Computing');

CREATE TABLE feedback(
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  course_id INT,
  COMMENT TEXT,
  created_at TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO feedback (student_id, course_id, comment, created_at) VALUES
(1, 1, 'Great introductory course!', '2023-08-01 10:00:00'),
(2, 2, 'Very informative.', '2023-08-02 11:00:00'),
(3, 3, 'Helped me understand the basics.', '2023-08-03 12:00:00'),
(4, 4, 'Excellent course on ML.', '2023-08-04 13:00:00'),
(5, 5, 'Learned a lot about cybersecurity.', '2023-08-05 14:00:00'),
(6, 6, 'Comprehensive introduction to cloud computing.', '2023-08-06 15:00:00');

CREATE INDEX idx_students_username ON students(username);

CREATE INDEX idx_courses_title ON courses(title);