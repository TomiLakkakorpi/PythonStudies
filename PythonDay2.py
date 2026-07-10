#--------------------------------------------------
# Python Perusteet - Day 2
#   1) Luokat
#   2) Perintä
#   3) Polymorfismi/monimuotoisuus
#   4) Moninperintä
#   5) Abstraktit luokat
#   6) Interfacet
#   7) Encapsulation
#   8) Oliot
#   9) Ohjelmistokehityksen tason parantaminen ja kehityksen eri vaiheet
#--------------------------------------------------

#--------------------------------------------------
# 1) Luokat
#--------------------------------------------------

class Kissa:
    def __init__(self, argnimi, argikä):
        self.nimi = argnimi
        self.ikä = argikä

    def kävelee(self):
        print(f"{self.nimi} kävelee.")

    def kehrää(self):
        print(f"{self.nimi} kehrää...")

Jenny = Kissa("Jenny", 15)
Kali = Kissa("Galileo",16)

print(Jenny.nimi)
Jenny.kävelee()
Jenny.kehrää()

print(Kali.nimi)
Kali.kävelee()
Kali.kehrää()

# Jos et käytä perintää, dictionary on hyvä vaihtoehto.
# funktioita koodatessa luokka on joustavampi ja parempi
# Dictionary sopii hyvin yksinkertaisiin olioihin, mutta luokka on parempi monimutkaisissa olioissa.
TestiJenny = {"nimi": "TestiJenny", "ikä": 1, "kävelee" : lambda : print(TestiJenny["nimi"] + " kävelee."), "kehrää" : lambda : print(TestiJenny["nimi"] + " kehrää...")}
print(TestiJenny["nimi"])
TestiJenny["kävelee"]()
TestiJenny["kehrää"]()

#--------------------------------------------------
# 2) Perintä
#--------------------------------------------------

# Perintä
# Kahdesta syystä:
# 1) Agregaatti, eli luokka koostuu monista luokista
# Tällöin luokalla on monia “äitejä” ja luokkia ominaisuuksina
# 2) Pääasiallinen tapa tehdä perintä on erityistapaus
# Tällöin äitiluokka on perustapaus ja lapsiluokka on äidistä eroava erikoistapaus
# Sääntö: älä peri ilman syytä, koodi monimutkaistuu

# Lapsi perii äidin ominaisuudet ja toiminnot
# Lapsi on erityistapaus jos
# 1) lisätään uusia ominaisuuksia
# 2) lisätään uusia toimintoja
# 3) muutetaan olemassa olevia toimintoa eli “override”

class SiamilainenKissa(Kissa):
    def __init__(self, argnimi, argikä, argväri):
        super().__init__(argnimi, argikä)
        #uusi ominaisuus
        self.väri = argväri

    # uusi toiminto
    # se vaatii lapselle uuden funktion
    def maukuu(self):
        print(f"{self.nimi} maukuu.")

    # toiminnon muuttaminen eli override
    def kehrää(self):
        print(f"{self.nimi} kehrää kuin siamilaisen kissan kuuluu.")

Justiina = SiamilainenKissa("Justiina", 10, "Punainen")
Justiina.kävelee()
Justiina.kehrää()
Justiina.maukuu()

#--------------------------------------------------
# 3) Polymorfismi eli monimuotoisuus
#--------------------------------------------------

# Perintään kuuluu läheisesti ohjelmistotekniikan termi
# "polymorfismi" eli monimuotoisuus
# siinä käytetään keskenään perivien luokkien samankaltaisuutta hyväksi

kissalauma = []
kissalauma.append(Jenny)
kissalauma.append(Kali)
kissalauma.append(Justiina)

# polymorfissa kutsutaan samaa funktiota kaikille keskenään perivien luokkien olioille
# Tässä kissa ja siamilainenkissa luokille
# tekniikkaa käytetään esim puhelimien näyttöjen päivityksessä
print("Polymorfismi")
for kissa in kissalauma:
    kissa.kehrää()

#--------------------------------------------------
# 4) Moninperintä
#--------------------------------------------------


# moninperintä
print("Moninperintä")

# Moninperinnässä lapsi perii usealta äidiltä
# Python tukee moninperintää

class Koira:
    def __init__(self, argnimi, argikä):
        self.nimi = argnimi
        self.ikä = argikä

    def kävelee(self):
        print(f"{self.nimi} kävelee kuin koira.")

    def haukkuu(self):
        print(f"{self.nimi} haukkuu kuten koirat haukkuvat.")

# Moninperinnässä on kaksi äitiä: kissa ja koira
# Lapsiluokka on KissaKoira
# mikäli perinnässä on samoja ominaisuuksia tai toimintoja
# Lapsi ottaa ne ensiksi äidiltä, joka on ensimmäisenä perintälistassa
# Tämän vuoksi moninperintä EI aiheuta ongelmia.
class KissaKoira(Kissa, Koira):
    def __init__(self, argnimi, argikä):
        super().__init__(argnimi, argikä)

    # override
    #def kehrää(self):
    #    print(f"{self.nimi} kehrää kuin kissa ja haukkuu kuin koira.")

