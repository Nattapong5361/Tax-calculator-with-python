import csv
#อัตตราภาษี
#เรียกใช้ไฟล์ csv ที่เก็บอัตราภาษี
with open (r"C:\Users\LENOVO\OneDrive\Documents\OneDrive\Desktop\Homework\TAX_Calculator with python\Tax-calculator-with-python\Tax rates.csv","r",encoding="utf-8") as file:
    csvreader = csv.reader(file)
    unconvert_tax=list(csvreader)
    tax_rate =[]
#แปลง rate (str) เป็น float แล้วเก็บใน list 
    for tax,rate in unconvert_tax :
        if tax == 'inf' :
            tax = float('inf')
            rate = float(rate)
            tax_rate.append((tax,rate))
        else :
            tax = float(tax)
            rate = float(rate)
            tax_rate.append((tax,rate))

# fuctiion คำนวนภาษี      
def calc_tax(net_income):
    tax = 0
    previous_step = 0 #step คือลำดับขั้นภาษีก่อนหน้า
    for step, rate in tax_rate:
        if net_income <= step:
            tax += (net_income - previous_step) * rate
            break
        else:
            tax += (step - previous_step) * rate
            previous_step = step
    return tax

#fuction สร้าง dictionary income และ deduct
def income_add(key, values):
    income.update({key: values})

    total_income = sum(income.values())
    income_list = len(income.keys())

    return total_income, income_list


def deduct_add(key, values):
    deduct.update({key: values})

    total_deduct = sum(deduct.values())
    deduct_list = len(deduct.keys())

    return total_deduct, deduct_list

income = {}
income_list = 0
income_sum = 0
deduct = {}
deduct_list = 0
deduct_sum = 0

print(tax_rate)

test_incomes = [100000, 250000, 600000, 1200000, 3000000, 6000000]

for income_value in test_incomes:
    tax_value = calc_tax(income_value)
    print(f"รายได้ {income_value:,.0f} บาท → ภาษีที่ต้องจ่าย = {tax_value:,.2f} บาท")