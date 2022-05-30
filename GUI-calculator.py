from cgitb import text
from struct import pack
from tkinter import *
from tkinter import ttk, messagebox #ทำให้กดปุ่มสามารถคำนวณได้

GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณปลา รถพุ่มพวงของลัน')
GUI.geometry('800x700') #กำหนดหน้าต่างของโปรแกรมเรา

bg = PhotoImage(file = 'car.png') #ดึงไฟล์รถของเรา

BG = Label(GUI,image = bg) #แสดงไฟล์รถ
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา(กิโลกรัม)',font=(None,20)) #Label= ป้ายหรือฉลาก กำหนดข้อความและฟอนต์ตัวอักษร
L.pack()

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็ยข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=(None,20)) # textvariable เป็นการเก็บข้อมูลตัวที่เราพิมพ์เข้ามา
E1.pack() #การเรียกฟังก์ชันขึ้นหน้าจอ

def Cal():
    try: #ทำให้มันไม่ error เมื่อพิมพ์คำสั่งอื่นนอกจากตัวเลข
        quan = float(v_quantity.get()) #ทำการดึงข้อมูลจากที่เราพิมพ์แล้วมาแปลงเป็นตัวเลขเพื่อการคำนวณ ตอนเราพิมพ์ข้อความมันจะเป็น string เลยต้องแปลงเป็นตัวเลข
        calc = quan * 39 #ราคา 39 บาทต่อกิโล *กับจำนวณปลา
        messagebox.showinfo('ราคาปลาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc)) #แสดงจำนวณปลาที่ได้ โดยใช้คำฟั่ง {} และ format 
        v_quantity.set('') #เป็นการเคลียร์ช่องที่กรอก
        E1.focus() #กรอกเสร็จจะโฟกัสที่กรอกเลย
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเป็นตัวเลขเท่านั้น')
        v_quantity.set('') #เป็นการเคลียร์ช่องที่กรอก
        E1.focus() #กรอกเสร็จจะโฟกัสที่กรอกเลย

B = ttk.Button(GUI,text='คำนวณ',command=Cal)  #ใส่ปุ่มเพื่อกดคำนวณและแสดงผลการคำนวณจากฟังก์ชันการคำนวร
B.pack(ipadx=30,ipady=20)  #ipadx  ipady ขยายความกว่าง x/y

GUI.mainloop() #ให้โปรแกรมรันตลอดเวลา