from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

json_key_path = "./logical-tea-345007-5edc511aecb4.json"	# JSON Key File Path

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)

# URL로 열기
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1DuBSkKT665lYLiatWSIZ94NssrhH5ErJQheUdFuPYKk/edit#gid=1319193929"
doc = gc.open_by_url(spreadsheet_url)

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
worksheet = doc.worksheet("벌금명단")
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
row_data = worksheet.row_values(2)
print(row_data[1:])

# 열 값 가져오기
col_data = worksheet.col_values(2)
print(col_data[2:])
col_data = worksheet.col_values(3)
print(col_data[2:])

# 열 값 가져오기
#  rang_data = worksheet.get_values("B3:B7")
#  print(rang_data)
vote_later = []
question_later = []
attend_later = []

i = 0
data = ['101', '010', '100'];
for result in data :
    print(result)
    if result[0] == '1':
        print(result[0])
        vote_later.append(i)
    if result[1] == '1':
        print(result[1])
        question_later.append(i)
    if result[2] == '1':
        print(result[2])
        attend_later.append(i)
    i += 1

print("투표 지각 :", vote_later)
print("질문 지각 :", question_later)
print("참석 지각 :", attend_later)


#------------------------
# 쓰기
#  worksheet.update_acell('B3', '= CONCATENATE("00", "1")')
