
def Evan():
	n = 27
	counter = 0
	number_of_one = 0
	largest = 0
	while(True):
		print(n)
		print(largest)
		if float(n) > float(largest):
			largest = n
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		counter += 1
		if n == 1:
			print("It took " + str(counter) + " times to hit number 1")
			print("Largest number: " + str(largest))
			break

Evan()

