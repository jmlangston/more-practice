import pprint

pp = pprint.PrettyPrinter()

words_file = open("words-subset.txt")

all_words = words_file.read().split("\n")

words_dict = {}

for word in all_words:
    letters_list = list(word)
    letters_list.sort()
    letters = "".join(letters_list)

    if letters not in words_dict:
        words_list = []
        words_list.append(word)
        words_dict[letters] = words_list

    else:
        words_list = words_dict[letters]
        words_dict[letters] = words_list.append(word)

# print len(all_words)
# print len(words_dict)

pp.pprint(words_dict)
