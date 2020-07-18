import math
from colorama import init
from colorama import Fore, Back, Style
init()

def info():
    print(Fore.GREEN + "Geometrie Rechner mit Formelanzeige")
    print(Fore.GREEN + "Made by Rene Ehlers")
    print(Fore.GREEN + "Published under: GNU GPLv3")
    print(Style.RESET_ALL)

def quadrat_fläche():
    quadrat_seitenlänge = input("Seitenlänge (ohne Einheit): ")
    quadrat_fläche_calc = float(quadrat_seitenlänge) * float(quadrat_seitenlänge)
    print("Seitenlänge x Seitenlänge =")
    print(Fore.GREEN + str(quadrat_fläche_calc), " Flächeneinheiten")
    print(Style.RESET_ALL)

def quadrat_diagonale():
    quadrat_seitenlänge = input("Seitenlänge (ohne Einheit): ")
    quadrat_diagonale_calc = float(quadrat_seitenlänge) * math.sqrt(2)
    print("Seitenlänge x Wurzel(2) =")
    print(Fore.GREEN + str(quadrat_diagonale_calc), " Längeneinheiten")
    print(Style.RESET_ALL)

def rechteck_fläche():
    seite1 = input("Erste Seitenlänge (a): ")
    seite2 = input("Zweite Seitenlänge (b): ")
    fläche_rechteck_gesamt = float(seite1) * float(seite2)
    print("Seitenlänge 1 x Seitenlänge 2 =")
    print(" ____________")
    print(" |", round(float(fläche_rechteck_gesamt)),     "FE     |")
    print(" ------------ ")
    print(Fore.GREEN + str(fläche_rechteck_gesamt), " Flächeneinheiten")
    print(Style.RESET_ALL)

def rechteck_umfang():
    seite1 = input("Erste Seitenlänge: ")
    seite2 = input("Zweite Seitenlänge: ")
    umfang_rechteck_gesamt = float(seite1) * 2 + float(seite2) * 2
    print("(Seitenlänge 1 x 2) + (Seitenlänge 2 x 2) =")
    print("Lange Seite: ")
    print("______" , max(float(seite1), float(seite2)), " x 2 = ", max(float(seite1), float(seite2)) * 2, " LE")
    print("Kurze Seite: ")
    print("|     ")
    print("|     " , min(float(seite1), float(seite2)), " x 2 = ", min(float(seite1), float(seite2)) * 2, " LE")
    print(Fore.GREEN + str(umfang_rechteck_gesamt), " Längeneinheiten")
    print(Style.RESET_ALL)

def rechteck_diagonale():
    seite1 = input("Erste Seitenlänge: ")
    seite2 = input("Zweite Seitenlänge: ")
    diagonale_rechteck_gesamt = math.sqrt(float(seite1) ** 2 + float(seite2) ** 2)
    print("Wurzel aus -- > (Seitenlänge 1 ^ 2) + (Seitenlänge 2 ^ 2) =")
    print(Fore.GREEN + str(diagonale_rechteck_gesamt), " Längeneinheiten")
    print(Style.RESET_ALL)

def kreis_fläche():
    radius = input("Radius: ")
    kreis_fläche_gesamt = math.pi * float(radius) ** 2
    print("Pi x Radius ^ 2 =")
    print(Fore.GREEN + str(kreis_fläche_gesamt), " Flächeneinheiten")
    print(Style.RESET_ALL)

def kreis_umfang():
    radius = input("Radius: ")
    kreis_umfang_gesamt = 2 * math.pi * float(radius)
    print("2 x Pi x Radius =")
    print(Fore.GREEN + str(kreis_umfang_gesamt), " Längeneinheiten")
    print(Style.RESET_ALL)

def sub_menu_quadrat():
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

def menu():
    print(Fore.BLUE + "Hauptmenü:")
    print("1. Quadrat")
    print("2. Rechteck")
    print("3. Kreis")
    print("e. Beenden")
    print(Style.RESET_ALL)

    userselection = input("Programmauswahl: ")
    if userselection == "1":
        sub_menu_quadrat()
    if userselection == "2":
        sub_menu_rechteck()
    if userselection == "3":
        sub_menu_kreis()
    if userselection == "e":
        exit()

info()
menu()