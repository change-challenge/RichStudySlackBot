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

with open("/Users/hojinjang/Desktop/SlackBot-RichStudy/json/attendVote.json", "rt") as block_f:
	data = json.load(block_f) 

def post_to_slack_attend(message, webhook_url):
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
#post_to_slack_attend(data, cash_fit)

def exit():
	print("시스템을 종료합니다.")
	sys.exit()

schedule.every().sunday.at("13:53").do(post_to_slack_attend, data, annocement)
schedule.every().sunday.at("13:53").do(exit)

while True:
    schedule.run_pending()
    time.sleep(1)