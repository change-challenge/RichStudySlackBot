from datetime import datetime, timedelta
import time
import src.src_time as st
# CERTIFICATE_VERIFY_FAILED 발생시 추가
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 여기까지 

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
				"text": "다음 북라톤 참여 여부를 위해 투표를 진행하려고 해요.\n *🤩: 참석  😭: 불참* 에 투표해주세요.\n\n*참석 못 하시는 분들은 <@U01R3U5FQL8> 카톡으로 사유* 를 말씀해주시고,\n *조가 정해지면 조장에게* 말씀해주시면 됩니다.\n\n*양희재 (010-2911-1973)*"
				}
		}
	]
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
