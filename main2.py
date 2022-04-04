# 부자칩 확인을 위해 구동할 파일 
# 한 달에 한번, 매월 1일 오전 0시에 구동되면 된다. 
# 구동되는 시점 기준, 한 달을 oldest로 잡은 뒤 글을 작성한 사람에 대한 데이터를 들고오고, 
# 1. 그 데이터들을 Slack에 공지한다. 
# 2. 구글 시트에도 추가를 한다. 

from slack import WebClient
from datetime import datetime
import src.src_time as st
import src.src_post as sp
import src.src_info as si
import slack_post
import slack_get
import google_send


from dateutil.relativedelta import relativedelta
from pytz import timezone


client = WebClient(si.BotOAuth.bot_token)

# print(slack_get.get_book_recomd_point())
# a = datetime.now(timezone('Asia/Seoul')) - relativedelta(months = 1)
# print(a.month)
client.chat_postMessage(channel=si.ChannelID.cash_fit, blocks=sp.make_book_recomd())