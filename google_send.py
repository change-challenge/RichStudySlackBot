import src.src_info as si
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import src.src_time as st
import slack_get as sk_get
import datetime

# 벌금 공지
# 북라톤 출석부
# https://developers.google.com/sheets/api/limits => 사용 제한
col_offset1 = 2
row_offset1 = 4
col_offset2 = 3
row_offset2 = 4
worksheet1 = si.import_googlesheet('2022년 상반기 벌금명단')
worksheet2 = si.import_googlesheet('북라톤 출석부')

def covert_timestr_to_colnum(timestr):
    timeidx1 = st.get_timeidx(col_offset1, row_offset1, worksheet1, timestr)
    if (timeidx1 == -1):
        print("[ERROR] 해당 날짜는 없어유\n")
        return ;
    timeidx2 = st.get_timeidx(col_offset2, row_offset2, worksheet2, timestr)
    if (timeidx2 == -1):
        print("[ERROR] 해당 날짜는 없어유\n")
        return ;
    return (timeidx1 + col_offset1, timeidx2 + col_offset2)

#chr은 고정의 의미, num은 변화의 의미
def write_vote_later(col_num1, col_num2, row_num1, row_num2, vote_later_data):
    #print("@@@@@@@@@@@구글 시트 작성@@@@@@@@@@@")
    for vote_bit in vote_later_data:
        Penalty = chr(col_num1 + ord('A')) + str(row_num1)
        Attendance = chr(col_num2 + ord('A')) + str(row_num2)
        flag = 0
        if (vote_bit == 0):
            flag = 1
        input_function = "= CONCATENATE(%d, IF(0, IF(\'북라톤 출석부\'!%s = \"X\", \"0\", \"1\"), \"0\"), IF(\'북라톤 출석부\'!%s = \"△\", \"1\", \"0\"))" % (flag, Attendance, Attendance)
        #print(Penalty, "\t<=  \"", input_function, "\"")
        worksheet1.update_acell(Penalty, input_function)
        row_num1 += 1
        row_num2 += 1
        #  time.sleep(0.25);                            # 사람이 너무 많아지면 필요할 수도 있음

def write_question_later(col_num1, col_num2, row_num1, row_num2, question_later_data):
	bits_data = worksheet1.col_values(col_num1 + 1)[row_offset1:]
	#print("@@@@@@@@@@@가져온 기존 데이터@@@@@@@@@@@")
	#print(bits_data, "\n")
	i = 0
	#print("@@@@@@@@@@@구글 시트 작성@@@@@@@@@@@")
	for question_bit in question_later_data:
		Penalty = chr(col_num1 + ord('A')) + str(row_num1)
		Attendance = chr(col_num2 + ord('A')) + str(row_num2)
		vote_flag = 0
		if (bits_data[i][0] == '1'):
			vote_flag = 1
		question_flag = 0
		if (question_bit == 0):
			question_flag = 1
        #input_function = "= CONCATENATE(%d, IF(%d, IF(OR(\'북라톤 출석부\'!%s = \"X\",\'북라톤 출석부\'!%s = ""), \"0\", \"1\"), \"0\"), IF(\'북라톤 출석부\'!%s = \"△\", \"1\", \"0\"))" % (vote_flag, question_flag, Attendance, Attendance, Attendance)
		input_function = "= CONCATENATE(%d, IF(%d, IF(OR(\'북라톤 출석부\'!%s = \"X\",\'북라톤 출석부\'!%s = \"\"), \"0\", \"1\"), \"0\"), IF(\'북라톤 출석부\'!%s = \"△\", \"1\", \"0\"))" % (vote_flag, question_flag, Attendance, Attendance, Attendance)
		#print(Penalty, "\t<=  \"", input_function, "\"")
		worksheet1.update_acell(Penalty, input_function)
		row_num1 += 1
		row_num2 += 1
		i += 1
        #  time.sleep(0.25);                            # 사람이 너무 많아지면 필요할 수도 있음

def send_later(date_time, later_data, data_type):
    col_num1, col_num2 = covert_timestr_to_colnum(date_time)
    row_num1 = row_offset1 + 1                               #날짜 다음 데이터 있는 곳 +1
    row_num2 = row_offset2 + 1                               #날짜 다음 데이터 있는 곳 +1
    if (data_type == 'v'):
        #print("\n[Python] : 투표 지각 여부를 작성합니다...\n")
        write_vote_later(col_num1, col_num2, row_num1, row_num2, later_data)
    elif (data_type == 'q'):
        #print("\n[Python] : 질문 지각 여부를 작성합니다...\n")
        write_question_later(col_num1, col_num2, row_num1, row_num2, later_data)
    else:
        print("data_type error(ex. 'v or 'q')")


def send_richchip():
    col_chip_offset = 18
    row_chip_offset = 5
    book_point = sk_get.get_book_recomd_point()
    idx = 0
    for point in book_point:
        if (point > 0):
            location = chr(col_chip_offset + ord('A')) + str(row_chip_offset)
            if (worksheet2.col_values(col_chip_offset+1)[row_chip_offset-1] == ""):
                data = "%.1f" %(point)
            else:
                old_point = float(worksheet2.col_values(col_chip_offset+1)[row_chip_offset-1])
                data = "= %.1f + %.1f" %(old_point, point)
            worksheet2.update_acell(location, data)
        row_chip_offset += 1


#  print())
#  send_later('04/02', sk_get.get_vote_users(st.TimeStr.vote_check_time_ts_ex), 'v')
#  bits_data = worksheet1.col_values(0 + col_offset1 + 1)[row_offset1:]
#  send_later('04/02', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'v')
#  send_later(sk_get.get_vote_users(st.TimeStr.vote_check_time_ts_ex), [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0], 'v')
#  send_later('04/02', [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], 'q')

#send_later('04/02', sk_get.get_vote_users(datetime.datetime(2022, 3, 19)), 'v')
#send_later('04/02', sk_get.get_question_users(), 'q')

#print(sk_get.get_vote_users(datetime.datetime(2022, 3, 19)))
#  send_later('04/02', , 'q')
