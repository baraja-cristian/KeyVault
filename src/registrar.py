from conecction_DB import *
import mariadb

class registrar():
    def __init__(self, nombres, apellidos, numero_telefono, email, contrasena, pin):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_de_telefono = numero_telefono
        self.email = email
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.contrasena = contrasena
        self.pin = pin

        self.connection = mariadb.connect(
            host="localhost",
            user="root",
            password="CrisBaraja10042",
            database="Password_manager_python"
        )
    def enviarDB(self):
        self.cursor = self.connection.cursor()

        consulta_SQL="""
        INSERT INTO Datos_personales (User_name, User_lastname, User_phone_number, User_email, User_password, User_pin)
        VALUES ("{}", "{}", "{}", "{}", "{}", {})""".format(self.nombres, self.apellidos, self.numero_de_telefono, self.email, self.contrasena, self.pin)
        self.cursor.execute(consulta_SQL)
        self.connection.commit()










































