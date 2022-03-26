
from oauth2client.service_account import ServiceAccountCredentials
import gspread

class WebHookUrl:
	announcement_webhook = "https://hooks.slack.com/services/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"
	question_webhook = "https://hooks.slack.com/services/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"
	penalty_webhook = "https://hooks.slack.com/services/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"
	cash_fit_webhook = "https://hooks.slack.com/services/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"

class BotOAuth:
	user_token = "xoxp-1830334374899-1853957534688-3251494072295-b70e8bf89cc4d9a0c416d14d3075940e"
	bot_token = "xoxb-1830334374899-2443966688067-w0MZL8043NzMuxjWzAhtK4mw"

class ChannelID:
	announcement = "C01PZAK0NGP"
	book_rec = "C02M3SU81K2"
	question = "C027UQYFH8U"
	penalty = "C029TP5DS0G"
	cash_fit = "C02QY3M5F7H"

class UserID:
	users_name = [
				"강동운",
				"김가현",
				"김민수",
				"김범태",
				"김성훈",
				"김주영",
				"문건호",
				"박상아",
				"박상진",
				"박서지",
				"박재형",
				"박혜빈",
				"서수희",
				"신환종",
				"심혜빈",
				"양희재",
				"윤영주",
				"이재원",
				"이현정",
				"장호진",
				"전진표",
				"정하진",
				"정현진",
				"천지영",
				"최명원",
				"하승희",
				"한수경"
			]
	user_id_to_name = {
				"U02RL2XV4KH" : "강동운",
				"U02RTQ2NXKQ" : "김가현",
				"U02LE7HKCE6" : "김민수",
				"U027JQK00KB" : "김범태",
				"U01QT3KFU4D" : "김성훈",
				"U026RFKEN3H" : "김주영",
				"U02733TKY9K" : "문건호",
				"U02S33JRS9J" : "박상아",
				"U02S4TERJ5S" : "박상진",
				"U02S2LM4LP4" : "박서지",
				"U02S0M72N82" : "박재형",
				"U01QMTD1K37" : "박혜빈",
				"U02S2PVS3B6" : "서수희",
				"U01QSTF6M18" : "신환종",
				"U02RU9NTCA2" : "심혜빈",
				"U01QEPH2TP1" : "양희재",
				"U01QLRF7MJ6" : "윤영주",
				"U02AKLMDSRE" : "이재원",
				"U02RTS9357G" : "이현정",
				"U01R3U5FQL8" : "장호진",
				"U02S3UAPS9J" : "전진표",
				"U02SR22Q9MW" : "정하진",
				"U02727PASNS" : "정현진",
				"U032CUPKA95" : "천지영",
				"U02S0ER3W9H" : "최명원",
				"U02RU5T3KSS" : "하승희",
				"U027382N5K7" : "한수경"
			}
	user_name_to_id = {
				"강동운" : "U02RL2XV4KH",
				"김가현" : "U02RTQ2NXKQ",
				"김민수" : "U02LE7HKCE6",
				"김범태" : "U027JQK00KB",
				"김성훈" : "U01QT3KFU4D",
				"김주영" : "U026RFKEN3H",
				"문건호" : "U02733TKY9K",
				"박상아" : "U02S33JRS9J",
				"박상진" : "U02S4TERJ5S",
				"박서지" : "U02S2LM4LP4",
				"박재형" : "U02S0M72N82",
				"박혜빈" : "U01QMTD1K37",
				"서수희" : "U02S2PVS3B6",
				"신환종" : "U01QSTF6M18",
				"심혜빈" : "U02RU9NTCA2",
				"양희재" : "U01QEPH2TP1",
				"윤영주" : "U01QLRF7MJ6",
				"이재원" : "U02AKLMDSRE",
				"이현정" : "U02RTS9357G",
				"장호진" : "U01R3U5FQL8",
				"전진표" : "U02S3UAPS9J",
				"정하진" : "U02SR22Q9MW",
				"정현진" : "U02727PASNS",
				"천지영" : "U032CUPKA95",
				"최명원" : "U02S0ER3W9H",
				"하승희" : "U02RU5T3KSS",
				"한수경" : "U027382N5K7",
	}

minsu_MSI_key = "richstudy-c771b0080ee8.json"   # JSON Key File Path...minsu
json_key_path = minsu_MSI_key
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1DuBSkKT665lYLiatWSIZ94NssrhH5ErJQheUdFuPYKk/edit#gid=2139714808"


def import_googlesheet(tab):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
    gc = gspread.authorize(credential)
    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet(tab)
    return (worksheet)
