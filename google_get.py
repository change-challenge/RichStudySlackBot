import src.src_info as si
import src.src_time as st
from datetime import datetime, timedelta
import time

#수정은 src/
worksheet = si.import_googlesheet('2022년 상반기 벌금명단')
#날짜 기준
col_offset = 2
row_offset = 4

def get_later(timestr):
	vote_later = []
	question_later = []
	attend_later = []
	timeidx = st.get_timeidx(col_offset, row_offset, worksheet, timestr)
	if (timeidx == -1):
		print("[ERROR] 해당 날짜는 없어유\n")
		return ("ERROR", "ERROR", "ERROR");
	bits_data = worksheet.col_values(timeidx + col_offset + 1)[row_offset:]
	i = 0
	for result in bits_data:
		if result[0] == '1':
			vote_later.append(si.UserID.users_name[i])
		if result[1] == '1':
			question_later.append(si.UserID.users_name[i])
		if result[2] == '1':
			attend_later.append(si.UserID.users_name[i])
		i += 1
	return (vote_later, question_later, attend_later)


#  v, q, a = get_later(st.TimeStr.check_time)
#v, q, a = get_later('04/02')
#print("투표 지각 :")
#print(v)
#print()
#print("질문 지각 :")
#print(q)
#print()
#print("참석 지각 :")
#print(a)
#print()

#------------------------

# URL로 열기

#  #OR
#
#  Spread Sheet Key로 열기
#  spreadsheet_key = "18n328MQoyReTNKuvvs_3YgLO-JW-bGWodQcKZen63LA"
#  doc = gc.open_by_key(spreadsheet_key)
#
#  #OR
#
#  Spread Sheet 이름으로 열기
#  doc = gc.open("test")

# Sheet 선택
#
#  # 모든 값을 list로 가져오기
#  list_of_lists = worksheet.get_all_values()
#  print(list_of_lists)
#
#  # 모든 값을 dict로 가져오기
#  #  list_of_dicts = sheet.get_all_records()
#  #  pprint(list_of_dicts)
#
# Cell 값 가져오기
#  value_a1 = worksheet.get('A3')
#  print(value_a1)
#
#  # 행 값 가져오기
#  row_data = worksheet.row_values(4)
#  print(row_data[2:])

# 열 값 가져오기
#  col_data = worksheet.col_values(3)
#  print(col_data[4:])
#
#  print()
#  # 범위 값 가져오기
#  rang_data = worksheet.get_values("C5:C31")
#  print(rang_data)
