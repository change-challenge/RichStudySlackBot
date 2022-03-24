from oauth2client.service_account import ServiceAccountCredentials
import gspread
import src_info as si

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
json_key_path = "./richstudy-f9673624cbe9.json"	# JSON Key File Path
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1DuBSkKT665lYLiatWSIZ94NssrhH5ErJQheUdFuPYKk/edit#gid=2139714808"

#  def import_gsheet(spreadsheet_url, timeidx):
credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet("벌금명단")

row_data = worksheet.row_values(4)
print(row_data[2:])
#  col_data = worksheet.col_values(timeidx)
worksheet.update_acell('C5', '= CONCATENATE("00", "1")')
    #  return (col_data[4:])

def get_later(spreadsheet_url, timeidx):
    vote_later = []
    question_later = []
    attend_later = []
    bits_data = import_gsheet(spreadsheet_url, timeidx)
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


#  google_day = sr...
#  for go
#  google_idx = google_day()
#  timeidx = 3
#  v, q, a = get_later(spreadsheet_url, timeidx)
#  print("투표 지각 :")
#  print(v)
#  print()
#  print("질문 지각 :")
#  print(q)
#  print()
#  print("참석 지각 :")
#  print(a)
#  print()
#------------------------
# 쓰기

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
