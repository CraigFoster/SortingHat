
from nltk import PorterStemmer
import nltk

def readScript(character):

	char_lines = ''

	with open("script1.txt") as infile:
		is_char = False
		blank_line_count = 0
		for line in infile:
			if (line.isspace()):
				blank_line_count += 1
			if (blank_line_count == 2):
				is_char = False
				
			if is_char:
				char_lines += line
		
			#print line
			if (character in line):
				is_char = True
				blank_line_count = 0
				
	#print char_lines		
	return char_lines			
				
if __name__ == "__main__":
	
	f = open('dumbledore_lines.txt', 'w')
	char_lines = readScript("DUMBLEDORE")
	f.write(char_lines)
	f.close()
	
	f = open('harry_lines.txt', 'w')
	char_lines = readScript("HARRY")
	f.write(char_lines)
	f.close()
	
	f = open('ron_lines.txt', 'w')
	char_lines = readScript("RON WEASLEY")
	f.write(char_lines)
	f.close()
	
	f = open('hermione_lines.txt', 'w')
	char_lines = readScript("HERMIONE")
	f.write(char_lines)
	f.close()
	
	f = open('hagrid_lines.txt', 'w')
	char_lines = readScript("HAGRID")
	f.write(char_lines)
	f.close()
	
	f = open('draco_lines.txt', 'w')
	char_lines = readScript("DRACO MALFOY")
	f.write(char_lines)
	f.close()
	
	#nltk files
	f = open('dumbledore_nltk.txt', 'w')
	char_lines = readScript("DUMBLEDORE")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	f = open('harry_nltk.txt', 'w')
	char_lines = readScript("HARRY")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	f = open('ron_nltk.txt', 'w')
	char_lines = readScript("RON WEASLEY")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	f = open('hermione_nltk.txt', 'w')
	char_lines = readScript("HERMIONE")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	f = open('hagrid_nltk.txt', 'w')
	char_lines = readScript("HAGRID")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	f = open('draco_nltk.txt', 'w')
	char_lines = readScript("DRACO MALFOY")
	nltk_lines = ''
	nltk_pair = nltk.pos_tag(nltk.word_tokenize(char_lines))
	for word, tag in nltk_pair:
			nltk_lines+=tag + ' '
	f.write(nltk_lines)
	f.close()
	
	
	
	