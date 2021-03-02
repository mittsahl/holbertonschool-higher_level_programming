-- Creates User with only
-- read privileges and create database
CREATE DATABASE IF NOT EXISTS  htbn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON htbn_0d_2.* TO 'user_0d_2'@'localhost';
