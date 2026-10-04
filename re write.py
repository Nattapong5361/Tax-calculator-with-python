from tkinter import *
import tkinter.filedialog
from pathlib import Path
import csv

#อ่านข้อมูลและแปลงจาก STR เป็น float
def read_tax_rate():
    with open(Path(__file__).with_name("Tax rates.csv"), "r", encoding="utf-8") as file:
        uncompleted_tax_rate = list(csv.reader(file))
        converted_tax = []
        for tax, rate in uncompleted_tax_rate:
            if tax == "inf":
                tax = float("inf")
                rate = float(rate)
                converted_tax.append((tax, rate))
            else:
                tax = float(tax)
                rate = float(rate)
                converted_tax.append((tax, rate))
        return converted_tax

#ลบข้อมูลใน listbox แล้วเพิ่มข้อมูลใหม่
# listbox ที่ต้องการให้สร้างค่า , dict ของข้อมูลปัจจุบัน
def rewrite_listbox(listbox, data):
    listbox.delete(0, END)
    for name, value in data.items():
        listbox.insert(END, f"{name} : {value:,}")

def delete_list(listbox, dict, item_type):
    selected_list = listbox.curselection()
    deleted_key = list(dict)[selected_list[0]]
    del dict[deleted_key]

    rewrite_listbox(listbox, dict)
    log_LB.insert(END, f"ลบรายการ{item_type}: {deleted_key}")

#รับค่า income แล้วเพิ่มเข้า listbox
def income_add():
    name = income_name_entry.get().strip()
    value = income_value_entry.get().strip()
    if name == "" or value == "":
        log_LB.insert(END, "กรอกชื่อรายได้และจำนวนเงิน")
    else:
        try:
            amount = float(value)
        except ValueError:
            log_LB.insert(END, "จำนวนเงินต้องเป็นตัวเลข")
        else:
            income.update({name: amount})
            rewrite_listbox(income_LB, income)
            income_name_entry.delete(0, END)
            income_value_entry.delete(0, END)
            log_LB.insert(END, f"เพิ่มรายได้ {name} : {amount:,}")


def deduct_add():
    name = deduct_name_entry.get().strip()
    value = deduct_value_entry.get().strip()
    if name == "" or value == "":
        log_LB.insert(END, "กรอกชื่อส่วนลด/ค่าใช้จ่ายและจำนวนเงิน")
    else:
        try:
            amount = float(value)
        except ValueError:
            log_LB.insert(END, "จำนวนเงินต้องเป็นตัวเลข")
        else:
            deduct.update({name: amount})
            rewrite_listbox(deduct_LB, deduct)
            deduct_name_entry.delete(0, END)
            deduct_value_entry.delete(0, END)
            log_LB.insert(END, f"เพิ่มส่วนลด/ค่าใช้จ่าย {name} : {amount:,}")


def calc_tax():
    total_income = sum(income.values())
    total_deduct = sum(deduct.values())
    net_income = total_income - total_deduct
    if net_income <= 0:
        net_income = 0

    sum_tax = 0
    previous_step = 0
    for step, rate in tax_rate:
        if net_income <= step:
            sum_tax += (net_income - previous_step) * rate
            break
        else:
            sum_tax += (step - previous_step) * rate
            previous_step = step

    log_LB.insert(END,f"รายได้ {total_income:,},ค่าใช้จ่าย/ส่วนลดหย่อน {total_deduct:,},รายได้สุทธิ {net_income:,},ภาษีที่ต้องจ่าย {sum_tax:,}",)
    show_result(net_income, sum_tax)


def show_result(net_income, sum_tax):
    result_win = Tk()
    result_win.title("ผลคำนวณภาษี")
    result_win.minsize(520, 380)

    income_label = Label(result_win, text="Income", fg="blue")
    income_label.place(x=30, y=20)
    result_income_LB = Listbox(result_win)
    result_income_LB.place(width=200, height=180, x=30, y=45)
    rewrite_listbox(result_income_LB, income)

    deduct_label = Label(result_win, text="ค่าใช้จ่าย + ลดหย่อน", fg="blue")
    deduct_label.place(x=270, y=20)
    result_deduct_LB = Listbox(result_win)
    result_deduct_LB.place(width=200, height=180, x=270, y=45)
    rewrite_listbox(result_deduct_LB, deduct)

    net_income_label = Label(result_win, text=f"รายได้สุทธิ : {net_income:,}", fg="blue", font=("arial", 12))
    net_income_label.place(x=30, y=250)
    sum_tax_label = Label(result_win, text=f"ภาษีที่ต้องจ่าย : {sum_tax:,}", fg="blue", font=("arial", 12))
    sum_tax_label.place(x=30, y=285)

    save_button = Button(result_win, text="บันทึกผล", fg="green", font=("arial", 12), command=save_result)
    save_button.place(x=30, y=325)


