"""
1. removes all punctuations
2. stemming and lemmatization
"""
import constants
import glob
import json
import nltk
from nltk.stem import WordNetLemmatizer
import re
import string

wordnet_lemmatizer = WordNetLemmatizer()
files = glob.glob(constants.COMMENT_DIR_PATH)
for file in files:
	input_file = open(file, "r")
	output_file = open(constants.PROCESSED_COMMENT_DIR_PATH + file, "r")
	data = json.loads(input_file.readlines())
	# TODO fix json load here
	for user_id, comment in data:
		re.sub('['+string.punctuation+']', " ",comment)
		nltk_tokens = nltk.word_tokenize(comment)
		reconstructed_comment = " ".join([wordnet_lemmatizer.lemmatize(word) for word in nltk_tokens])
		output_file.write(user_id + "," + reconstructed_comment + "\n")