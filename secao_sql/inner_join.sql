SELECT u.id AS uid, p.id AS pid,
p.bio, u.first_name
FROM users AS u
INNER JOIN profiles p 
ON u.id = p.user_id
WHERE u.first_name LIKE '%er'
ORDER BY u.last_name DESC
LIMIT 4;