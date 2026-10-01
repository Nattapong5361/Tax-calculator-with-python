from tkinter import*
#ตัวขนาด
mywin=Tk()
mywin.title('Tax Calculate')
mywin.minsize(700,520)
#หัวข้อ
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
bc=Button(mywin,
          text='Calculate',
          fg='green',
          font='Helvetic 13') #ใส่command
bc.grid(column=0,
        row=7,
        padx=10,
        pady=20)

#ช่องแสดง1
c01=Label(mywin,
          text='Income',
          fg='blue')
c01.grid(column=3,
         row=1,
         padx=(0,140),
         pady=0)
lb1=Listbox(mywin,
            bg='light cyan',
            width=30,
            height=5)#หาวิธีแสดงข้อมูล
lb1.grid(column=3,
         row=2,
         rowspan=2,
         padx=30,
         pady=0)

#ช่องแสดง2
c02=Label(mywin,
          text='Diduct',
          fg='blue')
c02.grid(column=3,
         row=4,
         padx=(0,140),
         pady=0)
lb2=Listbox(mywin,
            bg='light cyan',
            width=30,
            height=5)#หาวิธีแสดงข้อมูล
lb2.grid(column=3,
         row=5,
         rowspan=2,
         padx=30,
         pady=0)

#เส้นกั้น
li=Label(mywin,
          text='------------------------------------------------------------------------------------------------------------------------------------------------------')
li.grid(column=0,
        row=8,
        columnspan=4)
#ช่องlog
c00=Label(mywin,
          text='Log',
          fg='blue',
          font='Helvetic 13')
c00.grid(column=0,
         row=9,
         padx=0,
         pady=0)
lb0=Listbox(mywin,
            bg='light cyan',
            width=120,
            height=6)#หาวิธีแสดงข้อมูล
lb0.grid(column=0,
         row=10,
         columnspan=4,
         padx=30,
         pady=0)

mainloop()
