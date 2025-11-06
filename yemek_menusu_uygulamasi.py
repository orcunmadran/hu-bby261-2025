
import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk
import os

class YemekMenusuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Haftalık Yemek Menüsü")
        self.root.geometry("800x600")

        self.menu_data = self.load_menu_data("yemek_menusu.xml")
        self.image_references = []  # Resim referanslarını saklamak için

        self.create_widgets()
        self.show_meals("Pazartesi")

    def load_menu_data(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        menu = {}
        for gun in root.findall('gun'):
            gun_adi = gun.get('ad')
            yemekler = []
            for yemek in gun.findall('yemek'):
                yemek_adi = yemek.find('ad').text
                gorsel_yolu = yemek.find('gorsel').text
                yemekler.append({"ad": yemek_adi, "gorsel": gorsel_yolu})
            menu[gun_adi] = yemekler
        return menu

    def create_widgets(self):
        # Günlerin butonları için bir çerçeve
        days_frame = ttk.Frame(self.root, padding="10")
        days_frame.pack(fill="x")

        for day in self.menu_data.keys():
            button = ttk.Button(days_frame, text=day, command=lambda d=day: self.show_meals(d))
            button.pack(side="left", expand=True, fill="x", padx=5)

        # Yemeklerin gösterileceği alan
        self.meals_frame = ttk.Frame(self.root, padding="10")
        self.meals_frame.pack(fill="both", expand=True)

    def show_meals(self, day):
        # Önceki yemekleri temizle
        for widget in self.meals_frame.winfo_children():
            widget.destroy()
        
        self.image_references.clear()

        ttk.Label(self.meals_frame, text=f"{day} Menüsü", font=("Helvetica", 16, "bold")).pack(pady=10)

        meals = self.menu_data[day]
        for meal in meals:
            meal_frame = ttk.Frame(self.meals_frame, padding=5)
            meal_frame.pack(fill="x", pady=5)

            try:
                image_path = os.path.join(os.path.dirname(__file__), meal["gorsel"])
                img = Image.open(image_path)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                image_label = ttk.Label(meal_frame, image=photo)
                image_label.image = photo  # Referansı sakla
                self.image_references.append(photo)
                image_label.pack(side="left", padx=10)
            except FileNotFoundError:
                placeholder = ttk.Label(meal_frame, text="Görsel Yok", width=15, anchor="center")
                placeholder.pack(side="left", padx=10)

            ttk.Label(meal_frame, text=meal["ad"], font=("Helvetica", 12)).pack(side="left")


if __name__ == "__main__":
    root = tk.Tk()
    app = YemekMenusuApp(root)
    root.mainloop()
