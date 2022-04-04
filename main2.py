# 부자칩 확인을 위해 구동할 파일 
# 한 달에 한번, 매월 1일 오전 0시에 구동되면 된다. 
# 구동되는 시점 기준, 한 달을 oldest로 잡은 뒤 글을 작성한 사람에 대한 데이터를 들고오고, 
# 1. 그 데이터들을 Slack에 공지한다. 
# 2. 구글 시트에도 추가를 한다. 

from slack import WebClient
from datetime import datetime
from pytz import timezone
import src.src_time as st
import src.src_info as si
import src.src_post as sp
import slack_post
import slack_get
import google_send

from dateutil.relativedelta import relativedelta
from pytz import timezone

today = datetime.now(timezone('Asia/Seoul'))

if __name__ == "__main__":
	# 매월 첫 날 오후 12시 
	if (today.day == 1):
		slack_post.post_message(channel=si.ChannelID.book_recomd, blocks=sp.make_book_recomd())
		google_send.send_richchip()
		print("==========[Slack] 매월 부자칩 추가 공지 완료==========")
		print("==========[Google] 매월 부자칩 추가 작성 완료==========")
		print("시간 : " + today.strftime('%c'))
