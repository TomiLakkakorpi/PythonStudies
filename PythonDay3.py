#--------------------------------------------------
# Python Perusteet - Day 3
#   1) Enumeration
#   2) Virheenhallinta (Try-Finally)
#   3) CSV -tiedoston lukeminen
#   4) Piirtäminen ja tilastot

#--------------------------------------------------

#--------------------------------------------------
# 1) Enumeration
#--------------------------------------------------

# You should not use enumerate 
# Use "normal for" instead with dictionary

import enum

mydict = {
    112: "Aarne",
    543: "Bertta",
    673: "Celsius",
    878: "Daavid"
}

for key,value in mydict.items():
    print(key,value)

myvalue = 112

if mydict[myvalue] == "Aarne":
    print("Se oli Aarne")

# parempi on tehdä yllä oleva dictionary toisinpäin
# Esimerkiksi peleissä jonkun vihollisen tila (state)
# Helpompaa on lukea myöhemmin koodista että tila on "Alert" kuin että tila on 2
mydict2 = {
    "Aarne": 112,
    "Bertta": 543,
    "Celsius": 673,
    "Daavid": 878
}

#------------------------------

mylistA = ["Aarne", "Bertta", "Celsius", "Daavid"]

# enumerate() creates key-value pairs of value iterable
# printing the tuples in object directly
for ele in enumerate(mylistA):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(mylistA, 100):
    print (count, ele)
 
# getting desired output from tuple
for count, ele in enumerate(mylistA):
    print(count)
    print(ele)

# here we do again enumeratation from iterable list
# enumerate() creates enumerated object
result = enumerate(mylistA, 1001)
print(result) # shows object address
print(next(result)) # 1001, aarne
print(next(result)) # 1002, bertta

# string can also be enumerated
result = enumerate("Hukkaputki",1001)
for i,j in result:
    print(i,j)

#--------------------------------------------------
# 2) Virheenhallinta - Try-Finally
#--------------------------------------------------

try:
    # mode is w+ because we want to create new file if necessary
    # if no file is present, file is created
    # w+ overwrites existing content
    fileobject = open("storagefile.txt","w+")

    # write 3 lines of material
    fileobject.write("Tupu\n")    
    fileobject.write("Hupu\n")    
    fileobject.write("Lupu\n")    

finally:
    fileobject.close()

try:
    # We open storagefile for reading.
    # thus r is selected as mode
    fileobject = open("storagefile.txt","r")

    # here we read it all into list
    # result = fileobject.readlines()
    # print(result)

    # here we read from fileobject line by line
    for myline in fileobject:
        print("I read: ", myline)

finally:
    fileobject.close()

#--------------------------------------------------
# 3) CSV -tiedoston lukeminen
#--------------------------------------------------

with open("testi.csv") as mycsvfile:
    inputstream = csv.reader(mycsvfile,delimiter=";")
    title = True
    for row in inputstream:
        if title:
            print(row)
            title = False
        else:
            print("{} tyäskentellöö {}".format(row[0], row[2]))

#--------------------------------------------------
# 4) Piirtäminen ja tilastot
#--------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

xData = [1,2,3,4,5]
yData = [8, 1, 5, 9, 6]
varitys = ["gray","gray","gray","gray","gray"]

xArvo = np.array(xData)
yArvo = np.array(yData)
colorList = np.array(varitys)

plt.subplot(2,3,1)
plt.bar(xArvo,yArvo,color=colorList)
plt.show()
