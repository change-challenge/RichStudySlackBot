# 이 파일이 실행되는 날짜는 일요일 오후 12시
# 일단 chat.postMessage는 1. attachments 2. blocks[] as string 3. string만 받는다. 
# 즉, 그 각 포스트마다 날짜가 달라지는 부분을 파일이 실행되는 날짜를 기준으로 바꿔줘야한다. 
# {} : JSON 객체(python으로는 dict) // [] : JSON 배열(Python으로는 list)
# json.load => [JSON -> Python]
# json.dump => [Python -> JSON]

from slack import WebClient
import src.src_info as si
import src.src_post as sp

client = WebClient(si.BotOAuth.bot_token)

def post_message(channel, blocks):
	client.chat_postMessage(channel=channel, blocks=blocks)






#def exit():
#	print("시스템을 종료합니다.")
#	sys.exit()

#schedule.every().day.at("12:04").do(post_to_slack, attendData, annocement)
##schedule.every().day.at("12:04").do(post_to_slack, questionData, question)
#schedule.every().day.at("12:04").do(exit)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

#def post_to_slack(message, webhook_url):
#	slack_data = json.dumps({'blocks': message}) 
#	response = requests.post(
#		webhook_url, 
#		data=slack_data, 
#		headers={'Content-Type': 'application/json'} 
#	) 
#	if response.status_code != 200: 
#		raise ValueError( 
#			'Request to slack returned an error %s, the response is:\n%s'
#			% (response.status_code, response.text) 
#		) 