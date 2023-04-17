# Iskanje polisemnih lem po korpusu

V tem branchu se nahajajo programi za lažje iskanje lem po celotnem korpusu ccKres. Programa olajšata ročno dodeljevanje pomenov izbranim besedam.

## Uvod
Za ekstrakcijo najbolj polisemnih lem v slovenskem jeziku smo uporabili [anotiran korpus ELEXIS-WSD 1.0](https://www.clarin.si/repository/xmlui/handle/11356/1674) in jih v predhodnih korakih izluščili s pomočjo programa za polisemne leme (polisemne.py). S tem programom smo dobili seznam polisemnih besed v formatu TXT, ki ga v tem koraku s programom zmanjsaj-inventar-polisemnih-besed.py zmanjšamo glede na predhodno dodeljene besede (30 na osebo, gl. [Google razpredelnico](https://docs.google.com/spreadsheets/d/1F0hoprEzzbHYJFxI0k7_1c-4_GlL_qnSmPxCgn-yDYk/edit). Ta korak posamezni osebi omogoča lažjo navigacijo po inventarju polisemnih besed, kar bo uporabno v fazi določanja posameznega pomena leme v neki povedi. 

## Predhodne zahteve
Za uporabo programov potrebujemo:
- seznam polisemnih lem v formatu TSV (gl. zgoraj)
- besede, ki so nam bile dodeljene (30 besed), shranjene v datoteko TXT
- že lematiziran korpus [cckresV1_0.zip](https://www.clarin.si/repository/xmlui/handle/11356/1034) (več manjših datotek v formatu XML)
- nastavimo pot: nlp-course-digiling\iskanje-lem\polisemne-leme-in-stavki\ccKres_LEMATIZIRAN (ob uporabi programov pot ustrezno prilagodite)


## Uvozimo potrebne knjižnice
Če knjižnic še nimamo v Pythonu, jih inštaliramo z naslednjim ukazom z uporabo [pip](https://pip.pypa.io/en/stable/):
```bash
pip install [ime knjižnice]
```
Ko imamo knjižnice nameščene, jih uvozimo:
```
import xml.etree.ElementTree as ET
import os
import csv
```

## Uporaba programov
Znotraj tega brancha sta ustvarjena dva programa. Prvi zmanjša inventar polisemnih lem, drugi pa najde povedi, v katerih se nahajajo polisemne leme.

### zmanjsaj-inventar-polisemnih-besed.py
1. odpremo inventar polisemnih besed (datoteka TSV)
2. odpremo svoje polisemne besede (datoteka TXT)
3. program skrajša celoten seznam in ustvari izhodno datoteko z zmanjšanih inventarjem polisemnih lem (datoteka TSV)

### xml-leme-vse-nives.py
1. uvozimo knjižnice: xml.etree.ElementTree, os in csv
2. odpremo svoje polisemne besede (datoteka TXT)
3. ustvarimo prazen seznam stavki_s_polisemi
4. nastavimo izhodno datoteko, kamor se bodo zapisovale povedi, kjer se nahajajo polisemne besede, in leme (datoteka CSV), ter vanjo zapišemo imena stolpcev (Stavek, Polisemna lema)
5. nastavimo vhodni direktorij, v katerem so datoteke XML za obdelavo (celoten lematiziran korpus ccKres)
6. uporabimo knjižnico ElementTree za datoteke XML
7. za vsako XML datoteko v vhodnem direktoriju poiščemo vsak odstavek in stavke znotraj odstavka
8. preverimo vsako besedo v stavku in preverimo, ali ima beseda polisemno lemo
9. če je v stavku polisemna lema, program doda stavek v seznam stavki_s_polisemi
10. zapišemo stavek in polisemne leme v izhodno CSV datoteko
11. po obdelavi vseh XML datotek se izpiše število stavkov, ki vsebujejo poliseme
12. izpišejo se vsi stavki, ki vsebujejo poliseme, skupaj s podatki o njihovem odstavku in povedi

## Opomba
Programa sta v vmesni, delovni fazi in nista še končna.


## Licenca

[CC](https://creativecommons.org/licenses/by-nc/4.0/)
