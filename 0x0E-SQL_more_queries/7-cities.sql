-- Creates data base if not exists
-- db passed as arg
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
USE htbn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(id),
	name VARCHAR(256) NOT NULL
	);
