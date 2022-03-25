import src.src_info as si
import src.src_time as st

json_key_path = "richstudy-c771b0080ee8.json"	# JSON Key File Path
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1DuBSkKT665lYLiatWSIZ94NssrhH5ErJQheUdFuPYKk/edit#gid=2139714808"
worktab = '벌금명단'
worksheet = si.import_googlesheet(json_key_path, spreadsheet_url, worktab)
col_offset = 3
rol_offset = 4

def write_vote_later(timeidx, later_data):
    timeidx =
    worksheet.update_acell('C5', '= CONCATENATE("11", "1")')



# 쓰기


def write_question_later(timestr, later_data):

def send_later(timestr, later_data, data_type):
    timeidx = st.get_timeidx(worksheet, timestr) + col_offset
    if (data_type = "v"):
        write_vote_later(timeidx, later_data)
    else if (data_type = "q"):
        wirte_question_later(timeidx, later_data)
    else
        print("data_type error(ex. 'v or 'q')")

