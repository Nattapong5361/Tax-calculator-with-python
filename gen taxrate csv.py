import csv
tax_rate = [
    (150000, 0.00),
    (300000, 0.05),
    (500000, 0.10),
    (750000, 0.15),
    (1000000, 0.20),
    (2000000, 0.25),
    (5000000, 0.30),
    (float('inf'), 0.35)
]
filepath = r"C:\Users\LENOVO\OneDrive\Documents\OneDrive\Desktop\Homework\Final coding\file\names.csv"
with open(filepath,"w",encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile ,lineterminator= "\n")
    for i in tax_rate:
        csvwriter.writerow(i)



with open(filepath,"r",encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)
    print(data)