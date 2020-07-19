import math
from colorama import init
from colorama import Fore, Back, Style
init()

words = []
en = ["GeometryCalc with formulas", "Made by Rene Ehlers", "Sidelength (no unit): ", "Sidelength", " Squareunits", "Squareroot(2) =", " Lengthunits", "First sidelength (a): ", "Second sidelength (b): ", "SU", "a ", "b ", "Long Side: ", "Short Side: ", "LU", "Main Menu", 16, "Square", "Rectangle", "Circle", "Triangle", "Exit", "Other", "Program selection: ", "Squareroot", "Radius: ", "radius", "Side (a): ", "Height (a): ", "Side (a)", "Height (a)", 31, "Menu for square calculations", "Square Area:", "Square diagonal length", "Menu for rectangle calculations", "Rectangle Area:", "Rectangle Circumference:", "Rectangle Diagonal:", "Menu for circle calculations", "Circle Area:", "Circle Circumference", "Menu for trangle calculations", "Triangle Area:"]
de = ["GeometryCalc mit Formelanzeige", "von Rene Ehlers", "Seitenlänge (ohne Einheit): ", "Seitenlänge", " Flächeneinheiten", "Wurzel (2) =", " Längeneinheiten", "Erste Seitenlänge (a): ", "Zweite Seitenlänge (b): ", "FE", "a ", "b ", "Lange Seite: ", "Kurze Seite: ", "LE", "Hauptmenü", 16, "Quadrat", "Rechteck", "Kreis", "Dreieck", "Beenden", "Sonstiges", "Programmauswahl: ", "Wurzel", "Radius: ", "Radius", "Seite (a): ", "Höhe (a): ", "Seite (a)", "Höhe (a)", 31, "Menü zur Quadratberechnung", "Quadrat Fläche:", "Quadrat Diagonale:", "Menü zur Rechtecksberechnung", "Rechteck Fläche:", "Rechteck Umfang:", "Rechteck Diagonale:", "Menü zur Kreisberechnung", "Kreis Fläche:", "Kreis Umfang:", "Menü zur Dreiecksberechnung", "Dreieck Fläche:"]

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
    print(words[24]," -- > (",words[7]," ^ 2) + (",words[8]," ^ 2) =")
    print(Fore.GREEN + str(diagonale_rechteck_gesamt), words[6])
    print(Style.RESET_ALL)

def kreis_fläche():
    radius = input(words[25])
    kreis_fläche_gesamt = math.pi * float(radius) ** 2
    print("Pi x ",words[26]," ^ 2 =")
    print(Fore.GREEN + str(kreis_fläche_gesamt), words[4])
    print(Style.RESET_ALL)

def kreis_umfang():
    radius = input(words[25])
    kreis_umfang_gesamt = 2 * math.pi * float(radius)
    print("2 x Pi x ",words[26]," =")
    print(Fore.GREEN + str(kreis_umfang_gesamt), words[6])
    print(Style.RESET_ALL)

def dreieck_fläche():
    print("    /|\     ")
    print("   / | \    ")
    print("  /  |h \   ")
    print(" /   |   \  ")
    print("/____|____\ ")
    print("   a        ")
    seite = input(words[27])
    höhe = input(words[28])
    dreieck_fläche_ges = float(seite) * float(höhe) / 2
    print(words[29], "x", words[30])
    print(Fore.GREEN + str(dreieck_fläche_ges), words[4])
    print(Style.RESET_ALL)



def sub_menu_quadrat():
    print("\n")
    print(words[32])
    print("1.", words[33])
    print("2.", words[34])
    print("m.", words[15])
    print("e.", words[21])
    userselection = input(words[23])
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
    print(words[35])
    print("1.", words[36])
    print("2.", words[37])
    print("3.", words[38])
    print("m.", words[15])
    print("e.", words[21])
    userselection = input(words[23])
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
    print(words[39])
    print("1.", words[40])
    print("2.", words[41])
    print("m.", words[15])
    print("e.", words[21])
    userselection = input(words[23])
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
    print(words[42])
    print("1.", words[43])
    print("m.", words[15])
    print("e.", words[21])
    userselection = input(words[23])
    if userselection == "1":
        dreieck_fläche()
        sub_menu_dreieck()
    if userselection == "m":
        menu()
    if userselection == "e":
        exit()

def settings():
    print("\n")
    print(Fore.CYAN + words[22])
    lang()
    print(Style.RESET_ALL)

def menu_sel():
    userselection = input(words[23])
    if userselection == "1":
        sub_menu_quadrat()
    elif userselection == "2":
        sub_menu_rechteck()
    elif userselection == "3":
        sub_menu_kreis()
    elif userselection == "4":
        sub_menu_dreieck()
    elif userselection == "o":
        settings()
    elif userselection == "e":
        exit()
    else:
        print(Fore.LIGHTRED_EX +"Invalid!")
        print(Style.RESET_ALL)
        menu_sel()

def menu():
    print("\n")
    print(Fore.CYAN + words[15])
    print("1. ",words[17])
    print("2. ",words[18])
    print("3. ",words[19])
    print("4. ",words[20])
    print("o. ",words[22])
    print("e. ",words[21])
    print(Style.RESET_ALL)
    menu_sel()



def lang():
    print("Choose a language from below options")
    print("1. English")
    print("2. German")
    lan = input("Enter a number: ")
    if lan == "1":
        words.extend(en)
        info()
        menu()
    if lan == "2":
        words.extend(de)
        info()
        menu()
    if lan != "1" and lan != "2":
        print("\n")
        print(Fore.RED + "Invalid Language!")
        print(Style.RESET_ALL)
        print("Choose a valid Language by using the numbers (eg: 1) and press enter!")
        lang()


lang()