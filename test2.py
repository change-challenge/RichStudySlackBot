from slack import WebClient
import time
from datetime import datetime, timedelta

# datetime을 timestamp로 바꾸는 함수
def datetimeToTimestamp(dateTime):
	return time.mktime(datetime.strptime(str(dateTime), '%Y-%m-%d %H:%M:%S').timetuple())

botToken = "xoxb-1830334374899-2443966688067-w0MZL8043NzMuxjWzAhtK4mw"
cash_fit = "C02QY3M5F7H"
announcement = "C01PZAK0NGP"
bookrathonTime = datetime(2022, 3, 19)
nextbookrathonTime = bookrathonTime + timedelta(days=14)
# print(bookrathonTime)
# print(nextbookrathonTime)
# print(datetimeToTimestamp(bookrathonTime))
# print(datetimeToTimestamp(nextbookrathonTime))





client = WebClient(botToken)


# channel_message = client.conversations_history(channel=announcement, oldest=datetimeToTimestamp(datetime(2022, 3, 19)))
# conversations = channel_message[announcement]
all_the_members = client.users_list()
users = all_the_members["members"]
# print(all_the_members)

# user_ids = list(map(lambda u: u["id"], users))

# print(channel_message)

# print(channel_message["messages"][1]["reactions"])

for users in users:
	print(users["id"] +" " + users["profile"]["real_name"])
# print(users[])


# print(users[1])

# print(channel_message["messages"][1]["reactions"])
# print(channel_message["messages"][1]["text"])
# print(conversations)



# 이모지는 타임스탬프가 뜨지 않는다. => 참석투표 => 10시에 한번 해주면 됨
# 즉, 10시에 정확히 불러와야한다는 듯인듯
