import file
import random
import os

kuchenPath = os.path.join("./kuchen.txt")

kuchen = ["Erdbeerkuchen", "Pflaumenkuchen", "Obstkuchen", "Donauwelle", "Bienenstich"]

#file.saveFile(f"Hello World from save.py \n")
#file.saveFile(f"2\n")

#file.saveLinesToFile(kuchenPath, kuchen)

#print(file.readFile())

x = 0
randomNumber = []

while x < 100:
    randomNumber.append(str(random.randint(0,9999))+ f"\n")
    x += 1

numbers = os.path.join("./randomNumbers.txt")

file.saveLinesToFile(numbers, randomNumber)

readNumber = file.readLinesFromFile(numbers)

print(readNumber[45])
readNumber[45] = f"0000\n"

file.saveLinesToFile(numbers, readNumber)
