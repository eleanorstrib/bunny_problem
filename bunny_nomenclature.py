"""
Name that rabbit
================
"You forgot to give Professor Boolean's favorite rabbit specimen a name? You 
know how picky the professor is! Only particular names will do! Fix this 
immediately, before you're... eliminated!"
Luckily, your minion friend has already come up with a list of possible names, 
and we all know that the professor has always had a thing for names with lots of 
letters near the 'tail end' of the alphabet, so to speak. You realize that if 
you assign the value 1 to the letter A, 2 to B, and so on up to 26 for Z, and 
add up the values for all of the letters, the names with the highest total 
values will be the professor's favorites. For example, the name Annie has 
value 1 + 14 + 14 + 9 + 5 = 43, while the name Earz, though shorter, has value 
5 + 1 + 18 + 26 = 50. 
If two names have the same value, Professor Boolean prefers the 
lexicographically larger name. For example, if the names were AL (value 13) and 
CJ (value 13), he prefers CJ.
Write a function answer(names) which takes a list of names and returns the list 
sorted in descending order of how much the professor likes them.
There will be at least 1 and no more than 1000 names. 
Each name will consist only of lower case letters. The length of each name will 
be at least 1 and no more than 8.
Test cases
==========
Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]
Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]
>>> answer(["annie", "bonnie", "liz"])
['bonnie', 'liz', 'annie']
>>> answer(["abcdefg", "vi"])
['vi', 'abcdefg']
>>> answer(["AL", "CJ"])
['CJ', 'AL']
"""
def answer(names):
	alphabet = {
		'a': 1,
		'b': 2,
		'c': 3,
		'd': 4,
		'e': 5,
		'f': 6,
		'g': 7,
		'h': 8,
		'i': 9,
		'j': 10,
		'k': 11,
		'l': 12,
		'm': 13,
		'n': 14,
		'o': 15,
		'p': 16,
		'q':17,
		'r':18,
		's':19,
		't':20,
		'u':21,
		'v':22,
		'w':23,
		'x':24,
		'y':25,
		'z':26
	}

	# create a dict to put the names in in order of value
	# keys will be scores, values will be a list of names

	name_list = []
	
	#loop through names in original list
	for name in names:
		name = name.lower()
		sum_this_name = 0
		#loop through letters of each name
		for letter in name:
			sum_this_name = sum_this_name + alphabet[letter]
		name_list.append((sum_this_name, name))
 
	
	name_list.sort(reverse=True)
	
	return_this=[]

	for item in name_list:
		return_this.append(item[1])

	print return_this
	return return_this

answer(["abcdefg", "vi"])
