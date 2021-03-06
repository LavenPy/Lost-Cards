# -*- encoding: iso-8859-15 -*-
#PYTHON-Version 2.7.14

"""
Autor: Robin Gysin
Project: uebung fuer kommende IPA, learning how to Python
Datum: 03.11.2017 - **.**.****
"""

"""
############################################
## Raumliste
############################################
##  1 = House from Street
##  2 = House outside West
##  3 = House outside Ost
##  4 = Garden
##
## 11 = Entry with Stairs
## 12 = Kitchen
## 13 = Living Room
## 14 = Dinning Room
## 14 = Garage
##
## 21 = Hall
## 22 = Child Sleeping Room
## 23 = Office
## 24 = Bath
## 25 = Sleeping Room Parents
##
## 31 = Dachboden
## 32 = Dach
############################################
"""

from random import randint
import time
import os

item_list = {
    "Seil": 1,              ## 1 = Im Besitz    0 = Nicht vorhanden
    "Key": 0,
    "Dinosaurier": 0,
    "Garage": 0,
    "Messer": 1,
    "Taschenlampe": 0,
    "Murmeln": 0,
    "Python": 0,
    "Lichtschwert": 0,
    "Kaffeetasse": 0,
    "Gummiboot": 0,
    "Kissen": 0,
    "Klammer": 0,
    "Brechstange": 0,
    "Alarmanlage": 0,       ## 1 = Aus          0 = An
    "Hund": 0               ## 1 = Wach         0 = Schlafend
}

word_list = []

def cls():
    os.system ( 'cls' if os.name == 'nt' else 'clear' )
    print("\n") * 30

def end_of_Game_Dog():
    print("Der Hund erreicht dich und zerfleischt dich")
    print("Tja das war wohl nix mit deinen Karten.... Jetzt bist du tot")
    print ("-") * 100
    print ("Du hast das Spiel leider verloren. Versuch es nocheinmal.\nDas Spiel wurde Programmiert von Robin Gysin")
    print ("-") * 100
    raw_input("Alles gelesen?")
    quit()

def end_of_Game_Alarmanlage():
    print ("Oh Nein, Die Alarmanlage ging an!\nJetzt aber schnell weg bevor die Polizei kommt.")
    print ("-") * 100
    print ("Du hast das Spiel leider verloren. Versuch es nocheinmal.\nDas Spiel wurde Programmiert von Robin Gysin")
    print ("-") * 100
    raw_input ( "Alles gelesen?" )
    quit()

def get_all_available_items(item_list):
    print ("-") * 100
    print ("Du hast folgende Gegenstaende: ")
    print ("-") * 100
    for item in item_list:
        if item_list[item] == 1:
            if item == "Alarmanlage" or item == "Hund" or item == "Garage":
                idle = 0
            else:
                print item
        else:
            idle = 0
    print ("-") * 100
    return

def check_user_input(word_list):

    print ("-") * 100
    print ("Wohin willst du gehen? ")
    print ("-") * 100
    for word in word_list:
        print word
    print "Items"
    print ("-") * 100
    while True:
        i = 0
        user_input = raw_input("Bitte gebe deine Richtung ein: ")
        if user_input == "Items" or user_input == "items":
            get_all_available_items(item_list)
            check_user_input(word_list)
        else:
            for word in word_list:
                if word_list[i] == user_input:
                    return user_input
                else:
                    idle = 0
                    i += 1
        print("Das ist keine gueltige Eingabe")

def welcome_text():
    print ("-") * 100
    print ("Get your Cards together")
    print ("-") * 100
    print ("Kevin hat dir deine Pokemonkarten geklaut. Er hat sie in seinem Zimmer versteckt.\nGeh und hol sie dir zurueck. Schliesslich sind es ja deine!")
    print ("-") * 100
    return 1

