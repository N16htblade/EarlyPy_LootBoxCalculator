import random
import csv

'''def csvReader (filename):
    with open (fileName, mode ="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        listName = list(csv.reader(csv_file))'''

#opening and indexing all loot files
with open ("commonLoot.csv", mode ="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    dataCommon = list(csv.reader(csv_file))

with open ("uncommonLoot.csv", mode ="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    dataUncommon = list(csv.reader(csv_file))

with open ("rareloot.csv", mode ="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    dataRare = list(csv.reader(csv_file))

#checking number of runs and defining loot dictionary
expectedRuns = int(input("Please enter number of runs: "))
numRun = 1
totalBoxes = 0

#loop that runs until all items are found
while numRun <= expectedRuns:
    totalDropsList = {}
    x = len(totalDropsList)
    i = 0
    while x < 38:
        itemPool = random.randint(1, 100)
        if itemPool <= 45:
            lootDrop = random.randint(1,12)
            lootDropItem = dataCommon[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)
        elif itemPool <= 80:
            lootDrop = random.randint(1,12)
            lootDropItem = dataUncommon[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)
        else:
            lootDrop = random.randint(1,14)
            lootDropItem = dataRare[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)
    totalBoxes += i
    #print (f"During run {numRun} it took {i} boxes to find {len(totalDropsList)} items.")
    numRun += 1

#calculating average and showing results
meanBoxes = totalBoxes / expectedRuns
meanPrice = meanBoxes * 3

print (f"Based on opening {totalBoxes} boxes, it will take an average of {int(meanBoxes)} boxes to obtain all {len(totalDropsList)} items (average price of ${int(meanPrice)}).")