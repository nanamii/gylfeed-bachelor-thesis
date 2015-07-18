#!/usr/bin/env python3
# encoding:utf8

from textblob.classifiers import NaiveBayesClassifier

train_data = [
    ("Spionageabwehr: Regierungsmitglieder nutzen immer öfter Einweg-Handys","pos"),
    ("Xbox One: Spielestreaming für alle Besitzer von Windows 10", "neg"),
    ("iPod: Neue Shuffle und Nano unterstützen Apple Music nicht", "neg"),
    ("Homejoy.com: US-Pionier der Putzhilfenvermittlung im Netz gibt auf", "pos"),
    ("Internetnutzung verschleiern: Proxyham angeschaut und nachgebaut", "pos"),
    ("Grafikchips und Prozessoren: 2016 wird die Halbleiter-Branche endlich wieder spannend!", "pos"),
    ("DAB+: Radiosender warnt vor schneller UKW-Abschaltung", "neg"),
    ("Valve Software: Steam bietet Zwei-Faktor-Authentifizierung per Smartphone", "pos"),
    ("Circuit-Switch-Call: Vodafone startet Call+-Zusatzfunktionen für Anrufe", "neg"),
    ("Ex-Monopolist: British Telecom droht die Spaltung", "neg"),
    ("Hacking Team: Eine Spionagesoftware außer Kontrolle", "pos"),
    ("Verschlüsselung: Der lange Abschied von RC4", "pos"),
    ("Plastic Road: Niederländer wollen Straßen aus Plastikmüll bauen", "neg"),
    ("Embedded SIM-Karte: Samsung und Apple wollen eSIM", "neg"),
    ("London: Marshall stellt eigenes Smartphone vor", "neg"),
    ("Prozessor: Intel dehnt Moore's Law und verschiebt Cannonlake", "neg"),
    ("Smartphone: Fairphone 2 kann vorbestellt werden", "neg"),
    ("Two-Smartphone: Oneplus verspricht vereinfachtes Einladungssystem", "neg"),
    ("Deutsche Bahn: Pofalla soll Vorstand für Datenschutz werden", "pos"),
    ("Analogabschaltung: Netzausbau bringt Sendepause bei Kabelnetzbetreiber","neg"),
    ("The Flock: Server-Aus nach Spielertoden", "pos"),
    ("Stimmen des Untergangs: Der Prolog von Starcraft 2 ist eröffnet", "pos"),
    ("Gearbox Software: Duke Nukem soll wieder antreten", "pos"),
    ("Counter-Strike: E-Sportler berichtet über Doping mit Psychopharmaka", "pos"),
    #("Mortal Kombat X: Prügelspiel erhält verspätet Ab-18-Freigabe", "pos"),
    #("Deep Silver: Zusammenarbeit mit Yager bei Dead Island 2 beendet", "pos"),
    ("Spieleentwickler: Star Citizen schließt Kritiker aus Unterstützerkreis aus", "pos")
    ]

test_data = [
    ("Fluggastdatenspeicherung: EU-Parlament votiert für PNR-Datenbank"),
    ("Chipmaschinen-Hersteller: ASML liefert sechs EUV-Belichtungsmaschinen an Intel aus"),
    ("Apple: iCloud löscht unter Umständen Daten unwiederbringlich"),
    ("Spionagesoftware: Hacking Team nutzt UEFI-Rootkit"),
    ("Mobilfunk: 5G soll für Nutzer wie ein unbegrenztes System sein"),
    ("Mobilfunknetzbetreiber: Kostenloses WLAN für Regionalzüge kommt"),
    ("Kickstarter: Kerze lädt Smartphone"),
    ("Hacking Team: Carabinieri kapern mal kurz das Internet"),
    ("Nach Hackerangriff: OPM-Chefin Katherine Archuleta tritt zurück"),
    ("Smartphone-Hersteller: Geeksphone hört auf"),
    ("Systemverschlüsselung: Yubikeys Zwei-Faktor-Authentifizierung unter Linux nutzen"),
    ("Kritik an Dieter Nuhr: Wir alle sind der Shitstorm"),
    ("Navigationsgerät: Autofahrer verursacht wegen Navi schweren Unfall"),
    ("Until Dawn angespielt: Das Horrorhaus der tödlichen Entscheidungen"),
    ("Satoru Iwata: Nintendo-Chef im Alter von 55 Jahren gestorben"),
    ("Call of Duty: Zombies à la Film noir")

    ]

nbc = NaiveBayesClassifier(train_data, lang='de_DE')

for data in test_data:
    print(nbc.classify(data))

print(nbc.accuracy(train_data))
print(nbc.show_informative_features(5))



