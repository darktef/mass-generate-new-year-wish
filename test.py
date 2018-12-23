import itchat
import xlsxwriter
import csv
import pprint

USER_ATTR = [
    "City",
    "Province",
    "ContactFlag",
    "NickName",
    "RemarkName",
    "Sex",
    "Signature",
    "Uin",
    "UserName",
    "GroupLevel"
]

def collect_friends():
    friend_list = itchat.get_friends(update=True)
    write_to_csv(friend_list)

def write_to_xlsx(friend_list):
    workbook = xlsxwriter.Workbook('friends.xlsx')
    worksheet = workbook.add_worksheet()

    col = 0
    for attr in USER_ATTR:
        worksheet.write(0, col, attr)
        col += 1

    row = 1
    for friend in friend_list[1:]:
        col = 0

        for attr in USER_ATTR:
            worksheet.write(row, col, friend[attr])
            col += 1

        row += 1

    workbook.close()

def write_to_csv(friend_list):
    with open('friends.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=USER_ATTR, extrasaction='ignore')
        writer.writeheader()

        for friend in friend_list[1:]:
            friend["GroupLevel"] = 0
            writer.writerow(friend)

RESULT_IMAGE_NAME = u'result_%s.jpg'
SINCERE_WISH = u'祝%s新年快乐！'

def send_wishes(itchat):
    with open('test.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for friend in csv_reader:
            finds = itchat.search_friends(name=friend['NickName'])
            if len(finds) > 1: continue

            the_one = itchat.search_friends(name=friend['NickName'])[0]
            # wish = SINCERE_WISH % (friend['RemarkName'] or friend['NickName'])
            # itchat.send(wish, toUserName=the_one['UserName'])
            image_name = RESULT_IMAGE_NAME % friend['UserName']
            itchat.send_image(image_name, toUserName=the_one['UserName'])
    
itchat.auto_login(hotReload=True)
send_wishes(itchat)

# collect_friends()

