-- CREATE TABLE dogs (
--     name TEXT,
--     breed TEXT,
--     age INTEGER
-- );

-- .tables
-- .read basics.sql
-- .open dog_db.db

INSERT INTO dogs (name, age, breed) VALUES("Rose", 4, "Husy");
INSERT INTO dogs (name, age, breed) VALUES("Violet", 11, "Chihuahua");
INSERT INTO dogs (name, age, breed) VALUES("Lily", 5, "Labrador");
INSERT INTO dogs (name, age, breed) VALUES("Moose", 9 ,"Corgi");

SELECT * FROM dogs;
SELECT name from dogs;
SELECT name, age from dogs;

INSERT INTO dogs (name, age, breed) VALUES("Maggie", 4 "Terrier");
INSERT INTO dogs (name, age, breed) VALUES("River", 7 "Husky");
INSERT INTO dogs (name, age, breed) VALUES("Archer", 8 "Pitbull");
INSERT INTO dogs (name, age, breed) VALUES("Pam", 2 "Pug");

SELECT * FROM dogs WHERE name IS "Pam";
SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND BREED IS NOT "Pug";
SELECT * FROM dogs WHERE age > 8;
SELECT * FROM dogs WHERE name LIKE "%gg%";