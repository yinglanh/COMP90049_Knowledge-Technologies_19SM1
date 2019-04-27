## COMP90049_Knowledge-Technologies_19SM1
The task of the project is leveraging spelling correction methods for the problem of lexical normalisation, i.e. finding a canonical form for each token with a document. The dataset contains three text files. One misspell.txt which corresponds to short messages from Twitter, and one correct.txt file shows the correct words corresponds to misspell.txt, and one dic.txt which contains the look up dictionary. 
The system tries to find whether the words are correctly spelled, if not, the system will return some predicted words which the correct words might be. There are two methods used in this system, one is based on basic Levenshtein "distance" function, and another is based on "ratio" function.

### LD.py
In order to analysis the achievement of basic LD method, a function “distance” in the python package called Levenshtein is imported in this python file. The test words are taken and a list of its spelling mutation numbers of Levenshtein distance are generated. For each predicted list, contains the words with maximum correct probability (minimum Levenshtein distance). The parameters is (m, i, d, r) = (0, 1, 1, 1).
'''
for i, misspell_word in enumerate(test_word):
    print("!!!TEST WORD: "+misspell_word+"!!!")
    l = []
    for word in dictionary:
        l.append(Word(word, Levenshtein.distance(misspell_word, word)))
    l = sorted(l, key=get_distance)
'''
Also, a text file contains the recall and precision during the process is included.
'''
    with open("LD-output.txt", "a") as f:
        f.write("Recall_now: {} Precision_word: {}\n".format(corrects / (i + 1), predicts.count(correct_word[i]) / len(predicts)))
'''
### Improved_LD.py
Similar to LD.py, a function “ratio” in the package Levenshtein is imported. The parameter vector in this function is (m, i, d, r) = (0, 1, 1, 2). The “ratio” only returns one word with best similarity for each test word.
'''
for i, misspell_word in enumerate(test_word):
    print("!!!Test word: "+misspell_word+"!!!")
    l = []
    for word in dictionary:
        l.append(Word(word, Levenshtein.ratio(misspell_word, word)))
    l = sorted(l, key=get_distance, reverse=True)
'''
Also, a text file contains the accuracy and correct word number during the process is included.
'''
    with open("Improved_LD_output.txt", "a") as f:
        f.write("Accuracy_now: {} Correct_word: {}\n".format(corrects / (i + 1), predicts.count(correct_word[i]) / len(predicts)))
'''
