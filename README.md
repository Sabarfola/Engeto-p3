# Elections scraper

Projekt 3 pro Engeto Python Akademii

---
## Popis projektu

Účelem projektu je stažení výsledků voleb z roku 2017 pro vybraný okres z [tohoto odkazu](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101) a jejich uložení do csv souboru.
Výběr oblasti probíhá pomocí odkazu ze sloupce "Výběr obce".


## Potřebné knihovny

Viz. requirements.txt


## Práce s projektem

Spuštění projektu (scraper.py) probíhá z příkazové řádky kde jsou vyžadovány dva argumenty.

*scraper.py <url odkaz v uvozovkách> <požadovaný název výstupní csv souboru>*



### Příklad argumentů pro okres Blansko:

"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201"
blansko_vysledky.csv


### Spuštění programu:

scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201" blansko_vysledky.csv


### Běh programu

STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201 <br />
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=582671&xvyber=6201 <br />
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=582689&xvyber=6201 <br />
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=582701&xvyber=6201 <br />
... <br />
UKLÁDÁM DATA DO SOUBORU: blansko_vysledky.csv <br />


### První řádky výstupu:

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě
581291,Adamov,3 668,2 157,2 138,208,3,5,222,0,76,241,37,18,28,1,7,208,5,63,565,5,14,117,2,10,3,6,278,15,1
581313,Bedřichov,205,155,153,16,0,2,10,0,3,4,0,3,8,0,0,13,0,6,51,0,1,17,0,0,1,0,18,0,0
581330,Benešov,538,382,382,28,0,0,43,0,9,45,4,5,6,0,0,24,0,11,92,0,0,74,0,2,0,1,36,2,0
581283,Blansko,16 486,10 446,10 367,1 251,5,4,1 055,3,258,1 184,158,67,146,7,22,1 082,11,330,2 733,8,20,748,5,60,19,17,1 141,28,5
