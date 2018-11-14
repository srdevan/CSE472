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
	try:
		input_file = open(file, "r")
		path = file.split("/")[-1]
		output_file = open("/Users/shreyasdevan/Desktop/CSE 472/Project 2/detecting-bot-inflated-videos-on-youtube/dataset/comments/processed/" + file.split("/")[3], "w")
		comment_data = input_file.readlines()
		for each in comment_data:
			try:
				each = re.sub(r'\n', " ", each)
				user_id = re.split(r'\t+', each)[0]
				comment = re.split(r'\t+', each)[1]
				comment = re.sub('['+string.punctuation+']', " ",comment)
				nltk_tokens = nltk.word_tokenize(comment)
				reconstructed_comment = " ".join([wordnet_lemmatizer.lemmatize(word) for word in nltk_tokens])
				output_file.write(user_id + "\t" + reconstructed_comment + "\n")
			except:
				continue
	except:
		print("####################" + file)
		continue