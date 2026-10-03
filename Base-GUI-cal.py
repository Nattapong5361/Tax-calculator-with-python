from tkinter import*
#หน้าต่าง1
mywin=Tk()
mywin.title('Tax Calculate')
mywin.minsize(700,520)
#หัวข้อ
head=Label(mywin,
           text='Calculate Tax',
           fg='blue',
           font='Helvetic 20')
head.grid(column=1,
          row=0,
          columnspan=3,
          padx=(0,130),
          pady=20)
#ช่องใส่ชื่อเงิน
text_entry1=Label(mywin,
                  text='Name')
text_entry1.grid(column=0,
                 row=1,
                 padx=0,
                 pady=0)
name_enter=Entry(mywin,
                  text='NAME',
                  width=45)
name_enter.grid(column=1,
                row=1,
                padx=0,
                pady=0)

#ช่องใส่เงิน
text_entry2=Label(mywin,
                  text='Income')
text_entry2.grid(column=0,
                 row=2,
                 padx=20,
                 pady=0)
income=Entry(mywin,
             width=45)
income.grid(column=1,
            row=2,
            padx=20,
            pady=0)
income_button=Button(mywin,
          text='in',
          fg='red',
          width=10) #ใส่command
income_button.grid(column=2,
                   row=2,
                   padx=20,
                   pady=0)

#ชื่อคำนวณเพิ่ม
text_entry3=Label(mywin,
                  text='Name')
text_entry3.grid(column=0,
                 row=4,
                 padx=0,
                 pady=0)
name_enter2=Entry(mywin,
                  width=45)
name_enter2.grid(column=1,
                 row=4,
                 padx=0,
                 pady=0)

#คำนวณเพิ่ม
text_entry4=Label(mywin,
                  text='Diduct')
text_entry4.grid(column=0,
                 row=5,
                 padx=0,
                 pady=0)
deduct=Entry(mywin,
             width=45)
deduct.grid(column=1,
            row=5,
            padx=20,
            pady=0)
deduct_button=Button(mywin,
                     text='diduct',
                     fg='red',
                     width=10) #ใส่command
deduct_button.grid(column=2,
                   row=5,
                   padx=0,
                   pady=0)

#ปุ่มคำนวณ
cal_button=Button(mywin,
                  text='Calculate',
                  fg='green',
                  font='Helvetic 13') #ใส่command
cal_button.grid(column=0,
                row=7,
                padx=10,
                pady=20)

#ช่องแสดง1
text_listbox=Label(mywin,
                   text='Income',
                   fg='blue')
text_listbox.grid(column=3,
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
text_listbox2=Label(mywin,
                    text='Diduct',
                    fg='blue')
text_listbox2.grid(column=3,
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
text_listbox3=Label(mywin,
                    text='Log',
                    fg='blue',
                    font='Helvetic 13')
text_listbox3.grid(column=0,
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
#หน้าต่าง2
mywin2=Tk()
mywin2.title('Save')
mywin2.minsize(150,150)
#ตัวแสดงtax ทั้งหมด
text_net=Label(mywin2,
               text='Net income')
text_net.grid(column=0,
              row=1,
              padx=(20,0),
              pady=10)
text_tax=Label(mywin2,
               text='Tax')
text_tax.grid(column=0,
              row=3,
              padx=(0,20),
              pady=10)
#ปุ่มsave
save_button=Button(mywin2,
                   text='Save',
                   fg='green',) #ใส่command
save_button.grid(column=1,
                 row=6,
                 padx=0,
                 pady=20)

mainloop()