def house_from_street(item_list):
    print("Du stehst for Kevin's Haus.\nAlle Lichter sind aus. Es scheint als waere niemand zuhause.")
    word_list= ["Tuer", "Haus Links", "Haus Rechts"]
    user_input = check_user_input(word_list)
    if user_input == "Tuer":
        if item_list["Alarmanlage"] == 1:
            if item_list["Brechstange"] == 1:
                print("Du gehst zur Tuer und oeffnest sie! Die Alarmanlage ist schliesslich aus...")
                print("-") * 100
                room_list = 11
                return room_list
            else:
                print("Du gehst zur Tuer. Doch du kannst sie nicht aufhebeln.")
                room_number = 1
                return room_number
        elif item_list["Alarmanlage"] == 0:
            print ("Die Tuer ist verschlossen. Willst du sie aufbrechen?")
            print ("-") * 100
            while True:
                user_input = raw_input("(Y = Ja / N = Nein):  ")
                if user_input == "Y" or user_input == "y" or user_input == "Yes" or user_input == "yes" or user_input == "Ja" or user_input == "ja":
                    end_of_Game_Alarmanlage()
                elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no" or user_input == "Nein" or user_input == "nein":
                    print (" Du gehst wieder zurueck auf die Strasse und schaust dich um.")
                    print ("-") * 100
                    room_number = 1
                    return room_number
                else:
                    print ("-") * 100
                    print("Das ist keine Option")
                    print ("-") * 100
    elif user_input == "Haus Links":
        print("Du gehts Links um das Haus herum.")
        print ("-") * 100
        room_number = 2
        return room_number
    elif user_input == "Haus Rechts":
        print("Du gehts Rechts um das Haus herum.")
        print ("-") * 100
        room_number = 3
        return room_number
    else:
        quit()

def house_from_left(item_list):
    print("Du siehst einen grossen Baum neben dem Haus.\nDas Haus hat ein grosses Fenster das in die Kueche fuehrt.\nHinter dem Haus hat es noch einen Garten.")
    word_list = ["Baum","Fenster","Garten", "Haus Eingang"]
    user_input = check_user_input(word_list)
    if user_input == "Haus Eingang":
        room_number = 1
        return room_number
    elif user_input == "Baum":
        print("Du siehst eine Leiter, willst du sie erklimmen?")
        print ("-") * 100
        while True:
            user_input = raw_input ( "(Y = Ja / N = Nein):  " )
            if user_input == "Y" or user_input == "y" or user_input == "Yes" or user_input == "yes" or user_input == "Ja" or user_input == "ja":
                print("Du kletterst hinauf und betritts das Baumhaus von Kevin.\nEs liegen Murmel auf den Boden.\nDu sammelst sie ein und steckt sie in deinen Rucksack.\nSie koennten ja noch nuetzlich werden!")
                item_list["Murmeln"] = 1
                print("Du kletterst wieder hinab...")
                print ("-") * 100
                room_number = 2
                return room_number
            elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no" or user_input == "Nein" or user_input == "nein":
                print (" Du gehst wieder weg vom Baum.")
                print ("-") * 100
                room_number = 2
                return room_number
            else:
                print ("-") * 100
                print("Das ist keine Option")
                print ("-") * 100
    elif user_input == "Fenster":
        if item_list["Brechstange"] == 1:
            print("Du brichst das Fenster auf!\nUnd kletterst in die Kueche hinein.")
            print("-") * 100
            room_number = 12
            return room_number
        else:
            print("Du probierst das Fenster zu oeffnen. Es ist fest verschlossen\nHaettest du doch etwas um es aufzuhebeln.")
            print("-") * 100
            room_number = 2
            return room_number
    elif user_input == "Garten":
        print ("Du gehst ums Haus herum und betritts den Garten")
        room_number = 4
        return room_number

