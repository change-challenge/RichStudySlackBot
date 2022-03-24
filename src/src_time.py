from datetime import datetime, timedelta
import time

# readme first
# 1. 아래 6개 변수의 포맷 "2022-04-02"
# google_sheet_time은 월요일 기준, 이틀 전 토요일 (북라톤 날짜)
# penalty_time은 월요일 기준, 금요일 (벌금 데드라인 날짜)
# attend_time은 일요일 기준, 월요일 (참석 투표 날짜)
# question_time은 일요일 기준, 다음주 금요일 (질문 선정 날짜)
# bookrathon_time은 일요일 기준, 다음주 토요일 (북라톤 날짜)
# twodayago은 월요일 기준, 46시간 전 (post 시간)
# 2.
# check_time의 포맷은 "04/02" (google sheet에서 날짜 구분해주는 값)
# 3. 
# nowtimeStr // attend_time_str // question_time_str // bookrathon_time_str
# 위의 것들의 포맷은 "2022년 04월 02일"

nowtime = datetime.today().strftime('%Y-%m-%d')
google_sheet_time = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
penalty_time = (datetime.today() + timedelta(days=4)).strftime('%Y-%m-%d')
attend_time = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d') 
question_time = (datetime.today() + timedelta(days=12)).strftime('%Y-%m-%d') 
bookrathon_time = (datetime.today() + timedelta(days=13)).strftime('%Y-%m-%d')
twodayago = (datetime.today() - timedelta(hours=46)).strftime('%Y-%m-%d %H:%M:%S')
twodayago_ex = (datetime.today() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')

# datetime을 timestamp로 바꾸는 함수
def datetime_to_timestamp(dst_time):
	return time.mktime(datetime.strptime(dst_time, '%Y-%m-%d %H:%M:%S').timetuple())

class TimeStr:
	# 민수가 쓸 시간 (함수 구현 시, 함수를 돌릴 수 있게 two_dayago_ts_ex를 만들어놨다.)
	twodayago_ts = datetime_to_timestamp(twodayago)
	twodayago_ts_ex = datetime_to_timestamp(twodayago_ex)
	
	check_time = google_sheet_time[5:7] + "/" + google_sheet_time[8:10]

	nowtimeStr = nowtime[0:4] + "년 " + nowtime[5:7] + "월 " + nowtime[8:10] + "일"
	attend_time_str = attend_time[0:4] + "년 " + attend_time[5:7] + "월 " + attend_time[8:10] + "일"
	question_time_str = question_time[0:4] + "년 " + question_time[5:7] + "월 " + question_time[8:10] + "일"
	bookrathon_time_str = bookrathon_time[0:4] + "년 " + bookrathon_time[5:7] + "월 " + bookrathon_time[8:10] + "일"