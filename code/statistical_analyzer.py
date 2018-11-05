import constants
import pandas

THRESHOLD_MAP = { "RATIO_VIEW_COUNT_LIKE_DISLIKE_COUNT": 300,
					"RATIO_VIEW_COUNT_COMMENT_COUNT": 4500 }

def ratio_view_count_like_dislike_count(actual_videos, data_rvcldc):
	bot_videos = []
	counter = 0
	for data_point in data_rvcldc:
		try:
			if data_point >= THRESHOLD_MAP["RATIO_VIEW_COUNT_LIKE_DISLIKE_COUNT"]
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
			if data_point >= THRESHOLD_MAP["RATIO_VIEW_COUNT_COMMENT_COUNT"]
				bot_videos.append(actual_videos[counter])
			counter += 1
		except:
			counter += 1
			continue

	return bot_videos


def log_view_count_vs_like_dislike_count(actual_videos, data_lvc, data_lldc):
	"""
	TODO: 1) find slope for the trendline
	2) then find perpendicular distance to the trendline for all the videos
	3) return videos having distance more than threshold value
	"""
	pass


def evaluate_my_model():
	"""
	TODO: model accuracy based on ground truth
	"""
	pass

data = pd.read_csv(constants.STATISTICAL_ANALYZER_DIR_PATH + "view_bot.csv")
data_rvcldc = data["ratio_view_count_like_dislike_count"]
data_rvccc = data["ratio_view_count_comment_count"]
data_lvc = data["log_view_count"]
data_lldc = data["log_like_dislike_count"]
actual_videos = data["video_id"]

classified_bot_videos = ratio_view_count_comment_count(actual_videos, data_rvcldc)
evaluate_my_model(classified_bot_videos, actual_videos)

classified_bot_videos = ratio_view_count_like_dislike_count(actual_videos, data_rvccc)
evaluate_my_model(classified_bot_videos, actual_videos)

classified_bot_videos = log_view_count_vs_like_dislike_count(actual_videos, data_lvc, data_lldc)
evaluate_my_model()