def house_from_right(item_list):
    print("Du siehst an der Hauswand einen kleinen Kasten.\nEbenfalls siehst du das hinter dem Haus noch ein Garten ist.")
    word_list=["Kasten", "Garten", "Haus Eingang"]
    user_input = check_user_input(word_list)
    if user_input == "Kasten":
        print("Du gehst zum Kasten hin.\nDu siehst das der Kasten mit einem Zahlenschloss abgeschlossen ist.\nWillst du probieren das Schloss knacken?")
        while True:
            user_input = raw_input ( "(Y = Ja / N = Nein):  " )
            if user_input == "Y" or user_input == "y" or user_input == "Yes" or user_input == "yes" or user_input == "Ja" or user_input == "ja":
                Alarmanlage_unlock = alarmanlage_knacken()
                print("Du oeffnest den Kasten und nimmst die Sicherung fuer die Alarmanlage heraus.")
                item_list["Alarmanlage"] = 1
                room_number = 3
                return room_number
            elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no" or user_input == "Nein" or user_input == "nein":
                print (" Du gehst wieder zurueck.")
                print ("-") * 100
                room_number = 3
                return room_number
            else:
                print ("-") * 100
                print("Das ist keine Option")
                print ("-") * 100
    elif user_input == "Garten":
        print("Du gehst in den Garten")
        room_number = 4
        return room_number
    elif user_input == "Haus Eingang":
        room_number = 1
        return room_number

def alarmanlage_knacken():
    print('---------------------------------------------------------------------------------')
    print('Das Schloss braucht nur eine Zahl. Du hast aber nur 3 Versuche')
    print('Das Schloss geht von 0 - 9')
    print('---------------------------------------------------------------------------------')
    locked_kasten = randint(0, 9)
    i = 0
    while i < 3:
        unlocking_guess = int(raw_input("Deine Nummer zwischen 0 - 9: "))
        if unlocking_guess <= 9 and unlocking_guess >= 0:
            if unlocking_guess == locked_kasten:
                print("'Klick' das schloss geht auf")
                return 1
            elif unlocking_guess > locked_kasten:
                print("Deine Nummer ist zu gross")
                i += 1
            elif unlocking_guess < locked_kasten:
                print("Deine Nummer ist zu klein")
                i += 1
        else:
             print("Unallowed Number, please give me only Numbers between 1 and 10...")
    end_of_Game_Alarmanlage()

def garden(item_list):
    print("Du stehst im Garten und schaust dich um.\nDu siehst den Schopf von Kevin, Einen Swimmingpool und eine Hundehuette.")
    word_list = ["Schopf", "Swimmingpool", "Hundehuette", "Haus Links", "Haus Rechts"]
    print("-") * 100
    user_input = check_user_input(word_list)
    if user_input == "Schopf":
        print("Du gehst in den Schopf hinein...")
        if item_list["Taschenlampe"] == 0:
            print("Aber es ist zu dunkel... Du siehst deine eigenen Haende vor Augen nicht.\nDu gehst wieder hinaus")
            print("-") * 100
            room_number = 4
            return room_number
        elif item_list["Taschenlampe"] == 1:
            print("Aber es ist zu dunkel... Aber du hast ja eine Taschenlampe.\nDu schaltest die Taschenlampe ein und siehst dich um.\nDu findest eine Brechstange")
            item_list["Brechstange"] = 1
            print("Du gehst wieder aus dem Schopf hinaus.")
            print("-") * 100
            room_number = 4
            return room_number
    elif user_input == "Swimmingpool":
        print("Jetzt ist definitiv nicht der richtige Zeitpunkt fuer ein Bad")
        print ("-") * 100
        room_number = 4
        return room_number
    elif user_input == "Hundehuette":
        print("Du gehst zur Hundehuette.\nDavor liegt eine Taschenlampe... Die koennte nuetzlich werden..\nDu steckst die Taschenlampe in deinen  Rucksack.")
        item_list["Taschenlampe"] = 1
        print("-") * 100
        room_number = 4
        return room_number
    elif user_input == "Haus Links":
        print("Du gehst um das Haus auf die linke Seite.")
        room_number = 2
        return room_number
    elif user_input == "Haus Rechts":
        print("Du gehst um das Haus auf die rechte Seite.")
        room_number = 3
        return room_number

