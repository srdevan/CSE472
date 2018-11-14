import base64
import constants
import glob
import json
import MySQLdb
import requests

api_key = base64.b64decode(open("API_KEY.txt", "r").read()).decode("utf-8")

def prepare_dataset(video_id):
	db = MySQLdb.connect(host="localhost",  # your host 
						user="root",       # username
						db="bot_identification_warehouse")   # name of the database

	# Create a Cursor object to execute queries.
	cur = db.cursor()
	# stat_file = open("video_statistics.csv", "w")
	# stat_file.write("video_id, channel_id, subscriberCount, viewCount, likeCount, dislikeCount, commentCount,\
					# comments\n")
	# import pdb
	# pdb.set_trace()
	video_stat_url = constants.YOUTUBE_PREFIX_VIDEO_URL + api_key + "&id=" + video_id
	response = get_video_stats(video_stat_url)
	import pdb
	# pdb.set_trace()
	if response.status_code == 200:
		video_stats = parse_response(response.text)
		channel_ids = [item["snippet"]["channelId"] for item in video_stats["items"]]
		channel_stat_url = constants.YOUTUBE_PREFIX_CHANNEL_URL + api_key + "&id=" + ",".join(channel_ids)
		channel_response = get_video_stats(channel_stat_url)

		if channel_response.status_code == 200:
			channel_stats = parse_response(channel_response.text)
			channel_id_subscriber_count = { item["id"]: item["statistics"]["subscriberCount"] for item in \
											channel_stats["items"] }

			comments = ""
			item = video_stats["items"][0]
			item_stats = item["statistics"]
			channel_id = item["snippet"]["channelId"]
			subscriber_count = channel_id_subscriber_count[channel_id]
			comment_count = 0

			if "commentCount" in item_stats.keys():
				comment_count = item_stats["commentCount"]
				comments += get_comments(item["id"], int(comment_count))
			sql = "insert into videos (video_id,channel_id,view_count,like_count,dislike_count,subscriber_count,\
			                          comment_count) values (%s,%s,%s,%s,%s,%s,%s)"
			val = (item["id"],channel_id,item_stats["viewCount"],item_stats["likeCount"],\
					item_stats["dislikeCount"],subscriber_count,comment_count)

			cur.execute(sql, val)
			db.commit()

			comments_file = open(constants.COMMENT_DIR_PATH + video_id + ".json", "w")
			comments_file.write(comments)

def get_video_stats(url):
	return requests.get(url)

'''
{
 "kind": "youtube#videoListResponse",
 "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/snMkhZ_jdSocpldTvoUS4Njmo0g\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 1
 },
 "items": [
  {
   "kind": "youtube#video",
   "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/acLzHHVFPZeBUyaWRbtTUJ2HcxU\"",
   "id": "C0DPdy98e4c",
   "statistics": {
	"viewCount": "773907",
	"likeCount": "400",
	"dislikeCount": "188",
	"favoriteCount": "0"
   }
  }
 ]
}
'''
def prepare_comment_dataset():
	db = MySQLdb.connect(host="localhost",  # your host 
						user="root",       # username
						db="bot_identification_warehouse")   # name of the database

	# Create a Cursor object to execute queries.
	cur = db.cursor()
	query = "select video_id, comment_count from videos where video_id = 'Mpb0E9qWGjo';"
	cur.execute(query)
	results = cur.fetchall()
	for result in results:
		video_id = result[0]
		comment_count = result[1]
		file = open(constants.COMMENT_DIR_PATH + video_id + ".tsv", "w")
		comments = get_comments(video_id, comment_count)
		for comment_author, comment in comments.items():
			file.write(comment_author + "\t" + str(comment) + "\n")
		print("File " + video_id + "written")
		# exit()

def parse_response(response):
	return json.loads(response)	

def parse_comments(response):
	comments = { }
	for item in response["items"]:
		comment_author_name = (item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]).replace("\t", " ").replace("\n", " ")
		comments[comment_author_name] = (item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]).replace("\t", " ").replace("\n", " ")

	return comments


def get_comments(video_id, comment_count):
	comments = {}
	default = 100
	next_page_token = ""
	while(comment_count > 0):
		if default >= comment_count:
			comment_thread_url = constants.YOUTUBE_PREFIX_COMMENT_THREAD_URL + api_key + "&videoId=" + video_id + \
								"&maxResults=" + str(comment_count) + "&pageToken=" + next_page_token
		else:
			comment_thread_url = constants.YOUTUBE_PREFIX_COMMENT_THREAD_URL + api_key + "&videoId=" + video_id + \
								"&maxResults=" + str(default) + "&pageToken=" + next_page_token
		response = get_video_stats(comment_thread_url)
		if response.status_code == 200:
			parsed_response = parse_response(response.text)
			import pdb
			# pdb.set_trace()
			if "nextPageToken" in list(parsed_response.keys()):
				# pdb.set_trace()
				next_page_token = parsed_response["nextPageToken"]

			comments.update(parse_comments(parsed_response))
			comment_count -= 100

	return comments

def get_video_ids(data):
	video_hashes = []
	video_urls = list(data.keys())
	for video_url in video_urls:
		temp = video_url.split("/")[-1]
		video_hashes.append(temp.split("?")[0])

	return video_hashes

prepare_comment_dataset()
# files = glob.glob(constants.TWEETTUBE_DIR_PATH_REGEX)
# files = ["../dataset/tweettube_dataset/3.json"]
# for file in files:
# 	with open(file) as fd:
# 		data = json.load(fd)
# 		video_ids = get_video_ids(data)
# 		for video_id in video_ids[:]:
# 			try:
# 				prepare_dataset(video_id) 
# 			except:
# 				print("Exception")
