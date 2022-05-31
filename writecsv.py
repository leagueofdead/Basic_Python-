# writrcsv.py

import csv
from datetime import datetime

def witerocsv(data): #เป็นการสร้างตัวเก็บข้อมูล

	date = datetime.now().strftime('%Y-%m-%d')

	with open('data-temperature-{}.csv','a',newline='',encoding='utf-8') as file: #เป็นการเก็บข้อมูลไว้ ทำให้ไม่มีช่องว่างnewline='' และให้ไฟล์ของเรารับภาษาไทย encoding='utf-8'
		filewriter = csv.writer(file) #จะได้ไฟล์ writer มา
		filewriter.writerow(data) #เขียนครั้งละ 1 บรรทัด


witerocsv(['กทม',20.5])