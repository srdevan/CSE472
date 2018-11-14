"""-
bot_inflated
organic
"""
import bot_users
import re

def f1(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			user_ids = bot_users.users
			j = comment.split("\t")
			for i in range(len(user_ids)):
				if(j[0].lower() in user_ids[i]):
					return 1
	return 0


def f2(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['easy way to earn money', 'earn money', 'free money', 'earn easy money', 'make money online',
						'earn online', 'earn money online', 'get money']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f3(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['watch and share', 'please share']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f4(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['my referral code', 'referral code']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f5(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['visit this site', 'take a look at', 'check out', 'please see', 'go to', 'follow the link',
						'plz go through']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f6(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['donate', 'need of support', 'help this guy', 'giveaways']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f7(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['my link', 'click on the link', 'download link']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f8(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['credit service']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f9(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['shoot me an email']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f10(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['dot com']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f11(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['facebook', 'instagram', 'gofundme']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f12(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['action now']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f13(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['subscribe me', 'comment and subscribe', 'follow us', 'subscribe']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f14(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['discount']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f15(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['invite']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0

def f16(sentence, tag):
	for comment in sentence:
		if(tag == "bot_inflated"):
			patterns = ['http', 'https']
			j = comment.split("\t")
			for i in range(len(patterns)):
				if(re.findall(patterns[i], j[1].lower())):
					return 1
	return 0