import math
from colorama import init
from colorama import Fore, Back, Style
init()

words = []
en = ["GeometryCalc with formulas", "Made by Rene Ehlers", "Sidelength (no unit): ", "Sidelength", " Squareunits", "Squareroot(2) =", " Lengthunits", "First sidelength (a): ", "Second sidelength (b): ", "SU", "a ", "b ", "Long Side: ", "Short Side: ", "LU", "Main Menu", 16, "Square", "Rectangle", "Circle", "Triangle", "Exit"]
de = ["GeometryCalc mit Formelanzeige", "von Rene Ehlers", "Seitenlänge (ohne Einheit): ", "Seitenlänge", " Flächeneinheiten", "Wurzel (2) =", " Längeneinheiten", "Erste Seitenlänge (a): ", "Zweite Seitenlänge (b): ", "FE", "a ", "b ", "Lange Seite: ", "Kurze Seite: ", "LE", "Hauptmenü", 16, "Quadrat", "Rechteck", "Kreis", "Dreieck", "Beenden"]

def info():
    print(Fore.GREEN + words[0])
    print(Fore.GREEN + words[1])
    print(Fore.GREEN + "Published under: GNU GPLv3")
    print(Style.RESET_ALL)

def quadrat_fläche():
    quadrat_seitenlänge = input(words[2])
    quadrat_fläche_calc = float(quadrat_seitenlänge) * float(quadrat_seitenlänge)
    print(words[3], "x", words[3], " = ")
    print(Fore.GREEN + str(quadrat_fläche_calc), words[4])
    print(Style.RESET_ALL)

def quadrat_diagonale():
    quadrat_seitenlänge = input(words[2])
    quadrat_diagonale_calc = float(quadrat_seitenlänge) * math.sqrt(2)
    print(words[3], "x", words[5])
    print(Fore.GREEN + str(quadrat_diagonale_calc), words[6])
    print(Style.RESET_ALL)

def rechteck_fläche():
    seite1 = input(words[7])
    seite2 = input(words[8])
    fläche_rechteck_gesamt = float(seite1) * float(seite2)
    print(words[7], "x", words[8], " = ")
    print(" ____________")
    print(" |", round(float(fläche_rechteck_gesamt)), words[9],    "     |")
    print(" ------------ ")
    print(Fore.GREEN + str(fläche_rechteck_gesamt), words[5])
    print(Style.RESET_ALL)

def rechteck_umfang():
    seite1 = input(words[7])
    seite2 = input(words[8])
    umfang_rechteck_gesamt = float(seite1) * 2 + float(seite2) * 2
    print("(",words[10], "x 2) + (", words[11], "x 2) =")
    print(words[12])
    print("______" , max(float(seite1), float(seite2)), " x 2 = ", max(float(seite1), float(seite2)) * 2, words[14])
    print(words[13])
    print("|     ")
    print("|     " , min(float(seite1), float(seite2)), " x 2 = ", min(float(seite1), float(seite2)) * 2, words[14])
    print(Fore.GREEN + str(umfang_rechteck_gesamt), words[6])
    print(Style.RESET_ALL)

def rechteck_diagonale():
    seite1 = input(words[7])
    seite2 = input(words[8])
    diagonale_rechteck_gesamt = math.sqrt(float(seite1) ** 2 + float(seite2) ** 2)
    print("Wurzel aus -- > (Seitenlänge 1 ^ 2) + (Seitenlänge 2 ^ 2) =")
    print(Fore.GREEN + str(diagonale_rechteck_gesamt), words[6])
    print(Style.RESET_ALL)

def kreis_fläche():
    radius = input("Radius: ")
    kreis_fläche_gesamt = math.pi * float(radius) ** 2
    print("Pi x Radius ^ 2 =")
    print(Fore.GREEN + str(kreis_fläche_gesamt), words[4])
    print(Style.RESET_ALL)

