UPDATE users as us
join profiles p 
on p.user_id = us.id
SET p.bio = CONCAT(p.bio, 'atualizado') 
WHERE us.first_name = 'Tanner';


SELECT us.first_name, p.bio from users as us
join profiles p 
on p.user_id = us.id
WHERE us.first_name = 'Tanner';