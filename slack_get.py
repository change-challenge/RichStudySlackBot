from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from slack import WebClient
import json
import time
from datetime import date, datetime, timedelta
import src.src_info as si
import src.src_post as sp

client = WebClient(si.BotOAuth.bot_token)
channel_message = client.conversations_history(channel=si.ChannelID.announcement)
#conversations = channel_message[si.ChannelID.announcement]
#client.conversations_history(channel=si.ChannelID.announcement)

# datetime을 timestamp로 바꾸는 함수
def datetime_to_timestamp(dst_time):
	return time.mktime(datetime.strptime(dst_time, '%Y-%m-%d %H:%M:%S').timetuple())

attend_users = []
absent_users = []
# 돌아가는 시간은 월요일 저녁 22시
def get_attend_users(timestamp):
	conversation_history = client.conversations_history(channel=si.ChannelID.announcement, oldest=timestamp)
	for result in conversation_history["messages"]:
		if ("subtype" in result):
			return (result["reactions"][0]["users"], result["reactions"][1]["users"])

#print(datetime.today())
#print(time.mktime(datetime.today().timetuple()))

today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
twodayago = (datetime.today() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')
#twodayago = (datetime.today() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')
today_ts = datetime_to_timestamp(today)
twodayago_ts = datetime_to_timestamp(twodayago)

attend_users, absent_users = get_attend_users(twodayago_ts)

#print(attend_users)
#print(absent_users)
a = []
b = []
for users in attend_users:
	a.append(si.UserID.user_id_to_name[users])
for users in absent_users:
	b.append(si.UserID.user_id_to_name[users])
#print(a)
#print(b)
c = a + b
print(c)
#print("attend_users : ")
#print(attend_users)
#print("absent_users : ")
#print(absent_users)
