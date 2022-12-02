with open('elves.txt') as f:
	lines = f.readlines()

currentCalorieCount = 0;
maxCalorieCount = 0;

for l in lines:
	if not l.strip().isdigit():
		if currentCalorieCount > maxCalorieCount:
			maxCalorieCount = currentCalorieCount
		
		currentCalorieCount = 0
	else:
		currentCalorieCount += int(l)
		
print(maxCalorieCount)