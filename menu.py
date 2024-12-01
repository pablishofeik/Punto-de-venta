import customtkinter as ctk
from image_file import find_image
from product import Product

def show_Menu_Screen(self):
    self.productScreen.pack_forget()  # Ocultar la segunda pantalla
    self.pack(fill="both", expand=True)  # Mostrar la primera pantalla

class MenuApp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        main_frame = ctk.CTkFrame(self, width=1024, height=800, corner_radius=0, fg_color="#969696")
        main_frame.place(x=0,y=0)
        main_frame.pack(fill="both", expand=True)

        top_frame = ctk.CTkFrame(main_frame, width=1024, height=50, corner_radius=0, fg_color="#FFFFFF")
        top_frame.place(x=0,y=0)
        top_frame.pack(fill="both", expand=True)

        menuScreen = ctk.CTkFrame(main_frame, width=1024, height=750, corner_radius=0, fg_color="#969696")
        menuScreen.place(x=0,y=50)
        menuScreen.pack(fill="both", expand=True)
        
        name = str("Hola, Juan!")

        seller_label = ctk.CTkLabel(top_frame, text=name, font=("Arial", 20, "bold"), text_color="#000000")
        seller_label.pack(pady=(0, 0))  # Espaciado entre elementos


        product_img = find_image("images/products.png", 50)
        product_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=product_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_product
        )

        product_button.image = product_img
        product_button.place(x=100, y=20)

        sales_img = find_image("images/sales.png", 70)
        sales_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=sales_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_sales
        )

        sales_button.image = sales_img
        sales_button.place(x=400, y=20)

        reports_img = find_image("images/report.png", 70)
        reports_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=reports_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_sales
        )

        reports_button.image = reports_img
        reports_button.place(x=700, y=20)

        clients_img = find_image("images/clients.png", 70)
        clients_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=clients_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_sales
        )

        clients_button.image = clients_img
        clients_button.place(x=100, y=300)

        workers_img = find_image("images/worker.png", 70)
        workers_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=workers_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_sales
        )

        workers_button.image = workers_img
        workers_button.place(x=400, y=300)

        settings_img = find_image("images/settings.png", 70)
        settings_button = ctk.CTkButton(
            menuScreen,
            text="", 
            image=settings_img, 
            width=200, 
            height=200, 
            fg_color="#FFFFFF", 
            command=self.Btn_sales
        )

        settings_button.image = settings_img
        settings_button.place(x=700, y=300)

        #self.productScreen = Product(self, show_Menu_Screen)
        

    
    def Btn_product(self):
        self.menuScreen.pack_forget()
        self.productScreen.pack(fill="both", expand=True)
    
    def Btn_sales(self):
        print("")

