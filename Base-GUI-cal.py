from tkinter import*
#ตัวขนาด
mywin=Tk()
mywin.title('Tax Calculate')
mywin.minsize(700,500)
#หัวข้อ
c1=Label(mywin,text='Calculate Tax',fg='blue',font='Helvetic 20')
c1.grid(column=0, row=0, padx=30, pady=20)
#ช่องใส่เงิน
e1=Label(mywin,text='Income')
e1.place(x=30,y=100)
income=Entry(mywin,width=45)
income.place(x=100,y=100)
b1=Button(mywin,text='in',fg='red',width=10) #ใส่command
b1.place(x=400,y=98)
#คำนวณเพิ่ม
e2=Label(mywin,text='Diduct')
e2.place(x=30,y=156)
add=Entry(mywin,width=45)
add.place(x=100,y=155)
b1=Button(mywin,text='diduct',fg='red',width=10) #ใส่command
b1.place(x=400,y=150)
#ปุ่มคำนวณ
bc=Button(mywin,text='Calculate',fg='green',font='Helvetic 13') #ใส่command
bc.place(x=30,y=230)
#ช่องแสดง1
c01=Label(mywin,text='Income',fg='blue')
c01.place(x=566,y=50)
lb1=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb1.place(width=100,height=100,x=568,y=70)
#ช่องแสดง2
c02=Label(mywin,text='Diduct',fg='blue')
c02.place(x=566,y=180)
lb2=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb2.place(width=100,height=100,x=568,y=200)
#ช่องlog
c00=Label(mywin,text='Log',fg='blue',font='Helvetic 13')
c00.place(x=30,y=300)
lb0=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb0.place(width=640, height=120, x=30,y=325)

mainloop()
