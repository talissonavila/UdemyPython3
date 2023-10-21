SELECT u.id as Users_id  , p.id as Profiles_id,
p.bio , u.first_name
FROM users as u, profiles as p
WHERE u.id = p.user_id;