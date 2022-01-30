def run_pll(array_input, transform):
	out = [0]*9
	for (index, i) in enumerate(transform):
		out[index] = array_input[i]
	
	return out

def detect_pll(pll, data):
	for i in data:
		res = run_pll(pll, i["Transform"])
		for j in range(4):
			if res == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
				return i
			res = run_pll(res, [6, 3, 0, 7, 4, 1, 8, 5, 2]) # U move

def get_pll_case(input_pll, data): 
	for i in range(4): # Loop 4 times with a U move in between to account for all orientations
		resultant_pll = detect_pll(input_pll, data) #Get pll for this case
		if resultant_pll != None: # If there is a pll for this case, break out the function
			return resultant_pll
		input_pll = run_pll(input_pll, [6, 3, 0, 7, 4, 1, 8, 5, 2]) # U move

def get_resultant_pll(first_pll, second_pll, data):
	result1 = run_pll([0, 1, 2, 3, 4, 5, 6, 7, 8], first_pll["Transform"])
	result2 = run_pll(result1, second_pll["Transform"])

	resultant_pll = get_pll_case(result2, data)
	return resultant_pll