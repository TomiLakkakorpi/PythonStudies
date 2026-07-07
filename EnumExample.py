# testaamme pythonia
 
# actually you should not use enumerate!
# use "normal for" instead with dictionary
 
# Alla olevassa esimerkissä kuvaillaan pelin vihollisten tiloja ja logiikkaa.
# käyttämällä selkoenglantia olevia muuttujanimiä ja tilojen nimiä avaimina,
# logiikka helposti luettavissa ja ymmärrettävissä.
 
# dictionaryt on sijoitettava yhteen paikkaan (tiedostoon),
# jota kaikki koodit käyttävät
# MÄÄRITÄ AINA ASIAT YHTEEN PAIKKAAN!
mygamestateenemydictionary = {
    "NotDefined": 0,
    "Sleep": 1,
    "Patrol": 2,
    "Alerted": 3,
    "Combat": 4,
    "Dead": 5,
    "Fleeing": 6,
    "Error": -1
}
 
mygameobjectenemy = {
    1: { "name": "Aarne", "status": 0 },
    2: { "name": "Bertta", "status": 0 }
}
 
 
# current Hero scene status
isHeard = False
isHeard = True
enemy = 1
isSeen = False
isSeen = True
 
# enemy AI
if isHeard == True and mygamestateenemydictionary["Dead"] != enemy:
    if isSeen == True:
        mygameobjectenemy[enemy]["status"] = mygamestateenemydictionary["Combat"]
    else:
        # mygameobjectenemy[enemy]["status"] = 2
        mygameobjectenemy[enemy]["status"] = mygamestateenemydictionary["Alerted"]
 
# display enemy status
print(mygameobjectenemy[enemy]["status"])      
 
import enum
 
class mygamestateenemyclass (enum.Enum):
    NotDefined = 0
    Sleep = 1
    Patrol = 2
    Alerted = 3
    Combat = 4
    Dead = 5
    Fleeing = 6
    Error = -1
 
print(mygamestateenemyclass.Combat.value)
print(mygamestateenemyclass.Combat.name)
 
if isHeard == True and mygamestateenemyclass.Dead.value != enemy:
    if isSeen == True:
        mygameobjectenemy[enemy]["status"] = mygamestateenemyclass.Combat.value
    else:
        # mygameobjectenemy[enemy]["status"] = 2
        mygameobjectenemy[enemy]["status"] = mygamestateenemyclass.Alerted.value
 
# display enemy status
print(mygameobjectenemy[enemy]["status"])
 
# fiksumpi ratkaisu olisi tietty yhdistää nämä funktioihin
 
def mygamestateenemy(argnimi):
    match argnimi:
        case "NotDefined":
            return 0
        case "Sleep":
            return 1
        case "Patrol":
            return 2
        case "Alerted":
            return 3
        case "Combat":
            return 4
        case "Dead":
            return 5
        case "Fleeing":
            return 6
        case _:
            # error case
            return -1
 
if isHeard == True and mygamestateenemy("Dead") != enemy:
    if isSeen == True:
        mygameobjectenemy[enemy]["status"] = mygamestateenemy("Combat")
    else:
        # mygameobjectenemy[enemy]["status"] = 2
        mygameobjectenemy[enemy]["status"] = mygamestateenemy("Alerted")
       
# display enemy status
print(mygameobjectenemy[enemy]["status"])
 
# käytetään lambdafunktioita
# tällöin nimeämiskäytäntö on tärkeää
 
mygamestateenemy_combat = lambda : 4
mygamestateenemy_alerted = lambda : 3
mygamestateenemy_dead = lambda : 5
 
if isHeard == True and mygamestateenemy_dead() != enemy:
    if isSeen == True:
        mygameobjectenemy[enemy]["status"] = mygamestateenemy_combat()
    else:
        # mygameobjectenemy[enemy]["status"] = 2
        mygameobjectenemy[enemy]["status"] = mygamestateenemy_alerted()
       
# display enemy status
print(mygameobjectenemy[enemy]["status"])
 