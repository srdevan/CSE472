import base64
import constants
import glob
import json
import MySQLdb
import requests

api_key = base64.b64decode(open("API_KEY.txt", "r").read()).decode("utf-8")

def prepare_dataset(video_ids):
	db = MySQLdb.connect(host="localhost",  # your host 
						user="root",       # username
						db="bot_identification_warehouse")   # name of the database

	# Create a Cursor object to execute queries.
	cur = db.cursor()
	stat_file = open("video_statistics.csv", "w")
	stat_file.write("video_id, channel_id, subscriberCount, viewCount, likeCount, dislikeCount, commentCount,\
					comments\n")
	video_stat_url = constants.YOUTUBE_PREFIX_VIDEO_URL + api_key + "&id=" + ",".join(video_ids)
	response = get_video_stats(video_stat_url)

	if response.status_code == 200:
		video_stats = parse_response(response.text)
		channel_ids = [item["snippet"]["channelId"] for item in video_stats["items"]]
		channel_stat_url = constants.YOUTUBE_PREFIX_CHANNEL_URL + api_key + "&id=" + ",".join(channel_ids)
		channel_response = get_video_stats(channel_stat_url)

		if channel_response.status_code == 200:
			channel_stats = parse_response(channel_response.text)
			channel_id_subscriber_count = { item["id"]: item["statistics"]["subscriberCount"] for item in \
											channel_stats["items"] }

			for item in video_stats["items"]:
				item_stats = item["statistics"]
				channel_id = item["snippet"]["channelId"]
				subscriber_count = channel_id_subscriber_count[channel_id]
				comments = ""
				comment_count = 0
				if "commentCount" in item_stats.keys():
					comment_count = item_stats["commentCount"]
					comments = get_comments(item["id"], int(comment_count))
				sql = "insert into videos (video_id,channel_id,view_count,like_count,dislike_count,subscriber_count,\
				                          comment_count,comments) values (%s,%s,%s,%s,%s,%s,%s,%s)"
				val = (item["id"],channel_id,item_stats["viewCount"],item_stats["likeCount"],\
						item_stats["dislikeCount"],subscriber_count,comment_count,comments)
				cur.execute(sql, val)
				db.commit()

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
def parse_response(response):
	return json.loads(response)	

def parse_comments(response):
	comments = { }
	for item in response["items"]:
		comment_author_name = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
		comments[comment_author_name] = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

	return str(comments)

def get_comments(video_id, comment_count):
	comments = ""
	default = 100
	while(comment_count > 0):
		if default >= comment_count:
			comment_thread_url = constants.YOUTUBE_PREFIX_COMMENT_THREAD_URL + api_key + "&videoId=" + video_id + \
								"&maxResults=" + str(comment_count)
		else:
			comment_thread_url = constants.YOUTUBE_PREFIX_COMMENT_THREAD_URL + api_key + "&videoId=" + video_id + \
								"&maxResults=" + str(default)
		response = get_video_stats(comment_thread_url)
		if response.status_code == 200:
			parsed_response = parse_response(response.text)
			comments += parse_comments(parsed_response)
			comment_count -= 100

	return comments

def get_video_ids(data):
	video_hashes = []
	video_urls = [data.keys()]
	for video_url in video_urls:
		video_hashes.append(video_url.split("/")[-1])

	return video_hashes

video_ids = []
files = glob.glob(constants.TWEETTUBE_DIR_PATH_REGEX)
for file in files:
	with open(file) as fd:
		data = json.load(fd)
		video_ids += get_video_ids(data)

prepare_dataset(video_ids)