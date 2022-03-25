# 이 파일이 실행되는 날짜는 일요일 오후 12시
# 일단 chat.postMessage는 1. attachments 2. blocks[] as string 3. string만 받는다. 
# 즉, 그 각 포스트마다 날짜가 달라지는 부분을 파일이 실행되는 날짜를 기준으로 바꿔줘야한다. 
# {} : JSON 객체(python으로는 dict) // [] : JSON 배열(Python으로는 list)
# json.load => [JSON -> Python]
# json.dump => [Python -> JSON]

from slack import WebClient
import src.src_info as si
import src.src_post as sp
import slack_penalty

client = WebClient(si.BotOAuth.bot_token)


# 함수 호출 예시)
# post_message(si.ChannelID.cash_fit,sp.PostStatement.attend_vote_state)
def post_message(channel, blocks):
	client.chat_postMessage(channel=channel, blocks=blocks)


# post_message(si.ChannelID.cash_fit,sp.PostStatement.attend_vote_state)
post_message(si.ChannelID.cash_fit, slack_penalty.make_penalty())
# ===================================================================
# def post_to_slack(message, webhook_url):
# 	slack_data = json.dumps({'blocks': message}) 
# 	response = requests.post(
# 		webhook_url, 
# 		data=slack_data, 
# 		headers={'Content-Type': 'application/json'} 
# 	) 
# 	if response.status_code != 200: 
# 		raise ValueError( 
# 			'Request to slack returned an error %s, the response is:\n%s'
# 			% (response.status_code, response.text) 
# ) 