-- questao 1
INSERT INTO users (first_name, last_name, email, password_hash, salary)
VALUES
('Thiago', 'Andre', 'thbarbosa@email.com', 'voltaexalta', 9000),
('Pericles', 'Farias', 'pericao@email.com', 'melhoreuir', 1234),
('Gordinho', 'Do Surdo', 'saudades@email.com', 'mestre', 55532),
('Alexandre', 'Pires', 'amigos@email.com', 'spc123', 4577),
('Radio', 'Mania', 'aovivo@email.com', 'rjrjrjr', 7777);

-- questao 2
INSERT IGNORE INTO profiles 
(bio, description, user_id)
select
CONCAT('bio from ', first_name),
concat('description', first_name),
id from users;

-- questao 3
INSERT INTO user_roles (user_id, role_id) values
(
	(select id from users where email = 'thbarbosa@email.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'pericao@email.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'saudades@email.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'amigos@email.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'aovivo@email.com'),
	(select id from roles where name = 'POST')
);

-- questao 4
SELECT * FROM users 
order by id desc
limit 5;

-- questao 5
UPDATE users set first_name = 'Fala', last_name = 'Meu'
where id = 127;

-- questao 6
DELETE FROM user_roles WHERE user_id = (select id from users where email = 'aovivo@email.com')
and role_id = (select id from roles  WHERE name = 'POST');

-- questao 7
delete u from users as u
inner join user_roles as ur on u.id = ur.user_id 
inner JOIN roles as r on ur.role_id = r.id
WHERE r.name = 'PUT'
and u.id = 24;

-- questao 8
SELECT u.id as uid, u.first_name, r.name, p.bio
from users as u
inner join user_roles as ur on u.id = ur.user_id 
inner JOIN roles as r on ur.role_id = r.id
INNER join profiles p on p.user_id = u.id;

-- questao 9
SELECT u.id as uid, u.first_name, r.name, p.bio
from users as u
left join user_roles as ur on u.id = ur.user_id 
left JOIN roles as r on ur.role_id = r.id
left join profiles p on p.user_id = u.id;

-- questao 10
SELECT u.id as uid, u.first_name, r.name, p.bio, u.salary 
from users as u
left join user_roles as ur on u.id = ur.user_id 
left JOIN roles as r on ur.role_id = r.id
left join profiles p on p.user_id = u.id
order by u.salary desc;