def kreis_umfang():
    radius = input("Radius: ")
    kreis_umfang_gesamt = 2 * math.pi * float(radius)
    print("2 x Pi x Radius =")
    print(Fore.GREEN + str(kreis_umfang_gesamt), words[6])
    print(Style.RESET_ALL)

def dreieck_fläche():
    print("    /|\     ")
    print("   / | \    ")
    print("  /  |h \   ")
    print(" /   |   \  ")
    print("/____|____\ ")
    print("   a        ")
    seite = input("Eine Seite: ")
    höhe = input("Die Höhe der Seite: ")
    dreieck_fläche_ges = float(seite) * float(höhe) / 2
    print("Seite a x Höhe h->a")
    print(Fore.GREEN + str(dreieck_fläche_ges), words[4])
    print(Style.RESET_ALL)



def sub_menu_quadrat():
    print("\n")
    print("Menü zur Quadratberechnung")
    print("1. Quadrat Fläche:")
    print("2. Quadrat Diagonale:")
    print("m. Hauptmenü")
    print("e. Beenden")
    userselection = input("Programmauswahl: ")
    if userselection == "1":
        quadrat_fläche()
        sub_menu_quadrat()
    if userselection == "2":
        quadrat_diagonale()
        sub_menu_quadrat()
    if userselection == "m":
        menu()
    if userselection == "e":
        exit()

def sub_menu_rechteck():
    print("\n")
    print("Menü zur Rechteckberechnung")
    print("1. Rechteck Fläche:")
    print("2. Rechteck Umfang:")
    print("3. Rechteck Diagonale:")
    print("m. Hauptmenü")
    print("e. Beenden")
    userselection = input("Programmauswahl: ")
    if userselection == "1":
        rechteck_fläche()
        sub_menu_rechteck()
    if userselection == "2":
        rechteck_umfang()
        sub_menu_rechteck()
    if userselection == "3":
        rechteck_diagonale()
        sub_menu_rechteck()
    if userselection == "m":
        menu()
    if userselection == "e":
        exit()

def sub_menu_kreis():
    print("\n")
    print("Menü zur Kreisberechnung")
    print("1. Kreis Fläche:")
    print("2. Kreis Umfang:")
    print("m. Hauptmenü")
    print("e. Beenden")
    userselection = input("Programmauswahl: ")
    if userselection == "1":
        kreis_fläche()
        sub_menu_kreis()
    if userselection == "2":
        kreis_umfang()
        sub_menu_kreis()
    if userselection == "m":
        menu()
    if userselection == "e":
        exit()
def sub_menu_dreieck():
    print("\n")
    print("Menü zur Dreiecksberechnung")
    print("1. Dreieck Fläche:")
    print("m. Hauptmenü")
    print("e. Beenden")
    userselection = input("Programmauswahl: ")
    if userselection == "1":
        dreieck_fläche()
        sub_menu_dreieck()
    if userselection == "m":
        menu()
    if userselection == "e":
        exit()

def menu():
    print("\n")
    print(Fore.CYAN + words[15])
    print("1. ",words[17])
    print("2. ",words[18])
    print("3. ",words[19])
    print("4. ",words[20])
    print("e. ",words[21])
    print(Style.RESET_ALL)

    userselection = input("Programmauswahl: ")
    if userselection == "1":
        sub_menu_quadrat()
    if userselection == "2":
        sub_menu_rechteck()
    if userselection == "3":
        sub_menu_kreis()
    if userselection == "4":
        sub_menu_dreieck()
    if userselection == "e":
        exit()
def lang():
    print("Choose a language from below options")
    print("1. English")
    print("2. German")
    lan = input("Enter a number: ")
    if lan == "1":
        words.extend(en)
    if lan == "2":
        words.extend(de)
    if lan != "1" and lan != "2":
        print("\n")
        print(Fore.RED + "Invalid Language!")
        print(Style.RESET_ALL)
        print("Choose a valid Language by using the numbers (eg: 1) and press enter!")
        lang()


lang()
info()
menu()