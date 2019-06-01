The main dataset of this project is a collection of about 33K tweets, which has been split into three parts: a training set, and a evaluation set, and a test set. For train and evaluation set each tweet has been manually assigned a sentiment: either ?positive?, ?negative? or ?neutral? 
(Undoubtedly, there will be some tweets where you might think that the sentiment should be labelled differently, but such is the nature of Knowledge Tasks! :-))

This dataset contains eight files (plus this README), in three types, as follows:

{train,eval,test}-tweets.txt: These files contain the raw text of the tweets, one tweet per line, in the following format:
tweet-id TAB tweet-text NEWLINE
Note that the text was pre-processed (folding case, and removing all characters that are not alphabetic ([a-z])) before feature engineering/selection was performed.

{train,eval}-labels.txt: These files contain the manually--assigned sentiment labels, one tweet per line, in the following format:
tweet-id TAB label NEWLINE
The labels are one of "positive", "negative", or "neutral". Note that you will not be given labels for the test data, you need to submit a TXT file that contains the labels for the test data as a part of your project submission.

{train,eval,test}.csv: In these files we transformed the information contained within the tweets text (from first the group) to a structured form. We applied feature selection to generate the frequencies of 45 tokens in the training data, and then summarised  as a row (vector) for each tweet-id in CSV format as follow.

#tweet-id,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0

Each number in this row(vector) demonstrate the frequency of the related attribute (token) in the given tweet.



