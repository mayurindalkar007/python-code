str1 = raw_input("Enter string\n") 
str2 = ''
dictt = {}
for char in str1:
	print(char)

	try:
		dictt[char] += 1
	except:
		str2 += char
		dictt[char] = 1

print(str2)
print(dictt)
