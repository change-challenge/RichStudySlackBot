import requests
import json
import slack
import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


botToken = "xoxb-1830334374899-2443966688067-w0MZL8043NzMuxjWzAhtK4mw"
# # myToken은 거의 사용 없다. 
# myToken = "xoxp-1830334374899-1853957534688-3251494072295-b70e8bf89cc4d9a0c416d14d3075940e" 


def read_message(token, channel):
	response = requests.get("https://slack.com/api/conversations.history",
		headers={
			'Content-Type': 'application/x-www-form-urlencoded',
			'token': token,
			'channel': channel
			})
	if response.status_code != 200:
		raise ValueError(
			'Request to slack returned an error %s, the response is:\n%s' 
			% (response.status_code, response.text) 
		) 
	print(response.json())


read_message(botToken, "C02QY3M5F7H")


# def post_message(token, channel, text):
#     response = requests.post("https://slack.com/api/chat.postMessage",
#                              headers={"Authorization": "Bearer " + token},
#                              data={"channel": channel, "text": text})
#     print(response)

# post_message(botToken, "C02QY3M5F7H", "hello")
