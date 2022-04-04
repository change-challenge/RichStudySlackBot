import src.src_time as st
import src.src_info as si
import slack_get
import google_get as gg
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pytz import timezone
# CERTIFICATE_VERIFY_FAILED 발생시 추가
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 여기까지 

class slack_format:
	vote_format = {
		"type" : "section",
		"text" : {
			"type" : "mrkdwn",
			"text" : " "
		}
	}
	question_format = {
		"type" : "section",
		"text" : {
			"type" : "mrkdwn",
			"text" : " "
		}
	}
	attend_format = {
		"type" : "section",
		"text" : {
			"type" : "mrkdwn",
			"text" : " "
		}
	}
	book_recomd_format = {
		"type" : "section",
		"text" : {
			"type" : "mrkdwn",
			"text" : "\t"
		}
	}

class PostStatement:
	attend_vote_state = [
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
					"text": "[🖐 " + st.TimeStr.bookrathon_time_str + " 북라톤 참석 인원 조사] \n\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ">✅ 책 :  자유 선정\n>✅ 모임 장소 : 그룹 별 상이\n>✅ 모임 날짜 : *" + st.TimeStr.bookrathon_time_str + " (토)* \n>✅ 투표 기간 : *" + st.TimeStr.attend_time_str + " (월) 저녁 22시까지 (벌금 有)* \n\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "다음 북라톤 참여 여부를 위해 투표를 진행하려고 해요.\n *🤩: 참석  😭: 불참* 에 투표해주세요.\n\n*참석 못 하시는 분들은 <@U01QEPH2TP1> 카톡으로 사유* 를 말씀해주시고,\n *조가 정해지면 조장에게* 말씀해주시면 됩니다.\n\n*양희재 (010-2911-1973)*"
				}
		}
	]
	# 호진 ID : U01R3U5FQL8
	# 희재 ID : U01QEPH2TP1
	question_state = [
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
					"text": "[✍️ " + st.TimeStr.bookrathon_time_str + " 북라톤 질문 선정] \n\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ">✅ 작성 기간 : *" + st.TimeStr.question_time_str + " (금) 저녁 22시까지 (벌금 有)* \n\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "다음 북라톤에서 이야기 나눌 질문을 이 스레드 답글로 적어주세요.\n질문을 어떻게 적어야 할 지 감이 오지 않는다면, 아래의 스레드를 참고해주세요. \n (<https://rich-study.slack.com/archives/C01PZAK0NGP/p1638678949003900>)"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*부자스터디의 힘은 질문* 에서 나옵니다.\n여러분이 *알고 싶은 것, 모르는 것을* 같이 이야기해봐요!\n"
				}
		}
	]
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
	book_recomd_state = [
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
					"text": "[ :coin: " + str((datetime.now(timezone('Asia/Seoul')) - relativedelta(months = 1)).month) + "월 책 추천 - 부자칩 보상] \n\n"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "부자칩을 받으신 모든 분들 축하합니다. 🥳🥳"
				}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "부자스터디에서 *`나누기는 곱하기`* 가 됩니다. \n여러분의 *경험과 지식을 나눌수록 더 채워지는 것* 을 느끼실거예요!😎\n\n"
				}
		}
	]

def make_format1(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 4,000원\n"
	return (slack)

def make_format2(slack, later_users):
	for users in later_users:
		slack["text"]["text"] += "- " + users + "씨 벌금 5,000원\n"
	return (slack)

def make_penalty():
	penalty = PostStatement.penalty_state
	vote_later, question_later, attend_later = gg.get_later('04/02')
	vote = make_format1(slack_format.vote_format, vote_later)
	question = make_format1(slack_format.question_format, question_later)
	attend = make_format2(slack_format.attend_format, attend_later)
	penalty.insert(3, vote)
	penalty.insert(5, question)
	penalty.insert(7, attend)
	return (penalty)

def make_book_recomd():
	book_recomd = PostStatement.book_recomd_state
	book_add_post = slack_format.book_recomd_format
	
	book_point = slack_get.get_book_recomd_point()
	idx = 0
	for point in book_point:
		if (point > 0):
			if (point == 1):
				point = int(point)
			book_add_post["text"]["text"] += "> • *" + si.UserID.users_name[idx] + "* : " + str(point) + "개\n"
		idx += 1
	book_recomd.insert(2, book_add_post)
	return (book_recomd)