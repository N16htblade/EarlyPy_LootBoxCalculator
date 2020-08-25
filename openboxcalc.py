import random
import csv

totalDropsList = {}
x = len(totalDropsList)
i = 0

while x < 38:
    itemPool = random.randint(1, 100)
    if itemPool <= 45:
        with open ("commonLoot.csv", mode ="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            data = list(csv.reader(csv_file))
            lootDrop = random.randint(1,12)
            lootDropItem = data[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)
    elif itemPool <= 80:
        with open ("uncommonLoot.csv", mode ="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            data = list(csv.reader(csv_file))
            lootDrop = random.randint(1,12)
            lootDropItem = data[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)
    else:
        with open ("rareLoot.csv", mode ="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            data = list(csv.reader(csv_file))
            lootDrop = random.randint(1,14)
            lootDropItem = data[lootDrop][2]
            totalDropsList[f"{lootDropItem}"] = "1"
            i += 1
            x = len(totalDropsList)

print(f"It took {i} boxed to find {len(totalDropsList)} items!")
totalPrice = i*3
print(f"It will cost ${totalPrice} to unlock all items.")