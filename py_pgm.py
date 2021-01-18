import random

x = "y"

while x == "y":
	
	num = random.randint(1,4) 
	if num == 1:
		print("1")
	if num == 2:
		print("2")
	if num == 3:
		print("3")
	if num == 4:
		print("4")

	x = input("enter y to repeat else press n")
	print("\n")
