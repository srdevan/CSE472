import constants
from feature_functions import *
import math
import numpy
import pickle
import random
import re
from scipy.optimize import minimize

class MyMaxEnt():            
	def __init__(self, history_list, old_tag_list, funcs):
		self.history_list = history_list
		self.training_data = []
		self.model = [1/31]*31
		self.old_tag_list = old_tag_list
		self.feature_func = funcs
		self.tag_list = ["bot_inflated", "organic"]
		self.create_dataset()
		
	def create_dataset(self):
		try:
			self.training_data = pickle.load(open(constants.DUMPED_OBJECTS_DIR_PATH + "history.p", "rb"))
		except:
			for history in self.history_list:
				self.training_data.append(self.find_vector_list(history))
			pickle.dump(self.training_data, open(constants.DUMPED_OBJECTS_DIR_PATH + "history.p", "wb")) 
			
	def find_vector(self,comment,tag):
		vector = []
		for feature in self.feature_func:
			vector.append(feature(comment, tag))

		return vector
		
	def find_vector_list(self,history):
		vector_list = []
		for tag in self.tag_list:
			vector = []
			try:
				for feature in self.feature_func:
					vector.append(feature(history, tag))
				vector_list.append(vector)
			except:
				continue

		return vector_list
		
	def cost(self,model):
		score = 0
		for iter in range(len(self.training_data)):
			try:
				score += math.log(self.p_y_given_x(self.history_list[iter], self.training_data[iter], self.old_tag_list[iter], model))
			except:
				continue

		return -score
			
	def p_y_given_x(self,hl,feature_vecs,tags,model):	
		prob = 0
		if len(tags) == 0:
			tags = ['None']
		for tag in tags:
			vector = []    
			for func in self.feature_func:
				vector.append(func(hl,tag))
			numerator = math.exp(numpy.dot(vector,model))
			denominator = 0
			for feature in feature_vecs:
				denominator += math.exp(numpy.dot(feature,model))
			prob += numerator * 1.0 / denominator

		return prob
		
	def classify(self, comment):
		cfier = []
		denominator = 0

		for tag in self.tag_list:
			try:
				denominator += math.exp(numpy.dot(self.find_vector(comment,tag),self.model))
			except:
				return "None"

		for tag in self.tag_list:
			num = math.exp(numpy.dot(self.find_vector(comment,tag),self.model))
			p = num/denominator
			cfier.append(p)

		print(cfier)
		for iter in range(len(cfier)):
			if cfier[iter] > 1/2.0:
				return "bot_inflated"
			else:
				return "organic"

	def train(self):
		obj = minimize(self.cost, self.model, method = "L-BFGS-B", jac=False)
		self.model = obj.x