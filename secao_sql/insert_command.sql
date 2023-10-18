-- seleciona base de dados
use base_de_dados;
-- Mostra tabelas da base de dados
show tables;
-- descreve colunas da tabela
DESCRIBE users;
-- Insert SQL
INSERT INTO users (first_name, last_name, email, password_hash) VALUES 
("Xandy", "Aviao", "avioes@email.com", "debarembar"),
("solanja", "Aviao", "sol@email.com", "xandinho"),
("Wesley", "Safadao", "garota@email.com", "safada");
