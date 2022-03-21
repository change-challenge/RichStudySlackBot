import sys
import requests
import json
import slack
import time
import schedule
import datetime

myToken = "xoxb-1830334374899-2443966688067-w0MZL8043NzMuxjWzAhtK4mw"

#def post_message(token, channel, text):
#    response = requests.post("https://slack.com/api/chat.postMessage",
#        headers={"Authorization": "Bearer " + token},
#        data={"channel": channel,"text": text})
#print(now)

def read_message(token, channel):
    response = requests.get("https://slack.com/api/reactions.get",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel})
	if response.status_code != 200: 
		raise ValueError( 
			'Request to slack returned an error %s, the response is:\n%s' 
			% (response.status_code, response.text) 
		) 
	print(response)
	print(response.json())


read_message(myToken, "#cash-fit")

#def exit():
#	print("시스템을 종료합니다.")
#	sys.exit()
#post_msg = ""
#post_message(myToken,"#cash-fit", post_msg)
#schedule.every().day.at("12:58").do(post_message,myToken,"#cash-fit", post_msg)
#schedule.every().day.at("12:59").do(exit)

#while True:
#    schedule.run_pending()
#    time.sleep(1)	