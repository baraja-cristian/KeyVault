CREATE DATABASE Password_manager_python;
USE Password_manager_python;

CREATE TABLE Datos_personales(
	ID_datos_personales int AUTO_INCREMENT primary key,
    User_name varchar (50) NOT NULL,
    User_lastname varchar (50) NOT NULL,
    User_phone_number varchar (15) NULL,
	User_email VARCHAR(100) NOT NULL,
	User_password VARCHAR(100) NOT NULL,
    User_pin INT (4) NOT NULL
);

CREATE TABLE Info_data_user(
	ID_data_user int AUTO_INCREMENT primary key,
    ID_datos_personales int,
    Name_red_social varchar (50) NOT NULL,
    Usuario_red_social varchar (50) NOT NULL,
    Password_red_social varchar (50),
    FOREIGN KEY (ID_datos_personales) REFERENCES Datos_personales(ID_datos_personales) ON DELETE CASCADE ON UPDATE CASCADE
);
