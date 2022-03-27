from datetime import date, datetime, timedelta
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from slack import WebClient
import src.src_info as si
import src.src_time as st

client = WebClient(si.BotOAuth.bot_token)
users_name = si.UserID.users_name

# get_vote_users(st.TimeStr.twodayago_ts_ex)
# 돌아가는 시간은 월요일 저녁 22시
def get_vote_users(timestamp):
	total_users = []
	attend_users_id = []
	absent_users_id = []
	total_users_chk = [0 for _ in range(len(users_name))]
	vote_history = client.conversations_history(channel=si.ChannelID.announcement, oldest=timestamp)

	for result in vote_history["messages"]:
		if ("subtype" in result):
			attend_users_id = result["reactions"][0]["users"]
			absent_users_id = result["reactions"][1]["users"]
	# total_users 에는 투표한 인원(참석자 + 불참자)의 한글 이름이 정리되지 않은 상태로 있다.
	for users in attend_users_id + absent_users_id:
		total_users.append(si.UserID.user_id_to_name[users])
	for users in total_users:
		total_users_chk[users_name.index(users)] = 1
	return total_users_chk

# 돌아가는 시간은 금요일 저녁 22시
def get_question_users():
	total_users_chk = [0 for _ in range(len(users_name))]
	question_users = client.conversations_history(channel=si.ChannelID.question)["messages"][0]["reply_users"]
	for users in question_users:
		total_users_chk[users_name.index(si.UserID.user_id_to_name[users])] = 1
	return total_users_chk
