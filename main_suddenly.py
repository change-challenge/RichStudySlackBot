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

if __name__ == "__main__":
    today = datetime.now(timezone('Asia/Seoul'))
    if (st.get_timeidx(col_offset1, row_offset1, worksheet1, st.TimeStr.slack_post_check_time(today)) != -1):
        if (today.hour == 14):
                slack_post.post_message(si.ChannelID.announcement, sp.PostStatement.attend_vote_state)
                slack_post.post_message(si.ChannelID.question, sp.PostStatement.question_state)
                print("==========[Slack] 공지 작성 완료==========")
                print("시간 : " + today.strftime('%c'))
        else:
                print("==========[일요일 시간 오류]==========")
                print("시간 : " + today.strftime('%c'))
    else:
            print("==========[요일 오류]==========")
            print("시간 : " + today.strftime('%c'))
