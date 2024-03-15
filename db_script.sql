-- Create new database
create database employee_new;

-- Select created database
use employee_new;

CREATE TABLE `tb_metadata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `element` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
  
-- Select created database
use employee_new;

CREATE TABLE attendance ( 
 `employee_name` VARCHAR(50), 
 `clock_in_time` TIME
); 







