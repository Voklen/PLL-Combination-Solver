str1 = "a bunch of words with a repeated word: a"
substr = "a"

def search(string, keyword):
	result = []
	for i in range(len(string)):
		if string.startswith(keyword, i):
			result.append(i)
	return result

res = [i for i in range(len(str1)) if str1.startswith(substr, i)]
print(res)

print(search(str1, substr))