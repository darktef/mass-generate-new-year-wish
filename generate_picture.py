import csv
import subprocess
from subprocess import call

COMMAND_LIST = ['convert', 'happy_new_year.jpg', '-font', 'NotoSansMonoCJKtc', '-fill', '#D21F3C', '-pointsize', '128', '-annotate', '+310+400'] 
SINCERE_WISH = u'祝%s新年快乐！'
RESULT_IMAGE_NAME = u'result_%s.jpg'

with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for friend in csv_reader:
        user_specific_list = [
            SINCERE_WISH % (friend['RemarkName'] or friend['NickName']),
            RESULT_IMAGE_NAME % friend['UserName']
        ]
        call(COMMAND_LIST + user_specific_list)
