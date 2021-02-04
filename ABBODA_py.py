import pyodbc
import csv


def _openODBC(tag):
    sql_0 = "SELECT NUMERICLOG.TIMESTAMP, NUMERICLOG.DATAVALUE, NUMERICLOG.QUALITY  FROM SCHEMA.OAUSER.NUMERICLOG NUMERICLOG  WHERE (NUMERICLOG.LOGNAME='"
    sql_1 = "') AND (NUMERICLOG.TIMESTAMP>{ts '2019-06-01 00:00:00'} And NUMERICLOG.TIMESTAMP<{ts '2020-06-01 00:00:00'}) AND (NUMERICLOG.AGGREGATE='time average') AND (NUMERICLOG.INTERVALS=60)  ORDER BY NUMERICLOG.TIMESTAMP"
    sql_full = sql_0 + tag + sql_1
    # print(sql_full)

    conn = pyodbc.connect('DSN=ABBODA;SDSN=DATABASE1;HST=localhost;PRT=19986')
    cursor = conn.cursor()
    cursor.execute(sql_full)

    raw = cursor.fetchall()
    cursor.close()
    conn.close()
    return raw



def _wtCSV(DB):
    file_name = 'data/' + j.replace(':', '!').replace('\.', '.').replace('/', '.') + '.csv'
    print(file_name)
    with open(file_name, 'w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        for item in DB:
            write.writerow(item)
        f.close()
        print(j, ' Done!')


file_open = open('./taglist.txt', 'r')
file_db = file_open.readlines()
n = 0
for i in file_db:
    n = n + 1
    try:
        j = i.split('\n')[0]
        print('processing:' + j + ' ' + str(n) + '/' + str(len(file_db)))
        _wtCSV(_openODBC(j))
    except Exception as e:
        print(j + 'This Tag Error:' + str(e))
        pass
    continue
