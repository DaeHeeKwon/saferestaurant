import csv
import re
import pymysql

safe_restaurant = []
with open('safe_restaurant_20210105.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        line[0]=int(line[0])
        line[1]=int(line[1])
        if line[13]=='null':
            line[13]='9999-12-31'
        else:
            line[13]=line[13]
        safe_restaurant.append(line[:14]+[line[15]])

connection_info = { 'host': 'localhost', 'user': 'root', 'password': 'Kweondh123!', 'db': 'saferestaurant', 'charset': 'utf8' }
        
conn = pymysql.connect(**connection_info)
cursor = conn.cursor()

sql = 'DELETE FROM safe_restaurant'
cursor.execute(sql)

sql = 'INSERT INTO safe_restaurant VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
cursor.executemany(sql, safe_restaurant) # executemany : 여러 개의 데이터를 한 번에 일괄 삽입

conn.commit()

conn.close()