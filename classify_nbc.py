#!/usr/bin/env python3
# encoding:utf8

from textblob.classifiers import NaiveBayesClassifier

train_data = [
    ("Verschlüsselung, die neuen Trends","pos"),
    ("Spionagesoftware: Hacking Team nutzt UEFI-Rootkit", "pos"),
    ("Systemverschlüsselung: Yubikeys unter Linux nutzen", "pos"),
    ("Aktuelles zu PGP Verschlüsselung", "pos"),
    ("Festplatten-Verschlüsselung leicht gemacht", "pos"),
    ("Frische Kuchen mit Früchten", "neg"),
    ("Neueste Trends beim Backen", "neg"),
    ("Backen als Hobby entdeckt", "neg"),
    ("Kochen zur Entspannung", "neg"),
    ]

test_data = [
    ("Verschlüsselung für Anfänger"),
    ("Entwicklung neuer Verschlüsselungs-Algorithmen"),
    ("Linux-Community unterstützt Yubikey-Entwicklung"),
    ("Die neuesten Kuchen des Sommers"),
    ("Backen für jedermann"),
    ("Kochen mit Begeisterung"),
    ("Die besten Nudel-Rezepte"),
    ]

nbc = NaiveBayesClassifier(train_data)

for data in test_data:
    print(nbc.classify(data))




