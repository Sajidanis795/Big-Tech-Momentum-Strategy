# Big Tech Momentum Strategie
Dieses Repository enthält Python-Code, der eine einfache Momentum-Investitionsstrategie umsetzt, die auf Big-Tech-Aktien ausgerichtet ist. Die Strategie basiert auf der Idee des Momentum-Investierens, das den Kauf von Aktien beinhaltet, die im Preis gestiegen sind, in der Erwartung, dass der Trend anhalten wird.

# Überblick
Die Strategie betrachtet die Aktienkurse der größten Unternehmen im Nasdaq 100 Index, insbesondere:

Meta
Amazon
Apple
Microsoft
Google
Paypal
Adobe
Nvidia
Jeden Monat identifiziert die Strategie die zwei Aktien mit den höchsten Renditen im vergangenen Monat und investiert in sie. Die Renditen werden auf der Grundlage der bereinigten Schlusskurse berechnet, die von Yahoo Finance bezogen werden.

# Python-Code
Der Python-Code in diesem Repository lädt historische Daten für die ausgewählten Aktien herunter, berechnet die Renditen im vergangenen Monat, identifiziert die zwei Top-Aktien basierend auf diesen Renditen und visualisiert die Renditen in einem Balkendiagramm.

# Anforderungen
Der Code verwendet die folgenden Python-Bibliotheken:

yfinance zum Herunterladen von historischen Aktiendaten von Yahoo Finance.
pandas für Datenmanipulation und -analyse.
matplotlib für Datenvisualisierung.
# Haftungsausschluss
Dieser Code dient nur zu Informations- und Bildungszwecken. Er sollte nicht als Anlageberatung angesehen werden. Führen Sie immer Ihre eigene Recherche durch und berücksichtigen Sie Ihre finanziellen Verhältnisse, bevor Sie Anlageentscheidungen treffen.
