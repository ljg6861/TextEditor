#this is a helper file to build a tree that will assist in spell check
import pickle

def main(filename):
	with open(filename) as f:
		new_dict = {}
		new_dict[0] = ["0"]
		for line in f:
			counter = 0
			line = line.strip()
			line = line.replace('\ufeff', '')
			line = line.replace('\xed', '')
			line = line.replace('\xbb', '')
			line = line.replace('\xbf', '')
			line = line.lower()
			total = 0
			for char in line:
				number = ord(char)
				total = total + number
			for i in new_dict:
				if i == total:
					counter += 1
			if counter > 0:
				new_dict[total].append(line)
			else:
				new_dict[total] = [line]
	f.close()
	return new_dict

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def test():
	test = main("test.txt")
	save_obj(test, "test.txt")

def execute():
	diction = main("words.txt")
	save_obj(diction, "dictionary.txt")
	
def retrieve():
	dection2 = load_obj("dictionary.txt")
	print(dection2)

execute()
retrieve()