Pluto = KissaKoira("Pluto", 313)
Pluto.kävelee()
Pluto.haukkuu()

# !Huom yleensä kielissä on moninperintä kiellettyä

# Miksi moninperintää tehdään?
# perustuu ajatukseen että äitiluokasta saadaan ominaisuuksia ja toimintoja joita tarvitaan
# Käytännössä moninperinnän lapsen toteutus on kompromissi
# Monissa kielissä halutaan käyttää interfacea
# tällöin äitiluokka määrittää millaisia asioita lapselle halutaan
# mutta toteutus on lapsen oma

# äitiluokka voi sisältää:
# 1) funktioita, joita halutaan lapsessa toteuttaa
# 2) funktioita, joita lapsi voi periä
# äitiluokkaa ei voi itsessään toteuttaa.
# se on siis etukäteen sovittu joukko funktioita, joita lapsen toteutuksessa on pakko toteuttaa
# tietotekniikassa sitä kutsutaan abstract class eli abstrakti luokka tai interfaceksi kielen toteutuksesta riippuen.

#--------------------------------------------------
# 5) Abstraktit luokat
#--------------------------------------------------

# 1) abstrakti luokka:
# voi sisältää funktioita, joilla on toteutus
# voi sisältää funktioita, joilla ei ole toteutusta
# 2) interface:
# sisältää funktioita, joilla ei ole toteutusta

# kumpiakin rakenteita käytetään luomaan joukko haluttuja ja pakollisia funktioita, joita kaikki tämänkaltaiset
# ja näistä perivät luokat joutuvat jotenkin käyttämään
# tämä mahdollistaa yhdessä polymorfismin kautta samantapaisten luokkien yhteentoiminnan
# esimerkiksi kaikki graafisen elementin luovat luokat joutuvat implementoimaan draw() nimisen funktion

#--------------------------------------------------
# 6) Interfacet
#--------------------------------------------------

import abc 

# Tässä interface
class MyInterface(abc.ABC):
    #interface sisältyy funktioita, jotka implementoidaan perivässä luokassa
    @abc.abstractmethod
    def IFMethodAarne(self):
        pass

    @abc.abstractmethod
    def IFMethodBertta(self):
        pass

# tässä abstrakti luokka
class MyAbstractClass(abc.ABC):
    @abc.abstractmethod
    def ACMethodAarne(self):
        pass

    #seuraava funktio toteutetaan abstraktissa luokassa
    def ACMethodBertta(self):
        print("ACMethodBertta")

# tarvitaan luokka, joka ottaa käyttöön interfacen ja abstraktin luokan
# sen on implementoitava abstraktit methodit
class MyRealClass(MyInterface, MyAbstractClass):
    def __init__(self):
        super().__init__()

    def IFMethodAarne(self):
        print("IFMethodAarne")

    def IFMethodBertta(self):
        print("IFMethodBertta")

    def ACMethodAarne(self):
        print("ACMethodAarne")

myObject = MyRealClass()
myObject.IFMethodAarne()
myObject.IFMethodBertta()
myObject.ACMethodAarne()
myObject.ACMethodBertta()

#--------------------------------------------------
# 7) Encapsulation
#--------------------------------------------------

# encapsulation tarkoittaa, että luokan koodissa pyritään erottamaan sen ulkoinen ja sisäinen toiminta
# käytännössä osa muuttujista halutaan olevan yksityisiä (private) eli toimivan ainoastaan luokan sisällä
# Pythonin encapsulation toteutetaan _muuttuja merkillä

class Employee:
    def __init__(self, argnimi, argpalkka):
        self.nimi = argnimi
        self.palkka = argpalkka
        self.__salasana = argpalkka + 10000

    def employeeinfo(self):
        print(f"{self.nimi}, {self.palkka}, {self.__salasana}")

jussi = Employee("Jussi", 5000)
jussi.employeeinfo()

print(jussi.nimi)
print(jussi.palkka)

# print(jussi.__salasana) # tämä ei toimi, koska muuttuja on private
jussi.__salasana = 123456 ## tämä ei muuta private muuttujaa, vaan luo uuden julkisen muuttujan
# print(jussi.__salasana) # tämä tulostaa uuden julkisen muuttujan
print(jussi._Employee__salasana) # tämä tulostaa private muuttujan, mutta ei ole suositeltavaa

# !huom encapsulation ei toimi täysin
# Ei voi luottaa

#--------------------------------------------------
# 8) Oliot
#--------------------------------------------------

# Olio-ohjelmointi on tarkoitettu olioiden täyteen itsenäisyyteen
# mutta käytännössä kaikki ohjelmointikielet sisältävät myös luokkatasoisia muuttujia.

