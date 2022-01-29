import json
import backend

def get_pll(data):
	input_pll = input("What pll would you like to see the result of?\n")
	
	for i in data: # Loop through all the pll's
		if i["Name"] == input_pll: # If the name of the current item maches the user input, return this item
			return i
	

def main():
	print("Welcome to my pll result program")
	print("Made by Alex Gorichev")
	
	with open("data/plls.json", "r") as file:
		data = json.load(file)
	
	first_pll = get_pll(data)
	second_pll = get_pll(data)

	result1 = backend.run_pll([0, 1, 2, 3, 4, 5, 6, 7, 8], first_pll["Transform"])
	result2 = backend.run_pll(result1, second_pll["Transform"])

	resultant_pll = backend.get_pll_case(result2, data)
	print("These PLL's would result in a", resultant_pll["Name"], "perm")

main()