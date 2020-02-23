
# Use an import statement at the top
import random as rm

word_file = "4. words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
def generate_password():
# It should return a string consisting of three random words

    # region My Logic
    return word_list[int(len(word_list) * rm.random())] + word_list[int(len(word_list) * rm.random())] + word_list[int(len(word_list) * rm.random())]
    # endregion

    # region random.choice
    #return rm.choice(word_list) + rm.choice(word_list) + rm.choice(word_list)
    # endregion

    # region ''.join(random.choice)
    # return ''.join(random.sample(word_list,3))
    # endregion

# concatenated together without spaces



# test your function
print(generate_password())

