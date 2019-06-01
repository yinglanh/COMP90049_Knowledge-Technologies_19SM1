import Levenshtein
import os

os.listdir(r'/Users/yinglanhuang/Documents/Github/COMP90049_Knowledge-Technologies_19SM1')
# os.listdir(os.path.expanduser('~/Documents/Github/COMP90049_Knowledge-Technologies_19SM1'))
# os.chdir(r'Users/yinglanhuang/Documents/Github/COMP90049_Knowledge-Technologies_19SM1')

# Add words to the lists

dictionary = []
with open('dict.txt') as f:
    for word in f:
        dictionary.append(word.strip())

test_word = []
with open('misspell.txt') as f:
    for line in f:
        test_word.append(line.strip())

correct_word = []
with open('correct.txt') as f:
    for line in f:
        correct_word.append(line.strip())

'''
    # TEST
    print(len(correct_word))
    print(len(test_word))
    print(len(dictionary))
'''

class Word:
    def __init__(self, word, distance):
        self.word = word
        self.distance = distance
    def __str__(self):
        return "{} - {}".format(self.word, self.distance)
    def __repr__(self):
        return "{} - {}".format(self.word, self.distance)

def get_distance(word):
    return word.distance

with open("LD-output.txt", "w") as f:
    pass

corrects = 0
predicts_num = 0
for i, misspell_word in enumerate(test_word):
    # TEST
    print("!!!TEST WORD: "+misspell_word+"!!!")
    l = []
    for word in dictionary:
        l.append(Word(word, Levenshtein.distance(misspell_word, word)))
        # TEST
        # print("dic word appended to list l", word)

    l = sorted(l, key=get_distance)

    # TEST
    print("Sorted list l ")
    print(l)

    # dis is the min LD in dic, predicts[] gets all the words with min LD
    dis = l[0].distance
    predicts = []
    for w in l:
        if w.distance == dis:
            predicts.append(w.word)
        else:
            break

    print("Predicted list ")
    print(predicts)

    print("!!!CORRECT WORD: "+correct_word[i]+"!!!"+"\n")

    # check correct words, if it is found in the predict list, +1
    if correct_word[i] in predicts:
        corrects = corrects + 1
    # accuracy = accuracy + predicts.count(correct_word[i]) / len(predicts)
    # print("{}/{} accuracy: {}".format(i, len(test_word), corrects / (i + 1)))
    # print("{}/{} precision: {}".format(i, len(test_word), predicts.count(correct_word[i]) / len(predicts)))

    with open("LD-output.txt", "a") as f:
        f.write("Recall_now: {} Precision_word: {}\n".format(corrects / (i + 1), predicts.count(correct_word[i]) / len(predicts)))

        '''
        # TEST
        print("write output"+"accuracy now:")
        print(corrects / (i + 1))
        print("write output" + "precision on this word now:")
        print(predicts.count(correct_word[i]) / len(predicts))
        '''
    predicts_num = predicts_num + len(predicts)

# test results
# '''
print("Corrects: ",corrects)
print("Test_word: ",len(test_word))
# print(Predicts: ",len(predicts))
# '''

print("Recall: {}".format(corrects / len(test_word)))
print("Precision: {}".format(corrects / predicts_num))



