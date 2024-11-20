from plyer import notification
import datetime
import sqlite3
import schedule
import time
from tendo import singleton

me = singleton.SingleInstance()
con = sqlite3.connect('QTproj')
cur = con.cursor()
result = cur.execute(f"""SELECT * FROM date WHERE datee < '{str(datetime.datetime.now().date())}'""").fetchall()
con.close()
if len(result) > 0:
    for j in range(5):
        notification.notify(title='ЦВЕТЫ ВСЕ ЕЩЁ НЕ ПОЛИТЫ', message='ПОЛЕЙ ЦВЕТЫ!!!', app_icon=None, timeout=1)
time.sleep(300)


def job():
    con = sqlite3.connect('QTproj')
    cur = con.cursor()
    result = cur.execute(f"""SELECT * FROM date WHERE datee < '{str(datetime.datetime.now().date())}'""").fetchall()
    con.close()
    if len(result) > 0:
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        result = cur.execute(f"""UPDATE date SET datee = '{str(datetime.datetime.now().date())}' 
        WHERE datee < '{str(datetime.datetime.now().date())}'""").fetchall()
        con.commit()
        con.close()
        for j in range(5):
            notification.notify(title='ЦВЕТЫ ВСЕ ЕЩЁ НЕ ПОЛИТЫ', message='ПОЛЕЙ ЦВЕТЫ!!!', app_icon=None, timeout=1)
        time.sleep(30)
    else:
        con = sqlite3.connect('QTproj')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM date
        WHERE datee='{str(datetime.datetime.now().date())}'
        """).fetchall()
        res = result
        result = []
        if len(res) > 0:
            for i in res:
                result.append(i[1])
            if len(result) > 5:
                a = '\n'.join(result[:5] + ['и др цветы.'])
            else:
                a = '\n'.join(result)
            notification.notify(title='Полей цветы', message=a, app_icon=None, timeout=1)
            con.close()


schedule.every(8).seconds.do(job)
while True:
    schedule.run_pending()
