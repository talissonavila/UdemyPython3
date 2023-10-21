INSERT INTO profiles 
(bio, description, user_id)
SELECT 
CONCAT('bio from ', first_name), 
CONCAT('description from ', first_name), 
id FROM
users;
