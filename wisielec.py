import random
words = ["tree", "orange", "lemon", "keyboard", "apple", "banana", "headphones", "computer", "ball", "basketball", "tomatoe"]
word = random.choice(words)

length = []
print word
len = len(word)

hangman_one = "   ------"
hangman_two = "   |    |"
hangman_thr  =  "        |"			  
hangman_for =  "        |"
hangman_fiv =   "        |"
hangman_grn =  "  --------"

checked_words = 0
missed_words = ""

for letters in word:
		length.append("_")


looses = 0
guessed_words = 0

def draw_hangman():
	print hangman_one
	print hangman_two 
	print hangman_thr  		  
	print hangman_for
	print hangman_fiv 
	print hangman_grn

print word
print length
misses = 0
while(misses < 6 and guessed_words < len):
	print "           "
	
	print "           "
	guess = 0
	checked_words = 0
	letter = raw_input("Type letter: ")
	while(len > checked_words):
		if(word[checked_words] == letter and length[checked_words] == "_"):
			length[checked_words] = letter
			checked_words = checked_words + 1
			guess = guess + 1
			guessed_words = guessed_words + 1
			
		else:
			checked_words = checked_words + 1
	if(guess == 0):
		misses = misses + 1
	
	if(misses == 1):
		hangman_thr = "   o    |"
	if(misses == 2):
		hangman_for =  "   |    |"
	if(misses == 3):
		hangman_for =  "  \|    |"
	if(misses == 4):
		hangman_for =  "  \|/   |"
	if(misses == 5):
		hangman_fiv =   "  /     |"
	if(misses == 6):
		hangman_fiv =   "  /\    |"
	draw_hangman()
	print length
if(misses == 6):
	print "You lost!"
else:
	print "You won!"
		
		
		
		
		
	
		