def entry_with_stairs(item_list):
    print("Du kommst hinein und siehst eine lange Treppe mit Teppich.\nDas Haus ist schoen gestaltet mit vielen Bildern.\nDu siehst ein bild von Kevin... MIT DEINEN POKEMON KARTEN!!!!\nWas fuer eine Frechheit..")
    print("-") * 100
    print ("Du siehst einen Schrank, den Eingang zur Kueche, die Treppe nach oben, den Eingang zum Wohnzimmer und eine Geschlossene Tuer")
    word_list = ["Schrank", "Kueche", "Wohnzimmer", "Tuer", "Treppe", "Aussen"]
    user_input = check_user_input(word_list)
    if user_input == "Schrank":
        if item_list["Hund"] == 1:
            end_of_Game_Dog ()
        print("Du oeffnest den Schrank und siehst: Nunja, Spielzeutg seiner Eltern...\nnennen wir es mal so...")
        print("Du schliesst den Schrank wieder... Langsam und schockiert")
        print("-") * 100
        room_number = 11
        return room_number
    if user_input == "Kueche":
        if item_list["Hund"] == 1:
            end_of_Game_Dog ()
        print("Du trottelst richtung Kueche, Du stolperst ueber den Teppich und landest auf allen Vieren.\nDu stehst auf und reibst dir die Ellbogen.")
        print("Die Kueche ist aber nur noch ein Schritt entfernt")
        print("-") * 100
        room_number = 12
        return room_number
    if user_input == "Wohnzimmer":
        if item_list["Hund"] == 1:
            end_of_Game_Dog ()
        print("Du gehst richtig Wohnzimmer")
        print("-") * 100
        room_number = 13
        return room_number
    if user_input == "Tuer":
        if item_list["Hund"] == 1:
            end_of_Game_Dog ()
        print("Du gehst richtung Tuer, langsam streckst du deinen Arm aus.. Deine Hand zittert..\nDie Tuerklinke ist zum greifen nah... Du drueckst die Tuerklinke runter..\n und betritts den Raum")
        print("-") * 100
        room_number = 15
        return room_number
    if user_input == "Treppe":
        if item_list["Hund"] == 1 and item_list["Murmeln"] == 1:
            print("Du rennst die Treppe nach Oben,")
            print("Das waere doch ein guter Augenblick deine Murmeln auszuwerfen")
            print("Du hoerst den Hund ausrutschen auf den Murmeln. Ein Jaulen erklingt von unten")
            print("Das sollte den Hund erstmal ausser gefecht setzten...")
            item_list["Hund"] = 2
            room_number = 21
            return room_number
        elif item_list["Hund"] == 1 and item_list["Murmeln"] == 0:
            print("Du rennst die Treppe nach Oben,")
            end_of_Game_Dog ()
        else:
            print("Du gehst die Treppe nach Oben,")
            room_number = 21
            return room_number
    if user_input == "Aussen":
        print("Du gehst wieder nach draussen..")
        room_number = 1
        return room_number

def kitchen(item_list):
    print("-") * 100
    print("Du betritts die Kueche und machst das Licht an. Es ist eine sehr schoene Kueche..")
    print("Du siehst den Kuehlschrank, Ofen, Den Durchgang ins Esszimmer, Und den Eingang(innen)")
    word_list = ["Kuehlschrank", "Ofen", "Esszimmer", "Eingang"]
    user_input = check_user_input(word_list)
    if user_input == "Kuehlschrank":
        print("Du oeffnest den Kuehlschrank und siehst ein feines Joghurt.")
        print("Ein Joghurt goennst du dir. Du rastest fuer 3 Minuten")
        time.sleep(180)
        room_number = 12
        return room_number
    elif user_input == "Ofen":
        print("Du vernimmst einen Duft der aus dem Ofen zu kommen scheint...\nDer Ofen ist vor dir und du oeffnest die Tuer")
        print("Ein leckerer Kuchen ist darin... Moechtest du ein Stueck nehmen?")
        while True:
            user_input = raw_input ( "(Y = Ja / N = Nein):  " )
            if user_input == "Y" or user_input == "y" or user_input == "Yes" or user_input == "yes" or user_input == "Ja" or user_input == "ja":
                print("Du greifst in den Ofen")
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAH, Der Kuchen ist immer noch heiss.\nDu hast dir die Haende verbrannt. Na Toll...\nDas macht die suche nicht umbedingt einfacher...")
                room_number = 12
                return room_number
            elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no" or user_input == "Nein" or user_input == "nein":
                print (" Du gehst wieder zurueck.")
                print ("-") * 100
                room_number = 12
                return room_number
            else:
                print ("-") * 100
                print("Das ist keine Option")
                print ("-") * 100
    elif user_input == "Esszimmer":
        print("Du gehst richtig Esszimmer")
        room_number = 14
        return room_number
    elif user_input == "Eingang":
        print("Du gehst wieder zum Eingang des Hauses")
        room_number = 11
        return room_number

