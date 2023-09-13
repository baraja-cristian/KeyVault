from tkinter import ttk
from tkinter import *
from conecction_DB import *
from PIL import ImageTk, Image
import os


class ventana_login():
    def __init__(self, window):
        # INFORMACION BÁSICA DE LA VENTANA
        self.window = window
        self.window.title("Login")
        self.window.resizable(False, False)
        self.window.config(bg="black")
        # CENTRAMOS LA VENTANA DEL LOGIN
        ancho_ventana = 259
        alto_ventana = 300
        x_ventana = self.window.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.window.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.window.geometry(posicion)

        ##ACCEDE A LA RUTA PRINCIPAL DEL PROYECTO
        c_principal = os.path.dirname(__file__)
        print(c_principal)
        ##ACCEDE A LA CAPETA IMG
        c_img = os.path.join(c_principal, "img")
        print(c_img)

        ## POCICIONAMIENTO DEL FRAME DE LOS IMPUST DEL CAMPO DE LOGIN
        self.frame_login = LabelFrame(self.window, background="black", borderwidth=0, highlightbackground="red")
        self.frame_login.config(padx=20, pady=20)
        self.frame_login.grid()

        ## img logo
        label_logo_img = ImageTk.PhotoImage(Image.open(os.path.join(c_img, "KeyVault_logo_login.png")).resize((200,70)))
        ## Label logo
        label_logo = Label(self.frame_login, image=label_logo_img, borderwidth=0)
        label_logo.label_logo_img=label_logo_img
        label_logo.grid(row=1, column=1)

        ## Label, imput texto USUARIO
        Label(self.frame_login, text="Usuario", bg="black", fg="#F2E7DC" ).grid(row=2, column=1,)
        self.usuario = Entry(self.frame_login)
        self.usuario.config(width=30, borderwidth=0)
        self.usuario.grid(row=3, column=1, pady=5)

        ## Label, imput texto CONTRASEÑA
        Label(self.frame_login, text="Contraseña ", bg="black", fg="#F2E7DC").grid(row=4, column=1)
        self.contraseña = Entry(self.frame_login)
        self.contraseña.config(width=30, borderwidth=0, show="*")
        self.contraseña.grid(row=5, column=1, pady=5)

        ## Crear un objeto ttk.Style para personalizar los BTN
        style = ttk.Style()

        # Crear un estilo personalizado para el BTN, BTN login
        style.configure("style_btn_login.TButton", foreground="#F2E7DC",borderwidth=0,background="#7843e6")
        btn_login = ttk.Button(self.frame_login, text="Ingresar", command=self.validar_login)
        btn_login.config(width=30, style="style_btn_login.TButton")
        btn_login.grid(row=6, column=1, pady=8)

        # Crear un estilo personalizado para el BTN, BTN Crear cuenta
        self.vn_resgistrar= ventan_registrar(self.window)

        style.configure("style_btn_register.TButton",foreground="#F2E7DC",borderwidth=0,background="#7843e6")
        btn_register = ttk.Button(self.frame_login, text="Nuevo",   command=self.vn_resgistrar.mostar_ventan_registro)
        btn_register.config(width=30, style="style_btn_register.TButton")
        btn_register.grid(row=7, column=1,pady=5)


    def validar_login(self):
        
        if len(self.usuario.get()) != 0 and len(self.contraseña.get()) != 0:
            self.conn = DB(self.window, self.frame_login ,self.message_temp)
            self.conn.validar_login(self.usuario.get(), self.contraseña.get())
            #print("Login con exito")
        else:
            self.message_temp("Campos vacios", "#F2E7DC", self.frame_login)
            #print("Llena los campos")

    def message_temp(self, type_message, color_message, clase_rame_labe):
        self.label_message = Label(clase_rame_labe, text=type_message, borderwidth=0, bg="black", foreground=color_message)
        self.label_message.grid(row=8, column=1)
        clase_rame_labe.after(3000, self.eliminar_mensaje)

    def eliminar_mensaje(self):
        # Función para eliminar el mensaje de los errores
        if hasattr(self, 'label_message'):
            self.label_message.destroy()

