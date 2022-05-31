
from urllib.request import urlopen
from bs4 import BeautifulSoup

alldata = {} #เก็บข้อมูล

import csv
from datetime import datetime

def witerocsv(data): #เป็นการสร้างตัวเก็บข้อมูล

	date = datetime.now().strftime('%Y-%m-%d')

	with open('data-temperature-{}.csv','a',newline='',encoding='utf-8') as file: #เป็นการเก็บข้อมูลไว้ ทำให้ไม่มีช่องว่างnewline='' และให้ไฟล์ของเรารับภาษาไทย encoding='utf-8'
		filewriter = csv.writer(file) #จะได้ไฟล์ writer มา
		filewriter.writerow(data) #เขียนครั้งละ 1 บรรทัด



def checktemp(ID):

	url = 'https://www.tmd.go.th/province.php?id='+ str(ID) #coppy เว็บไซต์ ที่เราจะดึงมา

	webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด chrome
	html_page = webopen.read() #อ่านโค้ดเป็นภาษาคอมพิวเตอร์
	webopen.close()

	data = BeautifulSoup(html_page,'html.parser') #แปลงโค้ดให้ bs4 ช่วยแปลเป็นภาษาที่เราต้องการ

	try:
		temp = data.find('td',{'class':'strokeme'}) #หาโค้ดที่เราจะใช้
		title = data.find('span',{'class':'title'}) #หาโค้ดที่เราจะใช้ของหัวเรื่อง

		city = title.text.strip() #เอาที่ข้อความที่สำคัญ strip() เป็นการตัด  พัทลุง
		temp = temp.text

		#print(city,temp) #เอาที่ข้อความที่สำคัญ
		alldata[city] = temp

	except: #ถ้ามันรันไม่ได้ให้มันผ่านไปเลย
		pass

for i in range(1,101):
	checktemp(i)
	

# print(alldata)

for k,v in alldata.items():
	data = [k,v]
	witerocsv(data)

print('saved')	





