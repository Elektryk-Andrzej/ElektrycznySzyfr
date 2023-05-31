klucze = [
    ' ', '!', '?', '/', ':', '(', ')', '.', ',', '[', ']', '@', '#', '$', '&', '%', '^', '|', '-', '+', '*', '=', '_', '{', '}', '<', '>', '\'', '\"',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'X',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'x',
    'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż', 'ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
]
while True:
    zakodowanaWaidomość = []
    zdekodowanaWaidomość = []

    wybór = input("\"S\" = Szyfrowanie | \"O\" = Odszyfrowywanie | \"W\" = Wyjdź ->")

    if wybór.upper() == "S":
        import random

        zdanie = input("Wprowadź zdanie ->")

        lista_znaków_kodowanych = list(zdanie)

        try:
            for znak in lista_znaków_kodowanych:
                klucz_znaku = klucze.index(znak)
                losowy_klucz = klucz_znaku

                while klucz_znaku == losowy_klucz:
                    losowy_klucz = random.randint(5, len(klucze)-5)

                if losowy_klucz < klucz_znaku:
                    domena_znaku = klucz_znaku - losowy_klucz
                    zakodowanaWaidomość.append(f"{domena_znaku};{losowy_klucz}`")

                else:
                    domena_znaku = losowy_klucz - klucz_znaku
                    zakodowanaWaidomość.append(f"~{domena_znaku};{losowy_klucz}`")

        except:
            print(f"Wystąpił błąd! Dodałeś znaki które nie są obsługiwane przez ten szyfr.\nTekst: {zdanie}")

        print(f"Oto twoja zaszyfrowana wiadomość:\n\n> {''.join(zakodowanaWaidomość)}\n")



    elif wybór.upper() == "O":
        skończono_skan = False

        zdanie = input("Wprowadź szyfr ->")

        zbiory = zdanie.split("`")

        for zbiór in zbiory:
            zbiór = zbiór.split(";")

            for kod in zbiór:

                if kod.__contains__("~") == True:
                    kod = kod.replace("~", "")
                    czy_dodawanie = False
                    zbiór[0] = kod
                else:
                    if skończono_skan == False:
                        czy_dodawanie = True

                if skończono_skan == True:
                    domena_znaku = zbiór[0]
                    klucz_znaku = zbiór[1]


                    if czy_dodawanie == True:
                        zdekodowany_znak = int(domena_znaku) + int(klucz_znaku)
                    else:
                        zdekodowany_znak = int(klucz_znaku) - int(domena_znaku)

                    zdekodowany_znak = klucze[zdekodowany_znak]
                    zdekodowanaWaidomość.append(zdekodowany_znak)
                    skończono_skan = False

                else:
                    skończono_skan = True

        print(f"Oto twoja odszyfrowana wiadomość:\n\n> \"{''.join(zdekodowanaWaidomość)}\"\n")
    elif wybór.upper() == "W":
        break