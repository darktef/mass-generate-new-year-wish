import itchat
import xlsxwriter
import csv
import pprint
import random

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

def send_new_year_wishes(itchat):
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

CHRISTMAS_WISHES = [ u'白雪飘，钟声敲，圣诞节又来到；鹿铃响，喜气洋，惬意幸福心情爽；圣歌唱，心花放，吉祥快乐从天降；拇指动，短信转，愿%s圣诞开心伴!', u'身披圣诞衣，见人先作揖；头戴圣诞帽，逢人开口笑；脚穿圣诞靴，请客请吐血；背着圣诞袋，大家用脚踹。圣诞节到了，祝%s开心哦！', u'年年有圣诞，圣诞在年年，吉祥和平安，幸福加欢颜，祝福和问候，温暖来相伴，欢歌和笑语，弥漫情谊间，短信和短信，那是今天的重叠不断，愿%s圣诞快乐，开心平安。'
]
    
def send_christmas_wishes(itchat):
    with open('friends.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for friend in csv_reader:
            if int(friend['GroupLevel']) > 2: continue
            the_one = itchat.search_friends(name=friend['NickName'])[0]
            wish_num = random.randint(0, 2)
            wish = CHRISTMAS_WISHES[wish_num] % (the_one['RemarkName'] or the_one['NickName'])
            itchat.send(wish, toUserName=the_one['UserName'])


itchat.auto_login(hotReload=True)
send_christmas_wishes(itchat)

