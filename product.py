import customtkinter as ctk
from image_file import find_image

class Product(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Esta es la pantalla 2")
        label.pack(pady=20)
        # Configuración de la ventana principal
        self.configure(fg_color="#450000")  # Fondo color #D6CDC6
        #button = ctk.CTkButton(self, text="Volver a la pantalla 1", command=self.cambiar_pantalla)
        #button.pack(pady=10)
