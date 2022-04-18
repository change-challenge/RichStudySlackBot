# 시간을 과연 어떤 식으로 판단할 수 있는가?
# 각 기능마다 실행하는 파일을 만들어놓고, 그 파일을 돌아가게 하는 것이 나은 것인가?
# 아니면, main 하나를 만들어놓고, 시간을 판단하면서 돌아간게 하는 것이 맞는 것인가? 
from datetime import datetime
import src.src_time as st
import src.src_post as sp
import src.src_info as si
import slack_post
import slack_get
import google_send
from pytz import timezone

col_offset1 = 2
row_offset1 = 4
worksheet1 = si.import_googlesheet('2022년 상반기 벌금명단')
today = datetime.now(timezone('Asia/Seoul'))
vote_noti = "🖐 " + st.TimeStr.bookrathon_time_str + " 북라톤 참석 투표 공지"
question_noti = "✍️ " + st.TimeStr.bookrathon_time_str + " 북라톤 질문 선정 공지"


if __name__ == "__main__":
	print("######################시작####################################")
	# 월요일 
	if (st.get_timeidx(col_offset1, row_offset1, worksheet1, st.TimeStr.vote_check_time(today)) != -1):
		if (today.hour == 12):
			slack_post.post_message(si.ChannelID.penalty, sp.make_penalty(), "💸 부자스터디 벌금 알림 💸")
			print("==========[Slack] 월요일 모든 벌금 글 작성==========")
			print("시간 : " + today.strftime('%c'))
		elif (today.hour == 21):
			slack_post.vote_dm()
			print("==========[Slack] 미 투표자 독려 DM==========")
			print("시간 : " + today.strftime('%c'))
		elif (today.hour == 22):
			google_send.send_later(st.TimeStr.vote_check_time(today), slack_get.get_vote_users(st.TimeStr.vote_post_time(today)),'v')
			print("==========[Google Sheet] 월요일 참석투표 지각자 체크==========")
			print(slack_get.get_vote_users(st.TimeStr.vote_post_time(today)))
			print("시간 : " + today.strftime('%c'))
		else:
			print("==========[월요일 시간 오류]==========")
			print("시간 : " + today.strftime('%c'))
	# 금요일
	elif (st.get_timeidx(col_offset1, row_offset1, worksheet1, st.TimeStr.question_check_time(today)) != -1):
		if (today.hour == 22):
			google_send.send_later(st.TimeStr.question_check_time(today), slack_get.get_question_users(), 'q')
			print("==========[Google Sheet] 금요일 질문선정 지각자 체크==========")
			print(slack_get.get_question_users())
			print("시간 : " + today.strftime('%c'))
		else:
			print("==========[금요일 시간 오류]==========")
			print("시간 : " + today.strftime('%c'))
	# 일요일
	elif (st.get_timeidx(col_offset1, row_offset1, worksheet1, st.TimeStr.slack_post_check_time(today)) != -1):
		if (today.hour == 12):
			slack_post.post_message(si.ChannelID.announcement, sp.PostStatement.attend_vote_state, vote_noti)
			slack_post.post_message(si.ChannelID.question, sp.PostStatement.question_state, question_noti)
			print("==========[Slack] 일요일 공지 작성==========")
			print("시간 : " + today.strftime('%c'))
		else:
			print("==========[일요일 시간 오류]==========")
			print("시간 : " + today.strftime('%c'))
	else:
		print("==========[요일 오류]==========")
		print("시간 : " + today.strftime('%c'))
	print("###############################끝################################")
