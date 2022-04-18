# 이 파일이 실행되는 날짜는 일요일 오후 12시
# 일단 chat.postMessage는 1. attachments 2. blocks[] as string 3. string만 받는다. 
# 즉, 그 각 포스트마다 날짜가 달라지는 부분을 파일이 실행되는 날짜를 기준으로 바꿔줘야한다. 
# {} : JSON 객체(python으로는 dict) // [] : JSON 배열(Python으로는 list)
# json.load => [JSON -> Python]
# json.dump => [Python -> JSON]

from slack import WebClient
import slack_post
import slack_get
import src.src_info as si
import src.src_time as st
import src.src_post as sp
from datetime import datetime
from pytz import timezone

today = datetime.now(timezone('Asia/Seoul'))

client = WebClient(si.BotOAuth.bot_token)

# 함수 호출 예시)
# post_message(si.ChannelID.cash_fit,sp.PostStatement.attend_vote_state)
def post_message(channel, blocks, text):
	client.chat_postMessage(channel=channel, blocks=blocks, text=text)

def vote_dm():
	users_id = si.UserID.users_id
	users_id_to_name = si.UserID.users_id_to_name
	vote_id = slack_get.get_vote_users_ahour(st.TimeStr.vote_post_time(today))
	for id in vote_id:
		users_id.remove(id)
	for user in users_id:
		print(users_id_to_name[user])
		slack_post.post_message(user, sp.PostStatement.attend_vote_ahour, "🔥🔥 북라톤 모임 참석 투표 독려 알림 🔥🔥")
#post_message(si.ChannelID.cash_fit,sp.PostStatement.attend_vote_state)
#post_message(si.ChannelID.cash_fit, slack_penalty.make_penalty())