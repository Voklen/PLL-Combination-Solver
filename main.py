import json
import backend

def get_pll(data):
	input_pll = input("What pll would you like to see the result of?\n")
	
	for i in data: # Loop through all the pll's
		if i["Name"] == input_pll: # If the name of the current item maches the user input, return this item
			return i

def get_input():
	print("Welcome to my pll result program")
	print("Made by Alex Gorichev")
	
	with open("data/plls.json", "r") as file:
		data = json.load(file)
	
	first_pll = get_pll(data)
	second_pll = get_pll(data)
	return data, first_pll, second_pll

def main():
	data, first_pll, second_pll = get_input()
	resultant_pll = backend.get_resultant_pll(first_pll, second_pll, data)
	print("These PLL's would result in a", resultant_pll["Name"], "perm")

main()