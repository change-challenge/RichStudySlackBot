import src.src_info as si
import src.src_time as st

# 벌금 공지
col_offset1 = 3
rol_offset1 = 4

# 북라톤 출석부
col_offset2 = 3
rol_offset2 = 4
worksheet1 = si.import_googlesheet('벌금명단')
worksheet2 = si.import_googlesheet('북라톤 출석부')

def convert_timeidx_to_colrow(timeidx, col_offset, row_offset):
    col_num = timeidx + col_offset + 'A'
    row_num = rol_offset + 1
    return (col_num, row_num)

def write_vote_later(timeidx1, timeidx2, later_data):
    col_num1, row_num1 = convert_timeidx_to_colrow(timeidx1, col_offset1, rol_offset1)
    col_num2, row_num2 = convert_timeidx_to_colrow(timeidx2, col_offset2, rol_offset2)
    #  for vote_late_bits in later_data:
    #      pos = chr(col_num) + chr(row_num)
    #      if (vote_late_bits == 1)
    #          worksheet.update_acell(pos, '= CONCATENATE("1", IF(0, IF(\'북라톤 출석부\'!J5 = "X", "0", "1"), "0"), IF(\'북라톤 출석부\'!J5 = "△", "1", "0"))')
    #      else
    #          worksheet.update_acell(pos, '= CONCATENATE("0", IF(0, IF(\'북라톤 출석부\'!J5 = "X", "0", "1"), "0"), IF(\'북라톤 출석부\'!J5 = "△", "1", "0"))')




# 쓰기


def write_question_later(timeidx, later_data):
    timeidx = st.get_timeidx(worksheet, timestr)
    if (timeidx == -1):
        print("[ERROR] 해당 날짜는 없어유\n")
        return ("ERROR", "ERROR", "ERROR");
    bits_data = worksheet.col_values(timeidx + col_offset)[row_offset:]





def send_later(timestr, later_data, data_type):
    timeidx1 = st.get_timeidx(worksheet1, timestr)
    if (timeidx1 == -1):
        print("[ERROR] 해당 날짜는 없어유\n")
        return ;
    timeidx2 = st.get_timeidx(worksheet2, timestr)
    if (timeidx2 == -1):
        print("[ERROR] 해당 날짜는 없어유\n")
        return ;
    if (data_type = 'v'):
        write_vote_later(timeidx1, timeidx2, later_data)
    else if (data_type = 'q'):
        wirte_question_later(timeidx1, timeidx2, later_data)
    else
        print("data_type error(ex. 'v or 'q')")

send_later('04/02', )
