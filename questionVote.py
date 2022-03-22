from email import message
import slack 
import json 
import requests 
import time
import schedule
import datetime
import sys

cash_fit = 'https://hooks.slack.com/services/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' 
annocement = 'https://hooks.slack.com/services/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'
question = 'https://hooks.slack.com/services/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'

with open("/Users/hchang/Desktop/RichStudySlackBot/json/attendVote.json", "rt") as block_f:
	attendData = json.load(block_f)

with open("/Users/hchang/Desktop/RichStudySlackBot/json/questionVote.json", "rt") as block_f:
	questionData = json.load(block_f) 

with open("/Users/hchang/Desktop/RichStudySlackBot/json/test.json", "rt") as block_f:
	testData = json.load(block_f) 

def post_to_slack(message, webhook_url):
	slack_data = json.dumps({'blocks': message}) 
	response = requests.post(
		webhook_url, 
		data=slack_data, 
		headers={'Content-Type': 'application/json'} 
	) 
	if response.status_code != 200: 
		raise ValueError( 
			'Request to slack returned an error %s, the response is:\n%s'
			% (response.status_code, response.text) 
		) 
post_to_slack(testData, cash_fit)

#def exit():
#	print("시스템을 종료합니다.")
#	sys.exit()

#schedule.every().day.at("12:04").do(post_to_slack, attendData, annocement)
##schedule.every().day.at("12:04").do(post_to_slack, questionData, question)
#schedule.every().day.at("12:04").do(exit)

#while True:
#    schedule.run_pending()
#    time.sleep(1)