def living_room(item_list):
    print("Du gehst in das Wohnzimmer, Es ist klein. Doch mti der PS4 mit der Kevin immer angibt hast du nicht gesehen")
    print("Dafuer siehst du einen kleinen Fernseher, ein Sofa und den Eingang zum Esszimmer")
    word_list = ["Fernseher", "Sofa", "Esszimmer", "Eingang"]
    user_input = check_user_input(word_list)
    if user_input == "Fernseher":
        print("Du gehst zum Fernseher und schaltest in ein")
        fernseh_sendung = randint (1,5)
        if fernseh_sendung == 1:
            print("Es laufen die Nachrichten")
            print("-") * 100
            print("\nIndien: Wuetender Mob zuendet Baby-Elefanten an\n")
            print("-") * 100
        if fernseh_sendung == 2:
            print("Es laufen Nachrichten")
            print("-") * 100
            print("\nZivilcouragepreis gegen Rechtsradikale: AfD-Politiker hetzt gegen 15-Jaehrige\n")
            print("-") * 100
        if fernseh_sendung == 3:
            print("Es laufen Nachrichten")
            print("-") * 100
            print("\nMuenchen: Frau beißt Mann, der ihr einen Burger stehlen will\n")
            print("-") * 100
        if fernseh_sendung == 4:
            print("Es laufen Nachrichten")
            print("-") * 100
            print("\nUSA: Polizei will Kleinkriminelle mit 'Stranger Things'-Spoiler abschrecken\n")
            print("-") * 100
        if fernseh_sendung == 5:
            print("Es laufen Nachrichten")
            print("-") * 100
            print("\nRacheporno-Schutz: Facebook bittet User um deren Nacktfotos\n")
            print("-") * 100
        room_number = 13
        return room_number
    if user_input == "Sofa":
        print("Du sitzt auf das Sofa und greifst in die Spalte")
        print("Du findest 1 Franken in Muenzen, ein Dinosaurier und einen Schluessel")
        print("Du steckst den Dinosaurier und den Schluessel in deinen Rucksack")
        item_list["Key"] = 1
        item_list["Dinosaurier"] = 1
        room_number = 13
        return room_number
    if user_input == "Esszimmer":
        print("Du gehst ins Esszimmer")
        room_number = 14
        return room_number
    if user_input == "Eingang":
        print("Du gehst zurueck zum Eingang")
        room_number = 11
        return room_number

def dinning_room(item_list):
    print("Du gehst ins Esszimmer. Das Esszimmer ist nicht wirklich spannend")
    print("Du kannst in die Kueche oder ins Wohnzimmer gehen")
    word_list = ["Kueche", "Wohnzimmer"]
    user_input = check_user_input(word_list)
    if user_input == "Kueche":
        print("Du gehst in die Kueche")
        room_number = 12
        return room_number
    if user_input == "Wohnzimmer":
        print("Du gehst in das Wohnzimmer")
        room_number = 13
        return room_number

