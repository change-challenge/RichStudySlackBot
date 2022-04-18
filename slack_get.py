from slack import WebClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone

import src.src_info as si
import src.src_time as st

client = WebClient(si.BotOAuth.bot_token)
users_name = si.UserID.users_name

# get_vote_users(st.TimeStr.twodayago_ts_ex)
# 돌아가는 시간은 월요일 저녁 22시
def get_vote_users(date_time):
	total_users = []
	attend_users_id = []
	absent_users_id = []
	timestamp = st.datetime_to_timestamp(date_time)
	total_users_chk = [0 for _ in range(len(users_name))]
	vote_history = client.conversations_history(channel=si.ChannelID.announcement, oldest=timestamp)
	for result in vote_history["messages"]:
		if (result["user"] == "U02D1UEL81Z"):
			attend_users_id = result["reactions"][0]["users"]
			absent_users_id = result["reactions"][1]["users"]
	# total_users 에는 투표한 인원(참석자 + 불참자)의 한글 이름이 정리되지 않은 상태로 있다.
	for users in attend_users_id + absent_users_id:
		total_users.append(si.UserID.users_id_to_name[users])
	for users in total_users:
		total_users_chk[users_name.index(users)] = 1
	return total_users_chk


# 돌아가는 시간은 금요일 저녁 22시
def get_question_users():
	total_users_chk = [0 for _ in range(len(users_name))]
	question_users = client.conversations_history(channel=si.ChannelID.question)["messages"][0]["reply_users"]
	for users in question_users:
		total_users_chk[users_name.index(si.UserID.users_id_to_name[users])] = 1
	return total_users_chk

# 돌아가는 시간 매월 1일 오후 12시
def get_book_recomd_point():
	total_user = []
	total_users_chk = [0 for _ in range(len(si.UserID.users_name))]
	today = datetime.now(timezone('Asia/Seoul'))
	mon_ago = (today - relativedelta(months = 1)).timestamp()
	book_recomd_history = client.conversations_history(channel=si.ChannelID.book_recomd, oldest=mon_ago)
	for result in book_recomd_history["messages"]:
		if (result["user"] == "U02D1UEL81Z"):
			continue
		# 5월엔 삭제할 것 
		if (result["client_msg_id"] == "8f8930a5-ad4f-47ea-93ec-b9abb327a7aa"):
			continue
		# 여기까지
		total_user.append(si.UserID.users_id_to_name[str(result["user"])])
	for users in total_user:
		tmp = total_users_chk[si.UserID.users_name.index(users)]
		if (tmp < 1):
			total_users_chk[si.UserID.users_name.index(users)] += 0.5
	return (total_users_chk)

# 1시간 전 DM용
def get_vote_users_ahour(date_time):
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