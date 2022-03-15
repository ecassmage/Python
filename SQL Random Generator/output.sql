INSERT INTO Professor VALUES(1, 'Giselle', 'Luque', 'King', 'computers');
INSERT INTO Professor VALUES(2, 'Arlana', 'Rasmuson', 'King', 'math');
INSERT INTO Professor VALUES(3, 'Kimika', 'Leboeuf', 'King', 'biology');
INSERT INTO Professor VALUES(4, 'Deziree', 'Blasi', 'Count', 'science');
INSERT INTO Professor VALUES(5, 'Elen', 'Kutzer', 'King', 'biology');
INSERT INTO Professor VALUES(6, 'Laroya', 'Blau', 'Baron', 'science');
INSERT INTO Professor VALUES(7, 'Mikiala', 'Milan', 'Duke', 'biology');
INSERT INTO Professor VALUES(8, 'Chisholm', 'Sheskey', 'Duke', 'science');
INSERT INTO Professor VALUES(9, 'Marcus', 'Renzoni', 'Duke', 'science');
INSERT INTO Professor VALUES(10, 'Diana', 'Decourley', 'Duke', 'biology');

INSERT INTO Department VALUES(1, '1002A', 'science', 7);
INSERT INTO Department VALUES(2, '1003C', 'biology', 9);
INSERT INTO Department VALUES(3, '1001B', 'math', 3);
INSERT INTO Department VALUES(4, '1003B', 'computers', 2);
INSERT INTO Department VALUES(5, '1002C', 'chemistry', 2);

INSERT INTO Project VALUES(1, 'Delta', 503586.08, '1977-8-12', '1957-3-12', 2);
INSERT INTO Project VALUES(2, 'Blackberry', 416795.18, '1952-3-6', '1930-12-15', 3);
INSERT INTO Project VALUES(3, 'Eggton', 257609.41, '2016-5-24', '1979-1-25', 9);
INSERT INTO Project VALUES(4, 'Apple', 749180.24, '1932-6-7', '1911-7-1', 3);
INSERT INTO Project VALUES(5, 'Blackberry', 862896.37, '1966-7-25', '2019-6-24', 6);

INSERT INTO Graduate VALUES(1, 'Charvis', 'Pallant', 'Bachelors', 'math', 4, null);
INSERT INTO Graduate VALUES(2, 'Katira', 'House', 'Bachelors', 'computers', 4, null);
INSERT INTO Graduate VALUES(3, 'Arcelia', 'Jaime', 'Masters', 'computers', 3, null);
INSERT INTO Graduate VALUES(4, 'Flecia', 'Longanecker', 'Bachelors', 'science', 3, null);
INSERT INTO Graduate VALUES(5, 'Olegario', 'Mickell', 'Bachelors', 'math', 3, null);
INSERT INTO Graduate VALUES(6, 'Tonee', 'Mallari', 'Bachelors', 'science', 3, null);
INSERT INTO Graduate VALUES(7, 'Talika', 'Vanpoucke', 'Bachelors', 'biology', 4, null);
INSERT INTO Graduate VALUES(8, 'Allycia', 'Ensell', 'Masters', 'math', 5, null);
INSERT INTO Graduate VALUES(9, 'Kenroy', 'Yngsdal', 'Masters', 'biology', 4, null);
INSERT INTO Graduate VALUES(10, 'Vienna', 'Mannchen', 'Masters', 'computers', 2, null);

INSERT INTO works_on VALUES(8, 10, 2);
INSERT INTO works_on VALUES(1, 10, 4);
INSERT INTO works_on VALUES(5, 6, 4);
INSERT INTO works_on VALUES(2, 9, 4);
INSERT INTO works_on VALUES(7, 5, 2);

INSERT INTO works_in VALUES(45, 4, 8);
INSERT INTO works_in VALUES(39, 4, 7);
INSERT INTO works_in VALUES(35, 2, 3);
INSERT INTO works_in VALUES(96, 2, 8);
INSERT INTO works_in VALUES(13, 2, 8);
INSERT INTO works_in VALUES(54, 4, 1);
INSERT INTO works_in VALUES(85, 4, 10);
INSERT INTO works_in VALUES(65, 2, 10);
INSERT INTO works_in VALUES(61, 3, 10);
INSERT INTO works_in VALUES(21, 2, 10);
INSERT INTO works_in VALUES(56, 5, 8);
INSERT INTO works_in VALUES(10, 2, 2);
INSERT INTO works_in VALUES(28, 5, 4);
INSERT INTO works_in VALUES(13, 5, 10);
INSERT INTO works_in VALUES(27, 1, 6);

INSERT INTO co_investigator VALUES(1, 2);
INSERT INTO co_investigator VALUES(2, 10);
INSERT INTO co_investigator VALUES(2, 4);
INSERT INTO co_investigator VALUES(4, 10);
INSERT INTO co_investigator VALUES(3, 8);
INSERT INTO co_investigator VALUES(1, 3);

