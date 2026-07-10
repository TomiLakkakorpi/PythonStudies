#--------------------------------------------------
# Python Perusteet - Day 1 
#   1) Kommentit
#   2) Muuttujat
#   3) Tekstin printtaus
#   4) Listat
#   5) Tuplet
#   6) Sanakirjat (Dictionary)
#   7) Funktiot
#   8) Avainsana checkkaukset
#   9) Ehtolauseet
#   10) Loopit
#   11) Loogiset operaattorit
#   12) Range -funktio
#   13) Pattern matching
#   14) Joukot (sets) [PUUTTUU]
#   15) Anonyymifunktiot [PUUTTUU]
#   16) Callbackit [PUUTTUU]
#   17) Funktionaalinen ohjelmointi [PUUTTUU]
#--------------------------------------------------

#--------------------------------------------------
# 1) Kommentit
#--------------------------------------------------

# Kommentti

"""
Monirivinen kommentti
"""

print ("hello world!")

#--------------------------------------------------
# 2) Muuttujan alustus
#--------------------------------------------------

# Pythonissa muuttujan tyyppiä ei tarvitse ilmoittaa
VariableA = 123
VariableB = VariableA + 456

#--------------------------------------------------
# 3) Tekstin/muuttujan printtaus
#--------------------------------------------------

print("variable A = ", VariableA)
print("variable A = ", VariableA, "variable B = ", VariableB)

#printissä r tarkoittaa että teksti näytetään sellaisenaan ("raakana"), eikä esimerkiksi \n tulkita rivinvaihdoksi
print(r'C:\:')

#input palauttaa aina merkkijonon
variableC = input("Anna luku: ")
print("variable C = ", variableC)

#----------

# Pythonissa jos kahdella muuttujalla on sama arvo, tietoa ei tallenneta useaan kertaan vaan muuttuja viittaa samaan jo tallennettuun arvoon
# Täten muuttujan aaa ja muuttujan bbb ID:t ovat samat koska ne viittaavat samaan tallennettuun arvoon

aaa = 123
print(aaa)
print(id(aaa)) # prints out unique id of aaa
aaa = 555
print(aaa)
print(id(aaa)) # prints out unique id of aaa
bbb = 555
print(bbb)
print(id(bbb)) # prints out unique id of bbb

# kun aaa ja bbb ovat molemmat 555, ne osoittavat samaan paikkaan muistissa, joten niiden id on sama
# Eli kun bbb on 555, se ei luo uutta muuttujaa, vaan osoittaa samaan paikkaan muistissa kuin aaa.

#--------------------------------------------------
# 4) Listat
#--------------------------------------------------

myListA = [11, 22, 33, 44, 55, 66]

# Listan sisältö voi olla myös mitä vaan
myListB = [11, "Aku", 33, "Mikki", 55, "Hessu"]

# Listan sisältöä voidaan muokata
print("myListB = ", myListB)
myListB[0] = "Iines"
print("myListB = ", myListB)

#----------

# two lists are presented.
# They cannot be identical as they are stored independently in memory
# thus:
if ( [] == [] ):
    print("true 1") # true
if ( [] is [] ):
    print("true 2") # false
if ( {} == {} ):
    print("true 3") # true
if ( {} is {} ):
    print("true 4") # false

#----------

numberlist = [4,7,3,1,8]
resultlist = []

for element in numberlist:
    dummy = element * 2
    resultlist.append(dummy)

resultlist.sort(reverse=True)
resultlist.pop(0) # takes avay first, which is 8 after sorting
resultlist.pop(-1) # takes avay last, which is 2 after sorting

print("for result is ",resultlist)

#--------------------------------------------------
# 5) Tuplet
#--------------------------------------------------

# Tuplet ovat listan kaltainen tietorakenne, mutta niiden sisältöä ei voi muokata
mytupleA = ("Tupu, Hupu, Lupu")
print (mytupleA)

# Näin voi myös tehdä mutta se ei ole suositeltua
mytupleA = ("Tupu, Hupu, Lupu")
mytupleB = (*mytupleA, "Aku")
print (mytupleB)

#--------------------------------------------------
# 6) Sanakirjat (dictionary)
#--------------------------------------------------

# Sanakirja on tietorakenne joka tallentaa tietoa "avain-arvo" -pareina.
studentdict = {
    "Tupu" : 111,
    "Hupu" : 122,
    "Lupu" : 130   
}
print(studentdict)
print(studentdict["Lupu"]) # value to this key is 130

