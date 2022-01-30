import backend

def to_csv_string(a_2d_array):
	out = ""
	for i in a_2d_array:
		for j in i:
			out += j + ", "
		# Remove the last two characters (, ) and instead add a newline
		out = out[:-2] + "\n" 
	return out

def main():
	print("Welcome to my pll result program")
	print("Made by Alex Gorichev")
	
	data = backend.get_plls("data/plls.json")
	
	first_column = [""]
	output_array = []
	#Loop through all pll's
	for i in data:
		# add_pll is one column of the output and will be appended to the output_array
		add_pll = [i["Name"]]
		first_column.append(i["Name"])
		for j in data:
			# Calculate result_pll
			result_pll = backend.get_resultant_pll(i, j, data)
			add_pll.append(result_pll["Name"])
		output_array.append(add_pll)
	output_array.insert(0, first_column)

	with open("data/out.csv", "w") as file:
		file.write(to_csv_string(output_array))

main()