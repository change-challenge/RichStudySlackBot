# 파이썬은 call by refernce ? by value?
# 파이썬은 passed by assignment이다. 
# 자료구조에 따라 call by refernce인 지, by value인 지 달라진다. 
# dict은 가변변수라 call by reference이다. 그래서 자꾸 그 안에 값이 바뀌는 것. 

import googlesheet as gs
import src.src_time as st
import src.src_post as sp

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
json_key_path = "./richstudy-b474b3ff05a8.json"	# JSON Key File Path
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1DuBSkKT665lYLiatWSIZ94NssrhH5ErJQheUdFuPYKk/edit#gid=2139714808"

vote_later, question_later, attend_later = gs.get_later(spreadsheet_url, 3)

penalty_state = [
{
	"type": "context",
	"elements": [
		{
			"type": "mrkdwn",
			"text": "@here"
		}
	]
},
{
	"type": "header",
		"text": {
			"type": "plain_text",
			"text": "[💸 " + st.TimeStr.nowtime_str + " 현재 벌금] \n\n"
		}
},
{
	"type": "section",
	"text": {
		"type": "mrkdwn",
		"text": "*[모임 투표 지각자] *"
		}
},
{
	"type": "section",
	"text": {
		"type": "mrkdwn",
		"text": "*[질문 선정 지각자] *"
		}
},
{
	"type": "section",
	"text": {
		"type": "mrkdwn",
		"text": "*[모임 지각자] *"
		}
},
{
	"type": "section",
	"text": {
		"type": "mrkdwn",
		"text": "모든 벌금은 *"+ st.TimeStr.penalty_time_str + " (금) 23시 59분까지*  내야합니다.\n*기간 안에 내지 않으면, x2* 가 됩니다. 😢\n\n*벌금 내신 분들은 이 글에 이모지✅* 를 달아주세요.\n\n"
		}
}]

def make_format1(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 4,000원\n"
	return (slack)

def make_format2(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 5,000원\n"
	return (slack)

a = make_format1(sp.slack_format.vote_format, vote_later)
b = make_format1(sp.slack_format.question_format, question_later)
c = make_format2(sp.slack_format.attend_format, attend_later)

penalty_state.insert(3, a)
penalty_state.insert(5, b)
penalty_state.insert(7, c)

result = penalty_state