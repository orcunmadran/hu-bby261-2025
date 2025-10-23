#Lisans Seçici Prototipi

from rommenu import MenuSistemi

def ustveri():
    eserAdi = input("Eser Adı: ")
    eserSahibi = input("Eser Sahibi: ")
    userURL = input("Eser URL'si: ")
    sahipURL = input("Eser Sahibi URL'si: ")
    eserTarihi = input("Eser Tarihi (YYYY): ")

def zeropd():
    print("CC0 Sıfır (Zero): Kamu Malı tahsisi olarak kullanılır. Kullanımda olan son sürümü 1.0’dır. Resmi olarak Türkçe çevirisi yayınlanmıştır. Bu lisans kapsamında telif hakkı sınırlaması yoktur, kaynak atıf vermeden ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri()

def ccby():
    print("CC BY Atıf (Attribution): CC’nin en özgür lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri()

def ccbysa():
    print("CC BY-SA Atıf-AynıLisanslaPaylaş (Attribution-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir")
    ustveri()

def ccbynd():
    print("CC BY-ND Atıf-Türetilemez (Attribution-NonDerivative): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç da dahil olmak üzere kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri()

def ccbync():
    print("CC BY-NC Atıf-GayriTicari (Attribution-NonCommercial): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri()

def ccbyncsa():
    print("CC BY-NC-SA Atıf-GayriTicari-AynıLisanslaPaylaş (Attribution-NonCommercial-ShareAlike): Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek ve aynı lisansı devam ettirmek kaydıyla ticari amaç haricinde kopyalanabilir, düzenlenebilir, dağıtılabilir ve yeniden kullanılabilir.")
    ustveri()

def ccbyncnd():
    print("CC BY-NC-ND Atıf-GayriTicari-Türetilemez (Attribution-NonCommercial-NonDerivative): CC’nin en az özgürlük sağlayan lisansıdır. Kullanımda olan son sürümü 4.0’dır. Uluslararası olarak kullanılabilir. Resmi olarak Türkçe çevirisi yayınlanmıştır. Kaynak, atıf vermek kaydıyla ticari amaç haricinde kopyalanabilir, dağıtılabilir ve yeniden kullanılabilir, ancak üzerinde hiçbir değişiklik yapılamaz.")
    ustveri()

# Menüyü oluşturun
menu = MenuSistemi()
menu.karsilama("CC Lisans Seç")

# Menü öğelerini ve karşılık gelen fonksiyonları bir sözlükte tanımlayın
# Anahtar: Menüde görünecek açıklama, Değer: Çağrılacak fonksiyon nesnesi
menu_items = {
    "Kamu Malı / Public Domain": zeropd,
    "CC BY": ccby,
    "CC BY-SA": ccbysa,
    "CC BY-ND": ccbynd,
    "CC BY-NC": ccbync,
    "CC BY-NC-SA": ccbyncsa,
    "CC BY-NC-ND": ccbyncnd
}

menu.menuyuCalistir(menu_items)