import constants
import numpy as np
import pandas as pd

THRESHOLD_MAP = { "RATIO_VIEW_COUNT_LIKE_DISLIKE_COUNT": 300,
					"RATIO_VIEW_COUNT_COMMENT_COUNT": 4500 }

def ratio_view_count_like_dislike_count(actual_videos, data_rvcldc):
	bot_videos = []
	counter = 0
	for data_point in data_rvcldc:
		try:
			if data_point >= THRESHOLD_MAP["RATIO_VIEW_COUNT_LIKE_DISLIKE_COUNT"]:
				bot_videos.append(actual_videos[counter])
			counter += 1
		except:
			counter += 1
			continue

	return bot_videos


def ratio_view_count_comment_count(actual_videos, data_rvccc):
	bot_videos = []
	counter = 0
	for data_point in data_rvccc:
		try:
			if data_point >= THRESHOLD_MAP["RATIO_VIEW_COUNT_COMMENT_COUNT"]:
				bot_videos.append(actual_videos[counter])
			counter += 1
		except:
			counter += 1
			continue

	return bot_videos


def log_view_count_vs_like_dislike_count(actual_videos, data_lvc, data_lldc):
	"""
	1) find slope for the trendline
	2) then find perpendicular distance to the trendline for all the videos
	3) return videos having distance more than threshold value
	"""
	bot_videos = []
	first_point_x = 0
	first_point_y = 1.568
	second_point_x = 6.64
	second_point_y = 8.31

	first_point = np.array([first_point_x, first_point_y])
	second_point = np.array([second_point_x, second_point_y])
	range_1 = second_point - first_point
	norm_len = np.linalg.norm(range_1)

	for iter in range(len(data_lvc)):
		point = np.array([data_lldc[iter], data_lvc[iter]])
		distance = np.cross(range_1, point - first_point) / norm_len

		if(distance > 0 and distance > 0.5): #we considered the threshold point as (1.3, 3.59)
			bot_videos.append(actual_videos[iter])

	return bot_videos

data = pd.read_csv(constants.STATISTICAL_ANALYZER_DIR_PATH + "view_bot.csv")
data_rvcldc = data["ratio_view_count_like_dislike_count"]
data_rvccc = data["ratio_view_count_comment_count"]
data_lvc = data["log_view_count"]
data_lldc = data["log_like_dislike_count"]
actual_videos = data["video_id"]

classified_bot_videos_rvccc = ratio_view_count_comment_count(actual_videos, data_rvccc)
classified_bot_videos_rvcldc = ratio_view_count_like_dislike_count(actual_videos, data_rvcldc)
classified_bot_videos_lvcvldc = log_view_count_vs_like_dislike_count(actual_videos, data_lvc, data_lldc)
final_bot_identified_videos = set(classified_bot_videos_lvcvldc + classified_bot_videos_rvcldc + \
								classified_bot_videos_rvccc)
print("The ViewBot inflated videos are: ")
print(final_bot_identified_videos)