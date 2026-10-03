from tkinter import *
import tkinter.filedialog
import csv
import os
#อัตตราภาษี
#เรียกใช้ไฟล์ csv ที่เก็บอัตราภาษี
def read_tax_rate():
    csv_path = os.path.join(os.path.dirname(__file__), "Tax rates.csv")
    with open(csv_path, "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        unconvert_tax = list(csvreader)
        tax_rate = []
    #แปลง rate (str) เป็น float แล้วเก็บใน list 
        for tax, rate in unconvert_tax:
            if tax == 'inf':
                tax = float('inf')
                rate = float(rate)
                tax_rate.append((tax, rate))
            else :
                tax = float(tax)
                rate = float(rate)
                tax_rate.append((tax, rate))
        return tax_rate

# fuctiion คำนวนภาษี      
def calc_tax():
    total_income = sum(income.values())
    total_deduct = sum(deduct.values())
    net_income = total_income - total_deduct
    if net_income < 0:
        net_income = 0

    tax = 0
    previous_step = 0 #step คือลำดับขั้นภาษีก่อนหน้า
    for step, rate in tax_rate:
        if net_income <= step:
            tax += (net_income - previous_step) * rate
            break
        else:
            tax += (step - previous_step) * rate
            previous_step = step
    lb0.insert(END, f"รายได้ {total_income} ลดหย่อน/ค่าใช้จ่าย {total_deduct} รายได้สุทธิ {net_income} ภาษี {tax}")
    show_result(net_income, tax)





def show_result(net_income, tax):
    result_win = Toplevel()
    result_win.title('ผลคำนวณภาษี')
    result_win.minsize(520, 380)

    c1 = Label(result_win, text='Income', fg='blue')
    c1.place(x=30, y=20)
    lb_income = Listbox(result_win)
    lb_income.place(width=200, height=180, x=30, y=45)
    add_dict(lb_income, income)

    c2 = Label(result_win, text='ค่าใช้จ่าย + ลดหย่อน', fg='blue')
    c2.place(x=270, y=20)
    lb_deduct = Listbox(result_win)
    lb_deduct.place(width=200, height=180, x=270, y=45)
    add_dict(lb_deduct, deduct)

    c3 = Label(result_win, text=f'Net income : {net_income}', fg='blue', font='Helvetic 12')
    c3.place(x=30, y=250)
    c4 = Label(result_win, text=f'Tax : {tax}', fg='blue', font='Helvetic 12')
    c4.place(x=30, y=285)

    bs = Button(result_win, text='บันทึกผล', fg='green', font='Helvetic 12', command=save_result)
    bs.place(x=30, y=325)


def save_result():
    # ให้ผู้ใช้เลือกชื่อไฟล์ที่จะบันทึก
    filename = tkinter.filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])

    if not filename:   #ไว้ใช้ตอน user กด cancel
        lb0.insert(END, "ยกเลิกการบันทึกไฟล์")
    else:
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['type', 'name', 'value'])
            for name, value in income.items():
                writer.writerow(['income', name, value])
            for name, value in deduct.items():
                writer.writerow(['deduct', name, value])

        lb0.insert(END, 'บันทึกไฟล์แล้ว')

def import_file():
    filename = tkinter.filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    if filename:
        with open(filename, mode='r', encoding='utf-8', newline='') as file:
            rows = list(csv.reader(file))

        income.clear()
        deduct.clear()
        for row in rows:
            if len(row) < 3 or row[0] == 'type':
                continue
            kind, name, value = row[0], row[1], row[2]
            if kind == 'income':
                income[name] = float(value)
            elif kind == 'deduct':
                deduct[name] = float(value)

        add_dict(lb1, income)
        add_dict(lb2, deduct)
        lb0.insert(END, 'โหลดไฟล์แล้ว')


#เขียนค่าที่รับเข้ามาลง listbox
def add_dict(listbox, data):
    listbox.delete(0, END)
    for name, value in data.items():
        listbox.insert(END, f"{name} : {value}")

