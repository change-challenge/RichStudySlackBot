from slack import WebClient
import slack_post
import src.src_post as sp
import src.src_info as si
import src.src_time as st
from datetime import datetime
from pytz import timezone

today = datetime.now(timezone('Asia/Seoul'))

client = WebClient(si.BotOAuth.bot_token)
users_id = si.UserID.users_id
users_id_to_name = si.UserID.users_id_to_name

def get_vote_users(date_time):
	total_users = []
	attend_users_id = []
	absent_users_id = []
	timestamp = st.datetime_to_timestamp(date_time)
	vote_history = client.conversations_history(channel=si.ChannelID.announcement, oldest=timestamp)
	for result in vote_history["messages"]:
		if (result["user"] == "U02D1UEL81Z"):
			attend_users_id = result["reactions"][0]["users"]
			absent_users_id = result["reactions"][1]["users"]
	return (attend_users_id + absent_users_id)

vote_id = get_vote_users(st.TimeStr.vote_post_time(today))

for id in vote_id:
	users_id.remove(id)

attend_vote_ahour = [
		{
			"type": "header",
				"text": {
					"type": "plain_text",
					"text": ":alert::alert: [북라톤 참석 투표 마감 알림] :alert::alert:\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "현재 북라톤 참석 투표가 *1시간* 남았습니다.\n신속히 투표를 해주시기 바랍니다. \n"
				}
		}
	]

for user in users_id:
	print(users_id_to_name[user])
	slack_post.post_message(user, attend_vote_ahour)