INSERT INTO user_roles (user_id, role_id)
select
id,
(SELECT id from roles order by RAND() LIMIT 1) as qualquer
from users;