class ventan_registrar():
    def __init__(self, window):
        self.vn_resgistrar = window
        #self.connection = connection

    def mostar_ventan_registro(self):
        self.vn_resgistrar = tk.Toplevel(self.vn_resgistrar)
        self.vn_resgistrar.geometry("450x350") #COLOR DE FONDO
        self.vn_resgistrar.resizable(False, False)
        self.vn_resgistrar.config(bg="#000000")

        ##ACCEDE A LA CAPETA PRINCIPAL
        c_principal = os.path.dirname(__file__)
        ##ACCEDE A LA CAPETA IMG
        c_img = os.path.join(c_principal, "img")
        ####
        labelFrame_logo = LabelFrame(self.vn_resgistrar, borderwidth=0, bg="#000000")
        labelFrame_logo.grid(row=0, column=0)

        label_logo_img = ImageTk.PhotoImage(Image.open(os.path.join(c_img, "crear_cuenta_logo.png")))
        label_logo = Label(labelFrame_logo, image=label_logo_img, borderwidth=0)
        label_logo_img.label_logo_img = label_logo_img
        label_logo.grid(row=1, column=0)

        labelFrame = LabelFrame(self.vn_resgistrar, borderwidth=0, bg="#000000")
        labelFrame.grid(row=1, column=0)

        label_txt_nombre = Label(labelFrame, text="Ingrese su nombre", bg="#000000", fg="#FFFAEF")
        label_txt_nombre.grid(row=0, column=0, pady=5, padx=20)
        self.entry_nombre = Entry(labelFrame, borderwidth=0)
        self.entry_nombre.grid(row=1, column=0, pady=5, padx=20)

        label_txt_apellido = Label(labelFrame, text="Ingrese su apellido",bg="#000000", fg="#FFFAEF")
        label_txt_apellido.grid(row=0, column=1, pady=5, padx=20)
        self.entry_apellido = Entry(labelFrame, borderwidth=0)
        self.entry_apellido.grid(row=1, column=1, pady=5, padx=20)

        label_txt_numero_telefono = Label(labelFrame, text="Ingrese su número de teléfono", bg="#000000", fg="#FFFAEF")
        label_txt_numero_telefono.grid(row=2, column=0, pady=5, padx=20)
        self.entry_telefono = Entry(labelFrame, borderwidth=0)
        self.entry_telefono.grid(row=3, column=0, pady=5, padx=20)

        label_txt_numero_email = Label(labelFrame, text="Ingrese su email",bg="#000000", fg="#FFFAEF")
        label_txt_numero_email.grid(row=2, column=1, pady=5, padx=20)
        self.entry_telefono = Entry(labelFrame, borderwidth=0)
        self.entry_telefono.grid(row=3, column=1, pady=5,padx=20)

        label_txt_contrasena = Label(labelFrame, text="Ingrese una contraseña",bg="#000000", fg="#FFFAEF")
        label_txt_contrasena.grid(row=4, column=0, pady=5, padx=20)
        self.entry_contrasena = Entry(labelFrame, borderwidth=0)
        self.entry_contrasena.grid(row=5, column=0, pady=5, padx=20)

        label_txt_pin = Label(labelFrame, text="Ingrese un pin de 4 números",bg="#000000", fg="#FFFAEF")
        label_txt_pin.grid(row=4, column=1, pady=5, padx=20)
        self.entry_pin = Entry(labelFrame, borderwidth=0)
        self.entry_pin.grid(row=5, column=1, pady=5,padx=20)

        style = ttk.Style()
        style.configure("style_btn_register_.TButton",foreground="#000000", background="#000000", borderwidth=0)

        btn_crear_C_img = ImageTk.PhotoImage(Image.open(os.path.join(c_img, "btn_crear_cuenta.png")).resize((115,43)))

        btn_crearC_ = ttk.Button(labelFrame, image=btn_crear_C_img,)
        btn_crearC_.config(width=30, style="style_btn_register_.TButton")
        btn_crearC_.btn_crear_C_img=btn_crear_C_img
        btn_crearC_.grid(row=7, column=1)

        btn_crear_cerrar_img = ImageTk.PhotoImage(Image.open(os.path.join(c_img, "btn_crear_cerar_V.png")).resize((115,43)))
        btn_crear_cerrar = ttk.Button(labelFrame, image=btn_crear_cerrar_img, command=self.salir)
        btn_crear_cerrar.config(width=30, style="style_btn_register_.TButton")
        btn_crear_cerrar.btn_crear_cerrar_img=btn_crear_cerrar_img
        btn_crear_cerrar.grid(row=7, column=0)
    
    def salir(self):
        self.vn_resgistrar.destroy()