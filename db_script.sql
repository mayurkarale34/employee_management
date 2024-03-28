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

CREATE TABLE `employee_new`.`tb_attendance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(45) NULL,
  `clock_in` DATETIME NULL,
  PRIMARY KEY (`id`));

CREATE TABLE tb_employee_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(50),
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    mobile_number VARCHAR(10) UNIQUE NOT NULL,
    address VARCHAR(255),
    date_of_birth DATE,
    blood_group VARCHAR(10),
    gender VARCHAR(10),
    marital_status VARCHAR(10),
    highest_qualification_specialization VARCHAR(30),
    percentage_cgpa VARCHAR(5),
    year_of_passing VARCHAR(10),
    email VARCHAR(100),
    date_of_joining DATE,
    department VARCHAR(50),
    job_title VARCHAR(20),
    employment_type VARCHAR(15),
    employment_status VARCHAR(10),
    salary VARCHAR(20),
    areas_for_improvement VARCHAR(100),
    achievements VARCHAR(100),
    workshop_attended VARCHAR(100),
    certifications VARCHAR(100),
    skills_acquired VARCHAR(100)
);

CREATE TABLE `employee_new`.`tb_attendance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(45) NULL,
  `clock_in` TIME NULL,
  `attendance_date` DATE NULL,
  PRIMARY KEY (`id`));

-- Select created database
use employee_new;

  CREATE TABLE `tb_overallleave` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(45) NULL,
  `earn_leave` INT,
  `casual_leave` INT, 
  `sick_leave` INT,
  `meternity_leave` INT,
  `peternity_leave` INT,
  PRIMARY KEY (`id`));