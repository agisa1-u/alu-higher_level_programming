-- Creates the database hbtn_0d_2 and the user user_0d_2 (password: user_0d_2_pwd)
-- with only the SELECT privilege on hbtn_0d_2; does not fail if either exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
