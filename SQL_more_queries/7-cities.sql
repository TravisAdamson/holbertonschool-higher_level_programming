-- Creates database hbtn_0d_usa, the table states on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT FOREIGN KEY NOT NULL REFERENCES hbtn_0d_usa.states.id,name VARCHAR(256) NOT NULL);