def garage(item_list):
    if item_list["Garage"] == 0:
        if item_list["Hund"] == 0:
            print("Du bist in der Garage.. Das ist ja gar nicht so grusselig...\nDu schaust dich um und siehst unmengen an Ramsch...\nDoch, da hat sich etwas bewegt...")
            print("Da ist ein Pitbull, Schnell renn weg bevor er dich zerfleischt")
            item_list["Hund"] = 1
        elif item_list["Hund"] == 2:
            print("Du bist wieder in der Garage... Mutig von dir...\nDieser Mut soll belohnt werden. Du schaust dich um und darfst eine Sache auswaehlen die du mitnehmen darfst...\nKeine Angst ich verrate Kevin nichts..")
            print("Du siehst eine Kaffeemaschine, Ein Fahrrad, Einen Eimer, Ein altes Schlagzeug, Ein Lichtschwert(Das waere Praktisch gegen den Hund gewesen..)\nEin Gummiboot, Alte Reifen, Eine Python, Eine Kaffeetasse mit Space Invaders Aufschrift.")
            word_list = ["Kaffemaschine", "Fahrrad", "Eimer", "Schlagzeug", "Lichtschwert", "Gummiboot", "Reifen", "Python", "Kaffeetasse"]
            user_input = check_user_input(word_list)
            if user_input == "Lichtschwert":
                print("Du nimmst das Lichtschwert. Die macht sei mit dir")
                item_list["Lichtschwert"] = 1
            elif user_input == "Kaffeetasse":
                print("Geh zu Martin's Platz da steht sie. Einfach einstecken wenn er nicht schaut. ;)")
                item_list["Kaffeetasse"] = 1
            elif user_input == "Gummiboot":
                print("Das sieht aus als koennte man damit Schiffe versenken spielen... aber wo? Der Swimmingpool scheint geeignet dafuer")
                item_list["Gummiboot"] = 1
            elif user_input == "Python":
                print("Na klar nimmt der Spieler eine gefaehrliche Schlange.. Ob das eine gute Idee ist?\n Du steckst die Schlange in deinen Rucksack")
            else:
                print("Spannende Auswahl... Und wie willst du das mitnehmen?")
                print("Du laesst das besser in der Garage")
            print("Du gehst wieder zurueck zum Eingang. Du schliesst die Tuer und hinter dir")
            print("Hinter dir fallen Kartonschachteln vor die Tuer sie laesst sich nicht mehr oeffnen")
            item_list["Garage"] = 1
            room_number = 11
            return room_number
    else:
        print("Die Tuer laesst sich trotzdem nicht oeffnen...")
        room_number = 11
        return room_number



    room_number = 11
    return room_number

def hall(item_list):
    print("Du bist in einem langem Flur, Es ist ziemlich Duester. An den Waenden sind Bilder aufgehaengt. Geschmacklose Kunst...")
    print("Es sind vier Tueren zu sehen und an der Decke eine Lucke")
    word_list = ["Kinderzimmer", "Buero", "Bad", "Elternzimmer", "Lucke", "Treppe"]
    user_input = check_user_input(word_list)
    if user_input == "Kinderzimmer":
        print("Du gehst zu Kevins Zimmer... Doch der Sack hat abgeschlossen")
        room_number = 21
        return room_number
    if user_input == "Buero":
        print("Du gehst richtung Buero und tritts ein")
        room_number = 23
        return room_number
    if user_input == "Bad":
        print("Du gehst richtung Bad")
        room_number = 24
        return room_number
    if user_input == "Elternzimmer":
        print("Du gehst in das Schlafzimmer der Eltern")
        room_number = 25
        return room_number
    if user_input == "Treppe":
        print("Du gehst wieder hinunter")
        room_number = 11
        return room_number
    if user_input == "Lucke":
        print("Du gehst zur Lucke und probierst sie zu oeffnen. Doch du kommst nicht an den Griff ran...\n haettest du doch nur etwas um den Griff zu erreichen..")
        print("Hast du etwas?")
        while True:
            get_all_available_items(item_list)
            user_input = raw_input("Dein Item:")
            if user_input == "Seil":
                print("Du wirfst das Seil an den Griff... Es faehlt wieder hinunter...\n")
                time.sleep(5)
                print("Du wirfst das Seil an den Griff... Es faehlt wieder hinunter...\n")
                time.sleep ( 5 )
                print("Du wirfst das Seil an den Griff... Es faehlt wieder hinunter...\n")
                time.sleep ( 5 )
                print("Du wirfst das Seil an den Griff... Es faehlt wieder hinunter...\n")
                time.sleep ( 5 )
                print("Du wirfst das Seil an den Griff... Es faehlt durch den Griff und du ziehst daran")
                print("Eine Leiter donnert dir voll auf den Fuss... Toll gemacht... *Applaus*")
                room_number = 31
                return room_number
            else:
                print("Und was willst du damit machen? Nein Nein Nein, das ist das falsche Item")
                break
        room_number = 21
        return room_number

