-- Create new database
create database employee_new;

-- Select created database
use employee_new;

CREATE TABLE `tb_metadata` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `element` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE tb_employee_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(50),
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    mobile_number VARCHAR(10) UNIQUE NOT NULL,
    date_of_birth DATE,
    blood_group VARCHAR(10),
    gender VARCHAR(10),
    marital_status VARCHAR(10),
    highest_qualification_specialization VARCHAR(30),
    percentage_cgpa VARCHAR(5),
    year_of_passing VARCHAR(10),
    email VARCHAR(100),
    city VARCHAR(100),
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

  CREATE TABLE `tb_overallleave` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_name` VARCHAR(45) NULL,
  `earn_leave` INT,
  `casual_leave` INT, 
  `sick_leave` INT,
  `meternity_leave` INT,
  `peternity_leave` INT,
  PRIMARY KEY (`id`));

ALTER TABLE `employee_new`.`tb_employee_info` 
CHANGE COLUMN `job_title` `job_title` VARCHAR(100) NULL DEFAULT NULL ;

INSERT INTO tb_employee_info (employee_id, first_name, last_name, gender, date_of_birth, email, mobile_number, job_title, employment_status)
VALUES
('JDAA5101','John','Doe','Male','1980-05-15','johndoe@example.com','1234567891','Accountant', 'Active'),
('JSAA5102','Jane','Smith','Female','1985-08-22','janesmith@example.com','9876543210','HR Manager', 'Active'),
('MJAA5103','Michael','Johnson','Male','1990-03-10','michaeljohnson@example.com','5555555555','Software Engineer', 'Active'),
('EBAA5104','Emily','Brown','Female','1992-11-28','emilybrown@example.com','2223334444','Marketing Specialist', 'Active'),
('WCAA5105','William','Clark','Male','1988-07-19','williamclark@example.com','7778889999','Operations Manager', 'Active'),
('SAAA5106','Susan','Anderson','Female','1987-01-03','susananderson@example.com','4444444444','Financial Analyst', 'Active'),
('DLAA5107','David','Lee','Male','1982-09-12','davidlee@example.com','1112223333','Database Administrator', 'Active'),
('LMAA5108','Linda','Martinez','Female','1986-04-30','lindamartinez@example.com','8887776666','Recruiter', 'Active'),
('JWAA5109','James','White','Male','1991-06-17','jameswhite@example.com','6669991111','Marketing Coordinator', 'Active'),
('KJAA5110','Karen','Johnson','Female','1989-12-08','karenjohnson@example.com','3336669999','Logistics Coordinator', 'Active'),
('RMAA5111','Robert','Miller','Male','1983-03-25','robertmiller@example.com','5554443334','Senior Accountant', 'Active'),
('SWAA5112','Sarah','Williams','Female','1984-10-14','sarahwilliams@example.com','2223331111','Software Developer', 'Active'),
('CSAA5113','Christopher','Smith','Male','1980-02-05','christophersmith@example.com','7776665556','Marketing Manager', 'Active'),
('ECAA5114','Elizabeth','Clark','Female','1987-07-02','elizabethclark@example.com','4445556666','HR Assistant', 'Active'),
('MMAA5115','Matthew','Moore','Male','1993-05-20','matthewmoore@example.com','3335557777','Network Administrator', 'Active'),
('ALAA5116','Amy','Lewis','Female','1995-09-09','amylewis@example.com','5553337777','Operations Assistant', 'Active'),
('DWAA5117','Daniel','Wilson','Male','1981-11-15','danielwilson@example.com','2226667777','Financial Controller', 'Active'),
('KAAA5118','Kimberly','Anderson','Female','1990-08-12','kimberlyanderson@example.com','6664445555','Marketing Assistant', 'Active'),
('JHAA5119','Joseph','Hall','Male','1989-04-27','josephhall@example.com','8889991111','Inventory Manager', 'Active'),
('DMAA5120','Donna','Moore','Female','1985-01-19','donnamoore@example.com','5554449999','IT Manager', 'Active'),
('RMAA5121','Richard','Martin','Male','1984-06-03','richardmartin@example.com','4445551111','Financial Analyst', 'Active'),
('PMAA5122','Patricia','Robinson','Female','1982-03-08','patriciarobinson@example.com','6665559999','HR Director', 'Active'),
('CAAA5123','Charles','Anderson','Male','1994-07-26','charlesanderson@example.com','5554443333','Software Engineer', 'Active'),
('MAAA5124','Mary','Allen','Female','1988-12-14','maryallen@example.com','2226661111','Marketing Coordinator', 'Active'),
('THAA5125','Thomas','Harris','Male','1983-08-18','thomasharris@example.com','7775553333','Logistics Manager', 'Active'),
('LWAA5126','Laura','Walker','Female','1981-09-07','laurawalker@example.com','4443336666','Accountant', 'Active'),
('CPAA5127','Christopher','Perez','Male','1991-01-21','christopherperez@example.com','5554442222','Software Developer', 'Active'),
('ATAA5128','Amanda','Turner','Female','1995-04-06','amandaturner@example.com','6663331111','Marketing Specialist', 'Active'),
('MGAA5129','Matthew','Gonzalez','Male','1987-02-13','matthewgonzalez@example.com','7774441111','Recruiter', 'Active'),
('KPAA5130','Karen','Phillips','Female','1993-03-17','karenphillips@example.com','5555554444','Operations Coordinator', 'Active'),
('JWAA5131','James','Wright','Male','1990-12-29','jameswright@example.com','4443335555','Senior Accountant', 'Active'),
('JSAA5132','Jennifer','Scott','Female','1986-11-04','jenniferscott@example.com','8889995555','Database Administrator', 'Active'),
('MEAA5133','Michael','Evans','Male','1984-07-11','michaelevans@example.com','7776665555','Marketing Manager', 'Active'),
('MYAA5134','Michelle','Young','Female','1989-06-28','michelleyoung@example.com','6664443333','HR Assistant', 'Active'),
('DGAA5135','David','Green','Male','1995-05-24','davidgreen@example.com','5555553333','Network Administrator', 'Active'),
('LHAA5136','Linda','Hernandez','Female','1983-03-01','lindahernandez@example.com','4446667777','Operations Assistant', 'Active'),
('WHAA5137','William','Hall','Male','1981-02-09','williamhall@example.com','7773334444','Financial Controller', 'Active'),
('SLAA5138','Susan','Lopez','Female','1987-09-16','susanlopez@example.com','6663332222','Marketing Assistant', 'Active'),
('JKAA5139','Joseph','King','Male','1992-10-30','josephking@example.com','5555557777','Inventory Manager', 'Active'),
('KYAA5140','Karen','Young','Female','1986-04-14','karenyoung@example.com','4444443333','Software Engg', 'Active');

CREATE TABLE `tb_leave_applications` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` VARCHAR(45) NULL,
  `leave_type` VARCHAR(45) NULL,
  `from_date` DATE NULL,
  `to_date` DATE NULL,
  `status` VARCHAR(45) NULL,
  `applied_by` VARCHAR(100) NULL,
  `applied_on` DATETIME NULL,
  PRIMARY KEY (`id`));

ALTER TABLE `tb_attendance` 
CHANGE COLUMN `employee_name` `employee_id` VARCHAR(45) NULL DEFAULT NULL ;