# Luokkatasoisia muuttujia käytetään kun halutaan esittää
# 1) kaikille luokan jäsenille samoja arvoja
# 2) haluat käyttää sitä sisäisenä laskurina yms.

class ToimiHenkilö:
    # tässä on luokkatasoinen muuttuja
    hetu = 0

    #tässä konstruktori, joka luo olion
    def __init__(self, argnimi):
        #tässä luodaan objektitasoinen muuttuja
        self.nimi = argnimi
        # tässä muutetaan luokkatasoista muuttujaa aina, kun luodaan uusi toimihenkilö
        ToimiHenkilö.hetu += 1
        self.hetu = ToimiHenkilö.hetu

tupu = ToimiHenkilö("Tupu")
hupu = ToimiHenkilö("Hupu")
lupu = ToimiHenkilö("Lupu")

toimihenkilölista = [tupu, hupu, lupu]

for toimihenkilö in toimihenkilölista:
    print(f"toimihenkilö: {toimihenkilö.nimi}, henkilönumero: {toimihenkilö.hetu}")

#--------------------------------------------------
# 9) Ohjelmistokehityksen tason parantaminen ja kehityksen eri vaiheet
#--------------------------------------------------

"""
1) Jokaisella koodin osalla on vastaava koodari.
Eli kaikki koodi jaettiin eri koodareille.
--> Syntyy jonkinlainen omistajuus
--> Aina, kun kysyt jostain, löytyy vastaava, joka tietää
--> koodareiden keskinäinen kyselyn teho parani heti
=>>Koodarit saavat parempaa tietoa ja neuvoja ja yhteistyö paranee!

2) Käännä koodi joka yö.
Isosssa projektissa tulee uutta koodia koko ajan.
Koodareita on helposti tusina tai kaksi suuressa projektissa.
Ongelma oli, että versionhallintaan laitettu koodi ei toimi.

Kääntö kertoi heti, mikä koodi ei toiminut.
--> Tieto koottiin kääntäjän ilmoituksista ja koodinomistajista.
Tällöin saatiin vikatilanteen syypää heti selville.
Aamulla odottaa prioriteetti ykkösenä korjaus ja vihainen pomo.
--> Koodarien hutilointi versionhallinnan käytössä väheni.
==>Useampi öinen käännös todella kääntyi loppuun asti.

3) Testaajat testaa vain kääntyvää koodia.
Testaajat tietävät jo aamulla, onko uusi versio kääntyvä.
-->Jos ei toimi, testaajat jatkaa edellisellä kääntyneellä versiolla.
-->Testaajat eivät kokeile toimimattomia versiota, joten tunteja säästyy.
==>Testaajien tehokkaat työtunnit kaksinkertaistuivat.

Seuraavat askeleet vaativat paljon testaajilta!
Käytännössä testaajien on osattava tehdä skriptejä!
Testaajien koulutus koodaamaan alkaa nyt.

4) Tee käännökselle "smoke testaus".
Käännöksen jälkeen koodi asennetaan koelaitteeseen automaattisesti.
Tämän jälkeen laite käynnistetään.
-->Jos ei toimi, testaajat eivät asenna kääntyvää versiota.
==>Säästää turhilta hälytyksiltä testauksen sisällä.

5) Tee käännökselle laajempi smoke testaus.
Voiko koodilla tehdä perusasioita? 
Esimerkiksi lisätään potilas sairaalan leikkitietokantaan.
Esimerkiksi tietoliikennetorni tekee self diagnostiikan. jne.
-->Osoittaa koodareille loogisten vikojen syntymisen.
-->Tämä menee aina aamulla tokaksi selvitettäväksi (kääntymätö on eka).
==>Säästää aikaa ja poistaa turhat bugirapskat.

6) Laajenna testaus automaattitestaukseksi.
Vaiheiden teko parantaa yökäännöksen laatua.
--> laajempi osa käännetään ja testataan yöllä.
--> Testaajilla on enemmän aikaa.
--> koodaajat pääsee tutkimaan rajapintoja.
==> lisää varmuutta rajapinnoista, refaktoroinneista...

Seuraavat askeleet vaativat firman prosessin muutoksia!
Tämä vaatii pomoportaan mukaanottoa ja läsnäoloa aidosti.

7) Testaus jakautuu tässä vaiheessa kahteen osaan.
--> yönyli automaattitestaukset etsivät bugeja.
--> oikea testaus mittaa suorituskykyä.
==> Tutkitaan jo varhaisemmassa vaiheessa nopeutta.

8) Suorituskyky vaatii pysyvää testipenkkiä.
--> testejä automatisoidaan ja suorituskykyä testataan.
--> mitä aiemmin pullon kaulat löytyy, sen helpompi ne on refaktoroida!
--> vaatii tilastointia suorituskyvyn muutoksista.
==> Testaus ja bugien määrän seuranta.
"""