def child_bedroom(item_list): ## TO DO FINAL ROOM
    print("Du bist in Kevins Zimmer!\nDoch deine Karten sind nirgens.\nDu schreibst Kevin eine SMS das er dir, deine Karten zurueck geben soll.\nKevin antwortet mit Okey und er verspricht sie dir am naechsten tag zu bringen.\n du gehst wieder nach Hause")
    print("-") * 100
    print("Das Spiel ist zu ende! Doch hast du alles gefunden? ;)\nDas Spiel wurde als uebung entwickelt. Bugs sind eigentlich features")
    print("-") * 100

def office(item_list):
    print("Du bist im Buero und schaust dich um... Ein alter Computer... Es ist eine Nummer aufgeklebt '-5'\nWas das wohl zu beudeuten mag?")
    print("Du siehst eine Kaffeemaschine und den alten Computer")
    word_list = ["Computer", "Kaffeemaschine", "Zurueck"]
    user_input = check_user_input(word_list)
    if user_input == "Kaffeemaschine":
        print("Du laesst dir einen Kaffee raus... Der hilft beim denken")
        print("         {\n      {   }\n       }_{ __{\n    .-{   }   }-.\n   (   }     {   )\n   |`-.._____..-'\n   |             ;--.\n   |            (__  \ \n   |             | )  )\n   |             |/  /\n   |             /  / \n   |            (  /\n   \             y'\n    `-.._____..-'")
        room_number = 23
        return room_number
    if user_input == "Computer":
        computer_hacking()
        room_number = 23
        return room_number
    if user_input == "Zurueck":
        print("Du gehst wieder in den Flur")
        room_number = 21
        return room_number

def computer_hacking():
    print("Du stellst den Computer ein 'Krrrz' Der Computer bootet")
    print("-") * 100
    while True:
        print("Bitte geben ihr Password ein.")
        print("Mit Exit kannst du den Computer verlassen")
        print("Passwort Hint: Stabilo")
        password = raw_input("[Password]: ")
        if password == "Novwdgj":
            print("Der Computer laedt und laedt und laedt")
            time.sleep(30)
            print("Ein BlueScreen erscheint...")
            break
            return
        elif password == "WdziziNojxf":
            print ("-") * 100
            print ("KaffeCode: 45862551\nKaffeecodes an GYSR")
            print("-") * 100
            break
        elif password == "KpyydibWvph":
            print ("-") * 100
            print ("KaffeCode: 75188956\nKaffeecodes an GYSR")
            print("-") * 100
            break
        elif password == "VkazgWvph":
            print ("-") * 100
            print ("KaffeCode: 75258985\nKaffeecodes an GYSR")
            print("-") * 100
            break
        elif password == "BmvodnFvaazz":
            print ("-") * 100
            print ("KaffeCode: YttJfxd\nKaffeecodes an GYSR")
            print("-") * 100
            break
        elif password == "exit" or password == "Exit":
            return
        else:
            print("Falsches Passwort")
            cls()
    return

def bath(item_list):
    print("Du bist nun im Bad\nDu siehst eine Badewanne, eine Toilette, und ein Schrank..")
    word_list = ["Badewanne", "Toilette", "Schrank", "Zurueck"]
    user_input = check_user_input(word_list)
    if user_input == "Badewanne":
        print("Jetzt ist immer noch nicht die richtige Zeit fuer ein Bad")
        if item_list["Gummiboot"] == 1:
            print("Aber fuer eine Bootsfahrt ist immer Zeit...\n\n Oder eine Runde Schiffe versenken")
            battleship()
        room_number = 24
        return room_number
    if user_input == "Toilette":
        print("Na gut kurze Toilettenpause, bis in 30 Sekunden...")
        time.sleep(30)
        print("Upps, Sorry ich dachte du bist schon fertig")
        room_number = 24
        return room_number
    if user_input == "Schrank":
        if item_list["Key"] == 1:
            print("Du oeffnest den Schrank und darin sind Medikamente...\nStell die wieder hin!!!!\nOkey ich habe nichts gesehen! Aber nicht hier nehmen!!!")
        else:
            print("Der Schrank laesst sich nicht oeffnen. Er ist verschlossen")
        room_number = 24
        return room_number
    if user_input == "Zurueck":
        print("Du gehst wieder zurueck in den Flur")
        room_number = 21
        return room_number

