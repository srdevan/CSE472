import constants
import json
from MaxEnt import MyMaxEnt
import MySQLdb
import pickle
import random

"""
1. get all video ids and shuffle the array
2. run maxent to train 75% data
3. once model is built, we can pass the remaining dataset as testset and evaluate accuracy of model.
"""

#TODO: handle exceptions and perform unit tests

def fetch_results(query):
	db = MySQLdb.connect(host = "localhost", user = "root", db = "bot_identification_warehouse")
	cur = db.cursor()
	cur.execute(query)
	results = cur.fetchall()

	return results

def get_videos_ids_and_comment_tags():
	query = "select (video_id, comment_bot_gt) from videos;"
	rows = fetch_results(query)
	video_comment_bot_tag_map = {}
	for row in rows:
		video_comment_bot_tag_map[row[0]] = row[1]

	return video_comment_bot_tag_map

def randomize_dataset(video_comment_bot_tag_map):
	video_ids = list(video_comment_bot_tag_map.keys())
	random.shuffle(video_ids)
	comment_bot_tags = []
	for video_id in video_ids:
		comment_bot_tags.append(video_comment_bot_tag_map[video_id])

	return video_ids, comment_bot_tags

def prepare_dataset(training_videos, train = True):
	dir_path = constants.TRAINING_DATA_DIR_PATH if train else constants.TESTING_DATA_DIR_PATH
	dataset = open(dir_path + "training_video_data.csv", "w")
	data = []
	for video_id in training_videos:
		video_file = open(constants.COMMENT_DIR_PATH + video_id + ".json", "r")
		comments = json.loads(video_file.readlines())

		for comment in comments:
			user = comment[0]
			reply = comment[1]
			row = user + "," + reply + "\n"
			dataset.write(row)
			data.append(row)

	return data

def train_my_model(video_ids, comment_bot_tags):
	number_of_videos = len(video_ids)
	training_data_index = (number_of_videos * 3) // 4
	training_videos = video_ids[0:training_data_index]
	training_comment_bot_tags = comment_bot_tags[0:training_data_index]
	training_dataset = prepare_dataset(training_videos)

	testing_videos = video_ids[training_data_index:]
	testing_comment_bot_tags = comment_bot_tags[training_data_index:]
	testing_dataset = prepare_dataset(testing_videos, False)

	max_ent = MyMaxEnt(training_dataset, training_comment_bot_tags, feature_func)
	max_ent.train()

	return max_ent, testing_dataset, testing_comment_bot_tags

def test_my_model(max_ent, testing_dataset):
	classified_as = []
	for row in testing_dataset:
		classified_as.append(max_ent.classify(row))

	return classified_as

def evaluate_my_model(output_tags, ground_truth_tags):
	print("Precision\tAccuracy\tF1 score\t\n")

if sys.argv[1] == "train":
	try:
		video_comment_bot_tags = get_videos_ids_and_comment_tags()
		video_ids, comment_bot_tags = randomize_dataset(video_comment_bot_tag_map)
		max_ent, testing_dataset, testing_comment_bot_tags = train_my_model(video_ids, comment_bot_tags)
		pickle.dump({ "model": max_ent.model, "test_data": testing_dataset, "test_comment_tags": \
						testing_comment_bot_tags}, open(constants.DUMPED_OBJECTS_DIR_PATH + "model.p","wb"))
	except:
		print("---")
else:
	try:
		objects = pickle.load(constants.DUMPED_OBJECTS_DIR_PATH + "model.p", "rb")
		test_my_model(objects["model"], objects["test_data"])
		evaluate_my_model(classified_as, objects["test_comment_tags"])
	except:
		print("---")