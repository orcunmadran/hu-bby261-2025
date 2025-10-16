class MenuSistemi:

    def karsilama(program_adi):
        print(f"{program_adi} programına hoş geldiniz!")

    def menuOlustur(menuOgeleri):
        for oge in menuOgeleri:
            print(oge+"\n")
        secim = input("Bir seçenek giriniz: ")