def battleship():
    board = []

    for x in range ( 5 ):
        board.append ( ["O"] * 5 )

    def print_board ( board ):
        for row in board:
            print " ".join ( row )

    print_board ( board )

    def random_row ( board ):
        return randint ( 0, len ( board ) - 1 )

    def random_col ( board ):
        return randint ( 0, len ( board[0] ) - 1 )

    ship_row = random_row ( board )
    ship_col = random_col ( board )

    # Everything from here on should go in your for loop!
    for turn in range ( 4 ):
        # Be sure to indent four spaces!
        guess_row = int ( raw_input ( "Guess Row: " ) )
        guess_col = int ( raw_input ( "Guess Col: " ) )
        guess_col -= 1
        guess_row -= 1

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!\nIch gebe dir ein Codewort: 'PuddingBaum' Merke es dir gut"
            return
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif (board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
            if turn > 4:
                print ("Game Over")
            else:
                print (turn + 1)
        # Print (turn + 1) here!
        print_board ( board )
    print("Du hast diese Runde verloren... Versuch es noch einmal...")

def parents_room(item_list):
    print("Du gehst in das Schlafzimmer der Eltern.")
    print("Das Zimmer ist sehr ordentlich... Es gibt nichts zu finden ausser ein Balkon")
    word_list = ["Balkon", "Zurueck"]
    user_input = check_user_input(word_list)
    if user_input == "Balkon":
        print("Du gehst richtung Balkon.. und oeffnest ihn du tritts hinaus und rauchst eine Kippe... Warte 5 Minuten")
        print("Spass, Rauchen ist ungesund... Aber geniesse ruhig deine Aussicht")
        print("Du gehst wieder in das Schlafzimmer")
        room_number = 25
        return room_number
    if user_input == "Zurueck":
        print("Du gehst wieder zurueck")
        room_number = 21
        return room_number

def dachboden(item_list):
    print("Du bist auf dem Dachboden... Aber wie willst du Jetzt in das Zimmer kommen? Eventuell ueber das Dach?\nNein schlag dir das sofort wieder aus dem Kopf!! SOFORT!!!")
    word_list = ["Dach", "Zurueck"]
    user_input = check_user_input(word_list)
    if user_input == "Dach":
        print("Du kletterst auf das Dach und probierst in das Fenster von Kevin zu kommen. Jedoch musst du die Scheibe einschlagen... Hoffentlich ist die Alarmanlage aus")
        if item_list["Alarmanlage"] == 1:
            print("Du schlaegst die Scheibe ein und kletterst in sein Zimmer")
            room_number = 22
            return room_number
        else:
            print("Nein ist sie nicht ausgeschaltet? Viel spass beim suchen...")
            room_number = 31
            return room_number
    if user_input == "Zurueck":
        print("Du gehst wieder hinunter in den Flur und schliesst die Luke wieder...\n Na toll viel Spass beim wieder aufmachen")
        room_number = 21
        return room_number

room_number = 0

while True:
    if room_number == 0:
        room_number = welcome_text ()
        raw_input("Alles gelesen?")
        cls()
    elif room_number == 1: ## Startposition
        room_number = house_from_street(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 2: ## Haus von Links
        room_number = house_from_left(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 3: ## Haus von Rechts
        room_number = house_from_right(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 4: ## Garten
        room_number = garden(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 11:
        room_number = entry_with_stairs(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 12:
        room_number = kitchen(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 13:
        room_number = living_room(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 14:
        room_number = dinning_room(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 15:
        room_number = garage(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 21:
        room_number = hall(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 22:
        room_number = child_bedroom(item_list)
        raw_input ( "Alles gelesen?" )
        break
    elif room_number == 23:
        room_number = office(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 24:
        room_number = bath(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 25:
        room_number = parents_room(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()
    elif room_number == 31:
        room_number = dachboden(item_list)
        raw_input ( "Alles gelesen?" )
        cls ()


    else:
        break
raw_input("Alles gelesen?:  ")
