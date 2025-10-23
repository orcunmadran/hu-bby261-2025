from rommenu import MenuSistemi

def fonksiyon1():
    print("Fonksiyon 1 çalıştırıldı.")

def fonksiyon2():
    print("Fonksiyon 2 çalıştırıldı.")

# Menüyü oluşturun
menu = MenuSistemi()
menu.karsilama("Örnek")

# Menü öğelerini ve karşılık gelen fonksiyonları bir sözlükte tanımlayın
# Anahtar: Menüde görünecek açıklama, Değer: Çağrılacak fonksiyon nesnesi
menu_items = {
    "Fonksiyon A": fonksiyon1,
    "Fonksiyon B": fonksiyon2
}

menu.menuyuCalistir(menu_items)