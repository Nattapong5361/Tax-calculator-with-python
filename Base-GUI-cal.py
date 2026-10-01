from tkinter import*
#ตัวขนาด
mywin=Tk()
mywin.title('Tax Calculate')
mywin.minsize(700,500)
#หัวข้อ
c1=Label(mywin,text='Calculate Tax',fg='blue',font='Helvetic 20')
c1.grid(column=0, row=0, padx=30, pady=20)
c1=Label(mywin,
         text='Calculate Tax',
         fg='blue',
         font='Helvetic 20')
c1.grid(column=1,
        row=0,
        columnspan=3,
        padx=(0,130),
        pady=20)
#ช่องใส่ชื่อเงิน
e1=Label(mywin,
         text='Name')
e1.grid(column=0,
        row=1,
        padx=0,
        pady=0)
ni=Entry(mywin,
         text='NAME'
         ,width=45)
ni.grid(column=1,
        row=1,
        padx=0,
        pady=0)

#ช่องใส่เงิน
e1=Label(mywin,text='Income')
e1.place(x=30,y=100)
income=Entry(mywin,width=45)
income.place(x=100,y=100)
b1=Button(mywin,text='in',fg='red',width=10) #ใส่command
b1.place(x=400,y=98)
e2=Label(mywin,
         text='Income')
e2.grid(column=0,
        row=2,
        padx=20,
        pady=0)
income=Entry(mywin,
             width=45)
income.grid(column=1,
            row=2,
            padx=20,
            pady=0)
b1=Button(mywin,
          text='in',
          fg='red',
          width=10) #ใส่command
b1.grid(column=2,
        row=2,
        padx=20,
        pady=0)

#ชื่อคำนวณเพิ่ม
e3=Label(mywin,
         text='Name')
e3.grid(column=0,
        row=4,
        padx=0,
        pady=0)
nd=Entry(mywin,
         width=45)
nd.grid(column=1,
        row=4,
        padx=0,
        pady=0)

#คำนวณเพิ่ม
e2=Label(mywin,text='Diduct')
e2.place(x=30,y=156)
add=Entry(mywin,width=45)
add.place(x=100,y=155)
b1=Button(mywin,text='diduct',fg='red',width=10) #ใส่command
b1.place(x=400,y=150)
e4=Label(mywin,
         text='Diduct')
e4.grid(column=0,
        row=5,
        padx=0,
        pady=0)
deduct=Entry(mywin,
             width=45)
deduct.grid(column=1,
            row=5,
            padx=20,
            pady=0)
b2=Button(mywin,
          text='diduct',
          fg='red',
          width=10) #ใส่command
b2.grid(column=2,
        row=5,
        padx=0,
        pady=0)

#ปุ่มคำนวณ
bc=Button(mywin,text='Calculate',fg='green',font='Helvetic 13') #ใส่command
bc.place(x=30,y=230)
bc=Button(mywin,
          text='Calculate',
          fg='green',
          font='Helvetic 13') #ใส่command
bc.grid(column=0,
        row=7,
        padx=10,
        pady=20)

#ช่องแสดง1
c01=Label(mywin,text='Income',fg='blue')
c01.place(x=566,y=50)
lb1=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb1.place(width=100,height=100,x=568,y=70)
c01=Label(mywin,
          text='Income',
          fg='blue')
c01.grid(column=3,
         row=2,
         padx=(0,100),
         pady=0)
lb1=Listbox(mywin,
            width=30,
            height=3)#หาวิธีแสดงข้อมูล
lb1.grid(column=3,
         row=3,
         padx=30,
         pady=0)

#ช่องแสดง2
c02=Label(mywin,text='Diduct',fg='blue')
c02.place(x=566,y=180)
lb2=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb2.place(width=100,height=100,x=568,y=200)
c02=Label(mywin,
          text='Diduct',
          fg='blue')
c02.grid(column=3,
         row=5,
         padx=30,
         pady=0)
lb2=Listbox(mywin,
            width=30,
            height=3)#หาวิธีแสดงข้อมูล
lb2.grid(column=3,
         row=6,
         padx=30,
         pady=0)

#ช่องlog
c00=Label(mywin,text='Log',fg='blue',font='Helvetic 13')
c00.place(x=30,y=300)
lb0=Listbox(mywin)#หาวิธีแสดงข้อมูล
lb0.place(width=640, height=120, x=30,y=325)
c00=Label(mywin,
          text='Log',
          fg='blue',
          font='Helvetic 13')
c00.grid(column=0,
         row=8,
         padx=0,
         pady=0)
lb0=Listbox(mywin,
            width=120,
            height=6)#หาวิธีแสดงข้อมูล
lb0.grid(column=0,
         row=9,
         columnspan=4,
         padx=30,
         pady=0)

mainloop()