#sama asia kuin yllä printissä, mutta tässä on ensin haettu arvo muuttujaan ja sitten tulostettu se
dummy = studentdict["Lupu"]
print(dummy)

studentdict["Aku"] = 313 # you can add new key-value pair
studentdict.pop("Hupu") # you can remove key-value pairs
print(studentdict)

#--------------------------------------------------
# 7) Funktiot
#--------------------------------------------------

def func1():
    # outer function has variable
    func1variable = 111
    def func2():
        # inner function variable is defined as nonlocal
        # thus it works as global within func1 and func2
        nonlocal func1variable
        func1variable = 222
        print("func2 says ", func1variable)
    func2()
    print("func1 says ", func1variable)

func1()

#----------

def notreadyfunc():
    pass

notreadyfunc()

# pass can be set with class

class notreadyclass:
    pass

# functions can have return to return a value
def myreturnfunc(arg):
    return "\nYou said " + arg

print(myreturnfunc("Hello!!!"))

# keyword del is used to destroy a variable
# del mylistB

#--------------------------------------------------
# 8) Avainsanojen tarkistus
#--------------------------------------------------

# other keywords include:
# for, while, break, continue
for i in range(0,10,1):
    print(i, end= " ")
    if i == 8:
        break

#----------

iter = -1
while iter < 10:
    iter += 1
    if iter == 8 or iter == 7:
        continue
    else:
        print(iter, end= " ")

#----------

# Tarkistetään löytyykö annettua arvoa muuttujasta

jjj = "kukkakeppi"

if "k" in jjj:
    print("k found out!")

if "ö" in jjj:
    print("ö found out!")

if 11 in [22,44,66,11]:
    print("found out number 11 !")

#--------------------------------------------------
# 9) Ehtolauseet
#--------------------------------------------------

mynumber = int(input("\nGive a integer number  "))
if mynumber % 2 == 0:
    print("\neven number")
else:
    print("\nodd number")

#----------

mynumber = int(input("\nGive a temperature number  "))
if mynumber <= 10:
    print("\nIt is cool outside")
elif mynumber > 10 and mynumber <= 15:
    print("\nIt is warm outside")
else:
    print("\nIt is hot outside")

#--------------------------------------------------
# 10) Loopit
#--------------------------------------------------

mystring = "kukkakeppi"

for element in mystring:
    if element == 'k':
        pass
    else:
        print(element, end="")

print("")

for element in mystring:
    if element != 'k':
        print(element, end="")

#----------

# continue
# return to beginning of loop 
# and select next element
for element in mystring:
    if element == 'k' or element == 'i':
        continue
    print(element, end=" ")
else:
    print("Loop is over")
print("")

#----------

# break
# leave loop immediately
for element in mystring:
    if element == 'a':
        break
    print(element, end=" ")
else:
    # code never goes here as break
    # makes code leave loop immediately!
    print("Loop is over")
print("")

#--------------------------------------------------
# 11) Loogiset operaattorit
#--------------------------------------------------

hhh = iii = 25

if hhh == 25 and iii == 25:
    print("same")

hhh = 30

if hhh == 30 or iii == 30:
    print("one of them")

hhh = 15

if not hhh == 20:
    print("something else")

if hhh != 20:
    print("something else")

#----------

# is is used to check identification
kkk = True
#kkk = 111 
if type(kkk) is bool:
    print("It is Boolean...")

if type(kkk) == bool:
    print("It is Boolean value...")

#--------------------------------------------------
# #12) Range funktio
#--------------------------------------------------

print("")
# Range -objekti vs. lista
print(range(5))                 # Tulostaa: range(0, 5)
print(list(range(5)))           # Tulostaa: [0, 1, 2, 3, 4]

# Aloituspisteen määrittäminen
print(list(range(2, 5)))        # Tulostaa: [2, 3, 4]

# Askelvälin käyttö (step)
print(list(range(2, 10, 2)))    # Tulostaa: [2, 4, 6, 8]

# Listan monistaminen kertolaskulla
print(list([0]*7))              # Tulostaa: [0, 0, 0, 0, 0, 0, 0]

#--------------------------------------------------
# 13) Pattern matching
#--------------------------------------------------

class Point:
    x: int
    y: int

def mypointevaluation(point):
    match point:
        case Point(x=1, y=2):
            print("1 and 2")
        case _:
            print("Something else?")

mypoint = Point()
mypoint.x = 1
mypoint.y = 1
mypointevaluation(mypoint)

mypoint.x = 1
mypoint.y = 2
mypointevaluation(mypoint)