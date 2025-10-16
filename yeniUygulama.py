import rommenu

def fonksiyon1():
    print("Fonksiyon 1 çalıştırıldı.")

def fonksiyon2():
    print("Fonksiyon 2 çalıştırıldı.")

uygmenu = rommenu.MenuSistemi
uygmenu.karsilama("Yeni Uygulama")
uygmenu.menuOlustur(["1. Fonksiyon A", "2. Fonksiyon B"])