with open('elves.txt') as f:
	lines = f.readlines()

currentCalorieCount = 0;
maxCalorieCount = 0;

for l in lines:
	if l.strip().isdigit():
		currentCalorieCount += int(l)
	else:
		if currentCalorieCount > maxCalorieCount:
			maxCalorieCount = currentCalorieCount
		
		currentCalorieCount = 0
		
print(maxCalorieCount)