def save_result():
    filename = tkinter.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if filename == "" :
        log_LB.insert(END, "ยกเลิกการบันทึกไฟล์")
    else:
        with open(filename, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator="\n")
            for name, value in income.items():
                writer.writerow(["income", name, value])
            for name, value in deduct.items():
                writer.writerow(["deduct", name, value])
        log_LB.insert(END, "บันทึกไฟล์แล้ว")


def import_file():
    filename = tkinter.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filename:
        with open(filename, mode="r", encoding="utf-8") as file:
            data = list(csv.reader(file))

        income.clear()
        deduct.clear()

        for row in data:
            item_type = row[0]
            name = row[1]
            value = row[2]
            if item_type == "income":
                income.update({name: float(value)})
            elif item_type == "deduct":
                deduct.update({name: float(value)})

        rewrite_listbox(income_LB, income)
        rewrite_listbox(deduct_LB, deduct)
        log_LB.insert(END, "โหลดไฟล์แล้ว")


if __name__ == "__main__":
    #ประกาศตัวแปร
    tax_rate = read_tax_rate()
    income = {}
    deduct = {}

    #GUI
    main_window = Tk()
    main_window.title("Tax calculator")
    main_window.minsize(750, 500)

    #heading
    Head = Label(main_window, text="Tax calculator", fg="blue", font=("Arial", 15)).grid(row=0, column=0, padx=20, pady=30)
    #ช่องรับค่า income และ รายจ่าย + ลดหย่อน
    income_name = Label(main_window, text="ชื่อรายได้", font=("arial", 12)).grid(row=1, column=0)
    income_name_entry = Entry(main_window, width=20)
    income_name_entry.grid(row=1, column=1)

    income_value = Label(main_window, text="จำนวนเงิน", font=("arial", 12)).grid(row=1, column=2, padx=10)
    income_value_entry = Entry(main_window, width=20)
    income_value_entry.grid(row=1, column=3, padx=10)

    income_add_button = Button(main_window, text="เพิ่ม", command=income_add).grid(row=1, column=4, padx=10)

    deduct_name = Label(main_window, text="ชื่อส่วนลด+ค่าใช้จ่าย", font=("arial", 12)).grid(row=2, column=0)
    deduct_name_entry = Entry(main_window, width=20)
    deduct_name_entry.grid(row=2, column=1)

    deduct_value = Label(main_window, text="จำนวนเงิน", font=("arial", 12)).grid(row=2, column=2, padx=10)
    deduct_value_entry = Entry(main_window, width=20)
    deduct_value_entry.grid(row=2, column=3, padx=10)

    deduct_add_button = Button(main_window, text="เพิ่ม", command=deduct_add).grid(row=2, column=4, padx=10)

    import_button = Button(main_window, text="นำเข้าไฟล์", command=import_file)
    import_button.place(x=0, y=0)

    #ปุ่ม CALCULATE TAX
    calculate_button = Button(main_window, text="คำนวนภาษี", font=("arial", 20), command=calc_tax).grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    #listbox สำหรับแสดงข้อมูล income deduct log | LB = listbox
    income_LB_label = Label(main_window, text="income", fg="blue", font=("arial", 10)).place(x=580, y=30)
    income_LB = Listbox(main_window)
    income_LB.place(x=580, y=70, width=150, height=100)
    income_delete_button = Button(main_window,text="ลบรายได้",command=lambda: delete_list(income_LB, income, "รายได้"))
    income_delete_button.place(x=605, y=175, width=100)

    deduct_LB_label = Label(main_window, text="deduct and expense", fg="blue", font=("arial", 10)).place(x=580, y=210)
    deduct_LB = Listbox(main_window)
    deduct_LB.place(x=580, y=245, width=150, height=100)
    deduct_delete_button = Button(main_window,text="ลบรายการ",command=lambda: delete_list(deduct_LB, deduct, "ส่วนลด/ค่าใช้จ่าย"))
    deduct_delete_button.place(x=605, y=350, width=100)

    log_LB_Label = Label(main_window, text="Log", fg="blue", font=("arial", 12)).place(x=30, y=315)
    log_LB = Listbox(main_window)
    log_LB.place(width=540, height=120, x=30, y=340)

    mainloop()
