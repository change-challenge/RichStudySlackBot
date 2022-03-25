from datetime import datetime, timedelta
import time

# [readme first]
# google_sheet_time은 월요일 기준, 이틀 전 토요일 (북라톤 날짜)
# penalty_time_src은 월요일 기준, 금요일 (벌금 데드라인 날짜)
# twodayago_ts는 월요일 기준, 46시간 전 (post 시간)

# attend_time_src은 일요일 기준, 월요일 (참석 투표 날짜)
# question_time_src은 일요일 기준, 다음주 금요일 (질문 선정 날짜)
# bookrathon_time_src은 일요일 기준, 다음주 토요일 (북라톤 날짜)
# check_time은 월요일 기준, 이틀 전 토요일 (google sheet에서 날짜 구분해주는 값)
col_offset = 2
rol_offset = 4
vote_check_time = (datetime.today() - timedelta(hours=46)).strftime('%Y-%m-%d %H:%M:%S')
vote_check_time_ex = (datetime.today() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')

# datetime을 timestamp로 바꾸는 함수
def datetime_to_timestamp(dst_time):
	return time.mktime(datetime.strptime(dst_time, '%Y-%m-%d %H:%M:%S').timetuple())

class TimeStr:
	# 민수가 쓸 시간 (함수 구현 시, 함수를 돌릴 수 있게 two_dayago_ts_ex를 만들어놨다.)
	vote_check_time_ts = datetime_to_timestamp(vote_check_time)
	vote_check_time_ts_ex = datetime_to_timestamp(vote_check_time_ex)
	# 포맷) 04/02
	vote_check_time = (datetime.today() - timedelta(days=2)).strftime('%m/%d')
	question_check_time = (datetime.today() - timedelta(days=13)).strftime('%m/%d')
	# 포맷) 2022년 04월 02일
	nowtime_str = datetime.today().strftime('%Y년 %m월 %d일')
	penalty_time_str = (datetime.today() + timedelta(days=4)).strftime('%Y년 %m월 %d일')
	attend_time_str = (datetime.today() + timedelta(days=1)).strftime('%Y년 %m월 %d일')
	question_time_str = (datetime.today() + timedelta(days=12)).strftime('%Y년 %m월 %d일') 
	bookrathon_time_str = (datetime.today() + timedelta(days=13)).strftime('%Y년 %m월 %d일')

def get_timeidx(worksheet, check_time):
    row_data = worksheet.row_values(rol_offset)[col_offset:]
    i = 0
    for time in row_data:
        if (time == check_time):
            return(i)
        i += 1
    return(-1)

