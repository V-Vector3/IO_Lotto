import sqlite3
import datetime

DT_Now = datetime.datetime.now()

Today = "T{}{}{}".format(DT_Now.year, DT_Now.month, DT_Now.day)
information = sqlite3.connect("info.db")
curs = information.cursor()


def CreateTable():
    curs.execute('CREATE TABLE IF NOT EXISTS students (number INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, howMuch INTEGER DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')


def Setting():
    list_students = ["김현우", "남궁선", "문동규", "박건호", "박성진", "송준혁", "신민규", "오혜성", "이승우", "조우현",
                     "허태윤", '권지율', '김민주', '류승주', '문서연', '엄리원', '임수빈', '장한나', '정성연', '정지영', '정하은', '함지효']
    curs.execute(
        "INSERT INTO 'students' (number, name, howMuch, created_at) VALUES (1, 'ㅎㅇ', 0, 2022)")


def PLus1(num):
    try:
        int(num)
        curs.execute(
            'SELECT * FROM \'{}\' WHERE number=\'{}\''.format(Today, num))
        a = curs.fetchone("['howMuch']")
        if int(a) > 10:
            a = a
        else:
            a = int(a) + 1
        curs.execute('UPDATE')  # 개발 해야함, 지금은 귀찮귀찮 일단 pass
    except:
        print("망해써요")


CreateTable()
Setting()
