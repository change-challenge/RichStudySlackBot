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

penalty = sp.PostStatement.penalty_state
vote_later, question_later, attend_later = gs.get_later(spreadsheet_url, 3)

def make_format1(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 4,000원\n"
	return (slack)

def make_format2(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 5,000원\n"
	return (slack)

def make_penalty():
	vote = make_format1(sp.slack_format.vote_format, vote_later)
	question = make_format1(sp.slack_format.question_format, question_later)
	attend = make_format2(sp.slack_format.attend_format, attend_later)
	
	penalty.insert(3, vote)
	penalty.insert(5, question)
	penalty.insert(7, attend)
	return (penalty)