# รับจากช่องกรอก แล้วเก็บลง dictionary income 
def income_add():
    name = income_name.get().strip()
    amount_text = income_amount.get().strip()

    if name == "" or amount_text == "":
        lb0.insert(END, "กรอก income name และ income")
    else:
        try:
            amount = float(amount_text)
        except ValueError:
            lb0.insert(END, "income ต้องเป็นตัวเลข")
        else:
            income.update({name: amount})
            total_income = sum(income.values())
            income_list = len(income.keys())

            add_dict(lb1, income)
            income_name.delete(0, END)
            income_amount.delete(0, END)
            lb0.insert(END, f"เพิ่มรายได้ {name} : {amount} รวม {total_income} ({income_list} รายการ)")



# รับจากช่องกรอก แล้วเก็บลง dictionary deduct
def deduct_add():
    name = deduct_name.get().strip()
    amount_text = deduct_amount.get().strip()

    if name == "" or amount_text == "":
        lb0.insert(END, "กรอก deduct name และ deduct")
    else:
        try:
            amount = float(amount_text)
        except ValueError:
            lb0.insert(END, "deduct ต้องเป็นตัวเลข")
        else:
            deduct.update({name: amount})
            total_deduct = sum(deduct.values())
            deduct_list = len(deduct.keys())

            add_dict(lb2, deduct)
            deduct_name.delete(0, END)
            deduct_amount.delete(0, END)
            lb0.insert(END, f"เพิ่มลดหย่อน/ค่าใช้จ่าย {name} : {amount} รวม {total_deduct} ({deduct_list} รายการ)")



""""""""""""""""""""""""""""""""""""""
#โปรแกรมหลัก

if __name__ == "__main__":
    #กำหนดตัวแปร
    tax_rate = read_tax_rate()
    income = {}
    deduct = {}
    
    #ตัวขนาด
    mywin = Tk()
    mywin.title('Tax Calculate')
    mywin.minsize(700, 500)
    bi = Button(mywin, text='Import', command=import_file)
    bi.place(x=620, y=10)
    #หัวข้อ
    c1 = Label(mywin, text='Calculate Tax', fg='blue', font='Helvetic 20')
    c1.grid(column=0, row=0, padx=30, pady=20)
    #ช่องใส่เงิน
    e1 = Label(mywin, text='Income name')
    e1.place(x=30, y=100)
    income_name = Entry(mywin, width=14)
    income_name.place(x=120, y=100)
    e1b = Label(mywin, text='Income')
    e1b.place(x=230, y=100)
    income_amount = Entry(mywin, width=14)
    income_amount.place(x=280, y=100)
    b1 = Button(mywin, text='Add', fg='red', width=10, command=income_add)
    b1.place(x=400, y=98)
    #ลดหย่อน + ค่าใช้จ่าย
    e2 = Label(mywin, text='Deduct name')
    e2.place(x=30, y=156)
    deduct_name = Entry(mywin, width=14)
    deduct_name.place(x=120, y=155)
    e2b = Label(mywin, text='Deduct')
    e2b.place(x=230, y=156)
    deduct_amount = Entry(mywin, width=14)
    deduct_amount.place(x=280, y=155)
    b2 = Button(mywin, text='Add', fg='red', width=10, command=deduct_add)
    b2.place(x=400, y=150)
    #ปุ่มคำนวณ
    bc = Button(mywin, text='Calculate', fg='green', font='Helvetic 13', command=calc_tax)
    bc.place(x=30, y=230)
    #ช่องแสดง1
    c01 = Label(mywin, text='Income', fg='blue')
    c01.place(x=530, y=50)
    lb1 = Listbox(mywin) #listbox income
    lb1.place(width=150, height=100, x=530, y=70)
    #ช่องแสดง2
    c02 = Label(mywin, text='Deduct', fg='blue')
    c02.place(x=530, y=180)
    lb2 = Listbox(mywin) #listbox deduct
    lb2.place(width=150, height=100, x=530, y=200)
    #ช่องlog
    c00 = Label(mywin, text='Log', fg='blue', font='Helvetic 13')
    c00.place(x=30, y=300)
    lb0 = Listbox(mywin)
    lb0.place(width=640, height=120, x=30, y=325)

    mainloop()
